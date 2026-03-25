from fastapi import FastAPI
from dotenv import load_dotenv
from src.rag_pipeline import RAGPipeline
from src.citation_validator import CitationValidator
from src.confidence_scorer import ConfidenceScorer
from src.audit_logger import AuditLogger
from src.models import QueryRequest, QueryResponse

load_dotenv()
app = FastAPI(title="Vetted Legal AI Engine", version="0.1.0")
rag = RAGPipeline()
validator = CitationValidator()
scorer = ConfidenceScorer()
logger = AuditLogger()

@app.get("/health")
def health():
    return {"status": "ok", "service": "vetted-legal-ai-engine"}

@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    result = rag.query(request.question, request.jurisdiction)
    citations_valid = [validator.validate(c) for c in result.get("citations", [])]
    confidence = scorer.score(result, citations_valid)
    logger.log_query(request.question, result, confidence)
    return QueryResponse(
        answer=result["answer"],
        citations=result.get("citations", []),
        confidence_score=confidence,
        jurisdiction=request.jurisdiction,
    )

@app.post("/validate-citation")
async def validate_citation(citation: dict):
    return {"valid": validator.validate(citation.get("text", "")), "source": citation}
