from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class QueryRequest(BaseModel):
    question: str
    jurisdiction: Optional[str] = None
    max_results: int = 5

class Citation(BaseModel):
    text: str
    source: str
    statute: Optional[str] = None
    valid: bool = False

class QueryResponse(BaseModel):
    answer: str
    citations: List[dict] = []
    confidence_score: float = 0.0
    jurisdiction: Optional[str] = None

class AuditEntry(BaseModel):
    timestamp: datetime
    query: str
    response_summary: str
    confidence: float
    citations_count: int

class ConfidenceReport(BaseModel):
    overall_score: float
    source_match: float
    citation_validity: float
    jurisdiction_match: float
