"""
BHUMI-NITI: Section-Aware Legal & Policy Chunker
Preserves legislative hierarchy (Chapter, Section, Rule, Article) for precise statutory citation.
"""

import re
from typing import List, Optional, Dict, Any
from app.repository.models import DocumentChunkCreate


SECTION_REGEX = re.compile(
    r"(?m)^(?:\s*(?:§|Section|SECTION|Sec\.|Rule|RULE|Article|ARTICLE)\s*(\d+[A-Za-z]?(?:\s*\([0-9a-z]+\))*)[.\-:\s]*(.*?))(?:\n|$)"
)

CHAPTER_REGEX = re.compile(
    r"(?m)^(?:\s*(?:CHAPTER|Chapter|PART|Part)\s*([IVXLCDM\d]+)[.\-:\s]*(.*?))(?:\n|$)"
)


def normalize_text(text: str) -> str:
    """Normalize text for consistent indexing and comparison."""
    if not text:
        return ""
    cleaned = re.sub(r"\s+", " ", text).strip()
    return cleaned.lower()


def chunk_statutory_text(
    full_text: str,
    default_section_prefix: str = "Section",
    max_chunk_chars: int = 1800
) -> List[DocumentChunkCreate]:
    """
    Parses statutory text into section-aware chunks.
    Detects section boundaries, titles, and chapters.
    """
    if not full_text or not full_text.strip():
        return []

    lines = full_text.split("\n")
    chunks: List[DocumentChunkCreate] = []

    current_chapter: Optional[str] = None
    current_section_num: Optional[str] = None
    current_section_title: Optional[str] = None
    current_content_lines: List[str] = []
    chunk_counter = 0

    def _flush_current_chunk():
        nonlocal chunk_counter, current_content_lines
        if not current_content_lines:
            return
        content = "\n".join(current_content_lines).strip()
        if not content:
            current_content_lines = []
            return

        # If content exceeds max_chunk_chars, break by paragraphs
        if len(content) > max_chunk_chars:
            paras = content.split("\n\n")
            sub_buf = []
            sub_len = 0
            for p in paras:
                p_str = p.strip()
                if not p_str:
                    continue
                if sub_len + len(p_str) > max_chunk_chars and sub_buf:
                    sub_text = "\n\n".join(sub_buf).strip()
                    chunks.append(DocumentChunkCreate(
                        chunk_index=chunk_counter,
                        section_number=current_section_num,
                        section_title=current_section_title,
                        heading=current_chapter,
                        content_text=sub_text,
                        normalized_text=normalize_text(sub_text)
                    ))
                    chunk_counter += 1
                    sub_buf = [p_str]
                    sub_len = len(p_str)
                else:
                    sub_buf.append(p_str)
                    sub_len += len(p_str)
            if sub_buf:
                sub_text = "\n\n".join(sub_buf).strip()
                chunks.append(DocumentChunkCreate(
                    chunk_index=chunk_counter,
                    section_number=current_section_num,
                    section_title=current_section_title,
                    heading=current_chapter,
                    content_text=sub_text,
                    normalized_text=normalize_text(sub_text)
                ))
                chunk_counter += 1
        else:
            chunks.append(DocumentChunkCreate(
                chunk_index=chunk_counter,
                section_number=current_section_num,
                section_title=current_section_title,
                heading=current_chapter,
                content_text=content,
                normalized_text=normalize_text(content)
            ))
            chunk_counter += 1

        current_content_lines = []

    for line in lines:
        chap_match = CHAPTER_REGEX.match(line)
        if chap_match:
            _flush_current_chunk()
            chap_num = chap_match.group(1).strip()
            chap_title = (chap_match.group(2) or "").strip()
            current_chapter = f"Chapter {chap_num}" + (f": {chap_title}" if chap_title else "")
            current_content_lines.append(line)
            continue

        sec_match = SECTION_REGEX.match(line)
        if sec_match:
            _flush_current_chunk()
            current_section_num = sec_match.group(1).strip()
            current_section_title = (sec_match.group(2) or "").strip()
            current_content_lines.append(line)
            continue

        current_content_lines.append(line)

    _flush_current_chunk()

    # Fallback if no sections were matched (e.g. general narrative document)
    if not chunks and full_text.strip():
        paragraphs = [p.strip() for p in full_text.split("\n\n") if p.strip()]
        idx = 0
        buf = []
        buf_len = 0
        for p in paragraphs:
            if buf_len + len(p) > max_chunk_chars and buf:
                c_text = "\n\n".join(buf).strip()
                chunks.append(DocumentChunkCreate(
                    chunk_index=idx,
                    section_number=None,
                    section_title=None,
                    heading=None,
                    content_text=c_text,
                    normalized_text=normalize_text(c_text)
                ))
                idx += 1
                buf = [p]
                buf_len = len(p)
            else:
                buf.append(p)
                buf_len += len(p)
        if buf:
            c_text = "\n\n".join(buf).strip()
            chunks.append(DocumentChunkCreate(
                chunk_index=idx,
                section_number=None,
                section_title=None,
                heading=None,
                content_text=c_text,
                normalized_text=normalize_text(c_text)
            ))

    return chunks

