"""Append-only audit logging for all AI interactions."""
from datetime import datetime

class AuditLogger:
    def __init__(self):
        self._log = []

    def log_query(self, query: str, response: dict, confidence: float):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "query": query,
            "response_summary": response.get("answer", "")[:200],
            "confidence": confidence,
            "citations_count": len(response.get("citations", [])),
        }
        self._log.append(entry)

    def log_response(self, query_id: str, response: dict):
        self._log.append({"timestamp": datetime.utcnow().isoformat(), "query_id": query_id, **response})

    def get_audit_trail(self, limit: int = 100) -> list:
        return self._log[-limit:]
