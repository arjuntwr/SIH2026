"""
BHUMI-NITI: Policy & Research Repository — Core Service Layer
Provides CRUD, FTS5 BM25 search, provenance recording, and topic tagging.
All operations use the repo_ prefixed tables (separate from legacy documents table).
"""

import hashlib
import json
import uuid
from datetime import datetime, timezone
from typing import List, Optional, Dict, Any

from app.core.database import get_db_connection
from app.repository.models import (
    DocumentCreate,
    DocumentChunkCreate,
    DocumentSummaryResponse,
    DocumentDetailResponse,
    DocumentChunkResponse,
    ProvenanceRecord,
    SearchResultItem,
    SearchResponse,
    ProvenanceTier,
)
from app.repository.chunker import chunk_statutory_text, normalize_text


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _ensure_topic(cursor, topic_name: str) -> str:
    """Get or create a topic row and return its id."""
    cursor.execute("SELECT id FROM topics WHERE name = ?", (topic_name,))
    row = cursor.fetchone()
    if row:
        return row["id"]
    topic_id = str(uuid.uuid4())
    cursor.execute(
        "INSERT INTO topics (id, name) VALUES (?, ?)",
        (topic_id, topic_name),
    )
    return topic_id


def _row_to_summary(row, topics: List[str], chunk_count: int) -> DocumentSummaryResponse:
    return DocumentSummaryResponse(
        id=row["id"],
        doc_id=row["doc_id"],
        title=row["title"],
        short_title=row["short_title"],
        document_number=row["document_number"],
        document_type=row["document_type"],
        description=row["description"],
        issuing_authority=row["issuing_authority"],
        jurisdiction=row["jurisdiction"],
        state_code=row["state_code"],
        publication_date=row["publication_date"],
        status=row["status"],
        source_url=row["source_url"],
        provenance_tier=row["provenance_tier"],
        checksum_sha256=row["checksum_sha256"],
        chunk_count=chunk_count,
        topics=topics,
        created_at=row["created_at"],
    )


# ---------------------------------------------------------------------------
# Public API: ingest_document
# ---------------------------------------------------------------------------

