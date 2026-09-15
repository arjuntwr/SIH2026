"""
BHUMI-NITI: Policy & Research Repository Domain Models
Strict provenance hierarchy and typed schemas for land governance material.
"""

from enum import Enum
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class ProvenanceTier(str, Enum):
    """
    Three-Tier Provenance Hierarchy:
    - TIER_1_AUTHORITATIVE_GOVERNMENT: Official Gazette, Acts, Rules, Government Orders, India Code.
    - TIER_2_RESEARCH_INSTITUTIONAL: NITI Aayog, Academic Papers, Policy Reports, Think Tanks.
    - TIER_3_DERIVED_BHUMI_NITI: Synthesized summaries, cross-statutory matrices, derived metrics.
    """
    TIER_1_AUTHORITATIVE_GOVERNMENT = "TIER_1_AUTHORITATIVE_GOVERNMENT"
    TIER_2_RESEARCH_INSTITUTIONAL = "TIER_2_RESEARCH_INSTITUTIONAL"
    TIER_3_DERIVED_BHUMI_NITI = "TIER_3_DERIVED_BHUMI_NITI"


class DocumentType(str, Enum):
    ACT = "Act"
    RULE = "Rule"
    REGULATION = "Regulation"
    NOTIFICATION = "Notification"
    CIRCULAR = "Circular"
    GUIDELINE = "Guideline"
    SCHEME = "Scheme"
    POLICY_PAPER = "Policy_Paper"
    RESEARCH_REPORT = "Research_Report"
    CASE_STUDY = "Case_Study"
    COURT_PRECEDENT = "Court_Precedent"
    DATASET = "Dataset"


class DocumentChunkCreate(BaseModel):
    chunk_index: int
    section_number: Optional[str] = None
    section_title: Optional[str] = None
    heading: Optional[str] = None
    page_number: Optional[int] = None
    content_text: str
    normalized_text: Optional[str] = None


class DocumentChunkResponse(BaseModel):
    id: str
    document_id: str
    chunk_index: int
    section_number: Optional[str] = None
    section_title: Optional[str] = None
    heading: Optional[str] = None
    page_number: Optional[int] = None
    content_text: str
    created_at: str


class ProvenanceRecord(BaseModel):
    source_organization: str
    original_url: Optional[str] = None
    retrieval_timestamp: str
    verification_status: str = "Verified"
    checksum_sha256: Optional[str] = None
    provenance_tier: ProvenanceTier
    source_notes: Optional[str] = None


class DocumentCreate(BaseModel):
    doc_id: str
    title: str
    short_title: Optional[str] = None
    document_number: Optional[str] = None
    document_type: DocumentType
    description: Optional[str] = None
    issuing_authority: str
    jurisdiction: str
    state_code: Optional[str] = None
    district: Optional[str] = None
    publication_date: Optional[str] = None
    enactment_date: Optional[str] = None
    effective_date: Optional[str] = None
    status: str = "active"
    language: str = "en"
    source_url: Optional[str] = None
    source_name: Optional[str] = None
    source_type: Optional[str] = None
    provenance_tier: ProvenanceTier = ProvenanceTier.TIER_1_AUTHORITATIVE_GOVERNMENT
    checksum_sha256: Optional[str] = None
    topics: Optional[List[str]] = None
    chunks: Optional[List[DocumentChunkCreate]] = None


class DocumentSummaryResponse(BaseModel):
    id: str
    doc_id: str
    title: str
    short_title: Optional[str] = None
    document_number: Optional[str] = None
    document_type: str
    description: Optional[str] = None
    issuing_authority: str
    jurisdiction: str
    state_code: Optional[str] = None
    publication_date: Optional[str] = None
    status: str
    source_url: Optional[str] = None
    provenance_tier: str
    checksum_sha256: Optional[str] = None
    chunk_count: int = 0
    topics: List[str] = []
    created_at: str


class DocumentDetailResponse(DocumentSummaryResponse):
    chunks: List[DocumentChunkResponse] = []
    provenance: Optional[ProvenanceRecord] = None


class SearchResultItem(BaseModel):
    chunk_id: str
    document_id: str
    doc_id: str
    document_title: str
    document_type: str
    issuing_authority: str
    jurisdiction: str
    provenance_tier: str
    section_number: Optional[str] = None
    section_title: Optional[str] = None
    page_number: Optional[int] = None
    snippet: str
    content_text: str
    source_url: Optional[str] = None
    relevance_score: float


class SearchResponse(BaseModel):
    query: str
    total_matches: int
    results: List[SearchResultItem]
    limit: int
    offset: int