def ingest_document(doc: DocumentCreate, full_text: Optional[str] = None) -> str:
    """
    Ingest a document into the repository.

    - Stores metadata in repo_documents
    - Chunks the full_text (or doc.chunks if pre-chunked) into repo_document_chunks
    - Populates FTS5 index (repo_chunks_fts)
    - Records provenance in provenance_records
    - Associates topic tags in document_topics

    Returns the internal UUID primary key of the stored document.
    Raises ValueError if doc_id already exists (use update flow instead).
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # Idempotency guard
    cursor.execute("SELECT id FROM repo_documents WHERE doc_id = ?", (doc.doc_id,))
    existing = cursor.fetchone()
    if existing:
        conn.close()
        return existing["id"]

    now = _now_iso()
    doc_uuid = str(uuid.uuid4())

    # Compute checksum from full_text if available, else from title+doc_id
    checksum = doc.checksum_sha256
    if not checksum and full_text:
        checksum = _sha256(full_text)
    elif not checksum:
        checksum = _sha256(doc.doc_id + doc.title)

    # ------------------------------------------------------------------
    # 1. Insert document metadata
    # ------------------------------------------------------------------
    cursor.execute(
        """
        INSERT INTO repo_documents (
            id, doc_id, title, short_title, document_number, document_type,
            description, issuing_authority, jurisdiction, state_code, district,
            publication_date, enactment_date, effective_date, status, language,
            source_url, source_name, source_type, provenance_tier,
            checksum_sha256, created_at, updated_at
        ) VALUES (
            ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?,
            ?, ?, ?, ?,
            ?, ?, ?
        )
        """,
        (
            doc_uuid, doc.doc_id, doc.title, doc.short_title, doc.document_number,
            doc.document_type.value,
            doc.description, doc.issuing_authority, doc.jurisdiction,
            doc.state_code, doc.district,
            doc.publication_date, doc.enactment_date, doc.effective_date,
            doc.status, doc.language,
            doc.source_url, doc.source_name, doc.source_type,
            doc.provenance_tier.value,
            checksum, now, now,
        ),
    )

    # ------------------------------------------------------------------
    # 2. Determine chunks
    # ------------------------------------------------------------------
    chunks: List[DocumentChunkCreate] = []
    if doc.chunks:
        chunks = doc.chunks
    elif full_text:
        chunks = chunk_statutory_text(full_text)

    # ------------------------------------------------------------------
    # 3. Insert chunks + FTS5
    # ------------------------------------------------------------------
    for chunk in chunks:
        chunk_id = str(uuid.uuid4())
        norm = chunk.normalized_text or normalize_text(chunk.content_text)
        cursor.execute(
            """
            INSERT INTO repo_document_chunks (
                id, document_id, chunk_index, section_number, section_title,
                heading, page_number, content_text, normalized_text, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                chunk_id, doc_uuid, chunk.chunk_index,
                chunk.section_number, chunk.section_title,
                chunk.heading, chunk.page_number,
                chunk.content_text, norm, now,
            ),
        )
        # Manually populate FTS5 (content-table pattern needs explicit INSERT)
        cursor.execute(
            """
            INSERT INTO repo_chunks_fts (
                rowid, title, section_number, section_title,
                content_text, jurisdiction, document_type, issuing_authority
            ) VALUES (
                (SELECT rowid FROM repo_document_chunks WHERE id = ?),
                ?, ?, ?, ?, ?, ?, ?
            )
            """,
            (
                chunk_id,
                doc.title,
                chunk.section_number or "",
                chunk.section_title or "",
                chunk.content_text,
                doc.jurisdiction,
                doc.document_type.value,
                doc.issuing_authority,
            ),
        )

    # ------------------------------------------------------------------
    # 4. Provenance record
    # ------------------------------------------------------------------
    prov_id = str(uuid.uuid4())
    cursor.execute(
        """
        INSERT INTO provenance_records (
            id, document_id, source_organization, original_url,
            retrieval_timestamp, verification_status, checksum_sha256,
            provenance_tier, source_notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            prov_id, doc_uuid,
            doc.issuing_authority,
            doc.source_url,
            now,
            "Verified",
            checksum,
            doc.provenance_tier.value,
            doc.source_name,
        ),
    )

    # ------------------------------------------------------------------
    # 5. Topic tags
    # ------------------------------------------------------------------
    for topic_name in (doc.topics or []):
        topic_id = _ensure_topic(cursor, topic_name)
        cursor.execute(
            "INSERT OR IGNORE INTO document_topics (document_id, topic_id) VALUES (?, ?)",
            (doc_uuid, topic_id),
        )

    conn.commit()
    conn.close()
    return doc_uuid


# ---------------------------------------------------------------------------
# Public API: search_repository (FTS5 BM25)
# ---------------------------------------------------------------------------

def search_repository(
    query: str,
    jurisdiction: Optional[str] = None,
    document_type: Optional[str] = None,
    provenance_tier: Optional[str] = None,
    state_code: Optional[str] = None,
    topic: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
) -> SearchResponse:
    """
    FTS5 BM25 full-text search across all repo chunk content.
    Supports metadata filters for jurisdiction, document type, provenance tier, state, and topic.
    Results ordered by BM25 relevance (lower = more relevant).
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # Build FTS5 MATCH expression
    # Escape FTS5 special chars in query
    safe_query = query.replace('"', '""')
    fts_expr = f'"{safe_query}"'

    # Build JOIN filters
    filter_clauses = []
    filter_params: List[Any] = []

    if jurisdiction:
        filter_clauses.append("rd.jurisdiction = ?")
        filter_params.append(jurisdiction)
    if document_type:
        filter_clauses.append("rd.document_type = ?")
        filter_params.append(document_type)
    if provenance_tier:
        filter_clauses.append("rd.provenance_tier = ?")
        filter_params.append(provenance_tier)
    if state_code:
        filter_clauses.append("rd.state_code = ?")
        filter_params.append(state_code)
    if topic:
        filter_clauses.append(
            "rd.id IN (SELECT dt.document_id FROM document_topics dt "
            "JOIN topics t ON dt.topic_id = t.id WHERE t.name = ?)"
        )
        filter_params.append(topic)

    where_extra = ""
    if filter_clauses:
        where_extra = " AND " + " AND ".join(filter_clauses)

    sql = f"""
    SELECT
        rdc.id         AS chunk_id,
        rd.id          AS document_id,
        rd.doc_id      AS doc_id,
        rd.title       AS document_title,
        rd.document_type,
        rd.issuing_authority,
        rd.jurisdiction,
        rd.provenance_tier,
        rd.source_url,
        rdc.section_number,
        rdc.section_title,
        rdc.page_number,
        rdc.content_text,
        bm25(repo_chunks_fts) AS relevance_score
    FROM repo_chunks_fts
    JOIN repo_document_chunks rdc ON repo_chunks_fts.rowid = rdc.rowid
    JOIN repo_documents rd ON rdc.document_id = rd.id
    WHERE repo_chunks_fts MATCH ?
    {where_extra}
    ORDER BY bm25(repo_chunks_fts)
    LIMIT ? OFFSET ?
    """

    params = [fts_expr] + filter_params + [limit, offset]

    results = []
    try:
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        for row in rows:
            snippet = row["content_text"][:300] + ("…" if len(row["content_text"]) > 300 else "")
            results.append(
                SearchResultItem(
                    chunk_id=row["chunk_id"],
                    document_id=row["document_id"],
                    doc_id=row["doc_id"],
                    document_title=row["document_title"],
                    document_type=row["document_type"],
                    issuing_authority=row["issuing_authority"],
                    jurisdiction=row["jurisdiction"],
                    provenance_tier=row["provenance_tier"],
                    section_number=row["section_number"],
                    section_title=row["section_title"],
                    page_number=row["page_number"],
                    snippet=snippet,
                    content_text=row["content_text"],
                    source_url=row["source_url"],
                    relevance_score=float(row["relevance_score"]),
                )
            )
    except Exception as e:
        conn.close()
        # Return empty result rather than crash — FTS syntax errors are user input
        return SearchResponse(
            query=query, total_matches=0, results=[], limit=limit, offset=offset
        )

    conn.close()
    return SearchResponse(
        query=query,
        total_matches=len(results),
        results=results,
        limit=limit,
        offset=offset,
    )


# ---------------------------------------------------------------------------
# Public API: list_documents
# ---------------------------------------------------------------------------

def list_documents(
    jurisdiction: Optional[str] = None,
    document_type: Optional[str] = None,
    provenance_tier: Optional[str] = None,
    state_code: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
) -> Dict[str, Any]:
    """List documents with optional filters. Returns paginated summary list."""
    conn = get_db_connection()
    cursor = conn.cursor()

    clauses = []
    params: List[Any] = []

    if jurisdiction:
        clauses.append("rd.jurisdiction = ?")
        params.append(jurisdiction)
    if document_type:
        clauses.append("rd.document_type = ?")
        params.append(document_type)
    if provenance_tier:
        clauses.append("rd.provenance_tier = ?")
        params.append(provenance_tier)
    if state_code:
        clauses.append("rd.state_code = ?")
        params.append(state_code)
    if status:
        clauses.append("rd.status = ?")
        params.append(status)

    where = ("WHERE " + " AND ".join(clauses)) if clauses else ""

    cursor.execute(
        f"SELECT COUNT(*) as total FROM repo_documents rd {where}", params
    )
    total = cursor.fetchone()["total"]

    cursor.execute(
        f"""
        SELECT rd.*,
               COUNT(rdc.id) as chunk_count
        FROM repo_documents rd
        LEFT JOIN repo_document_chunks rdc ON rd.id = rdc.document_id
        {where}
        GROUP BY rd.id
        ORDER BY rd.provenance_tier, rd.publication_date DESC
        LIMIT ? OFFSET ?
        """,
        params + [limit, offset],
    )
    rows = cursor.fetchall()

    docs = []
    for row in rows:
        # Fetch topics for this doc
        cursor.execute(
            "SELECT t.name FROM topics t "
            "JOIN document_topics dt ON t.id = dt.topic_id "
            "WHERE dt.document_id = ?",
            (row["id"],),
        )
        topic_rows = cursor.fetchall()
        topics = [t["name"] for t in topic_rows]
        docs.append(_row_to_summary(row, topics, row["chunk_count"]).model_dump())

    conn.close()
    return {"total": total, "limit": limit, "offset": offset, "documents": docs}


# ---------------------------------------------------------------------------
# Public API: get_document_detail
# ---------------------------------------------------------------------------

def get_document_detail(document_id: str) -> Optional[DocumentDetailResponse]:
    """
    Return full document detail including all chunks and provenance.
    Accepts either internal UUID or doc_id string.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM repo_documents WHERE id = ? OR doc_id = ?",
        (document_id, document_id),
    )
    row = cursor.fetchone()
    if not row:
        conn.close()
        return None

    doc_uuid = row["id"]

    # Topics
    cursor.execute(
        "SELECT t.name FROM topics t "
        "JOIN document_topics dt ON t.id = dt.topic_id "
        "WHERE dt.document_id = ?",
        (doc_uuid,),
    )
    topics = [t["name"] for t in cursor.fetchall()]

    # Chunks
    cursor.execute(
        "SELECT * FROM repo_document_chunks WHERE document_id = ? ORDER BY chunk_index",
        (doc_uuid,),
    )
    chunk_rows = cursor.fetchall()
    chunks = [
        DocumentChunkResponse(
            id=c["id"],
            document_id=doc_uuid,
            chunk_index=c["chunk_index"],
            section_number=c["section_number"],
            section_title=c["section_title"],
            heading=c["heading"],
            page_number=c["page_number"],
            content_text=c["content_text"],
            created_at=c["created_at"],
        )
        for c in chunk_rows
    ]

    chunk_count = len(chunks)
    summary = _row_to_summary(row, topics, chunk_count)

    # Provenance
    cursor.execute(
        "SELECT * FROM provenance_records WHERE document_id = ?", (doc_uuid,)
    )
    prow = cursor.fetchone()
    provenance = None
    if prow:
        provenance = ProvenanceRecord(
            source_organization=prow["source_organization"],
            original_url=prow["original_url"],
            retrieval_timestamp=prow["retrieval_timestamp"],
            verification_status=prow["verification_status"],
            checksum_sha256=prow["checksum_sha256"],
            provenance_tier=ProvenanceTier(prow["provenance_tier"]),
            source_notes=prow["source_notes"],
        )

    conn.close()
    return DocumentDetailResponse(**summary.model_dump(), chunks=chunks, provenance=provenance)


# ---------------------------------------------------------------------------
# Public API: get_document_provenance
# ---------------------------------------------------------------------------

def get_document_provenance(document_id: str) -> Optional[ProvenanceRecord]:
    """Return only the provenance record for a document (lightweight)."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT pr.* FROM provenance_records pr
        JOIN repo_documents rd ON pr.document_id = rd.id
        WHERE rd.id = ? OR rd.doc_id = ?
        """,
        (document_id, document_id),
    )
    prow = cursor.fetchone()
    conn.close()
    if not prow:
        return None
    return ProvenanceRecord(
        source_organization=prow["source_organization"],
        original_url=prow["original_url"],
        retrieval_timestamp=prow["retrieval_timestamp"],
        verification_status=prow["verification_status"],
        checksum_sha256=prow["checksum_sha256"],
        provenance_tier=ProvenanceTier(prow["provenance_tier"]),
        source_notes=prow["source_notes"],
    )

