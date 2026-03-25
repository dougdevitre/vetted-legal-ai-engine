"""Detect jurisdiction from query text."""
import re

STATE_PATTERNS = {
    "MO": ["missouri", "rsmo", "mo rev stat"],
    "IL": ["illinois", "ilcs"],
    "KS": ["kansas", "ksa"],
    "CA": ["california", "cal civ"],
    "NY": ["new york", "nycl"],
    "TX": ["texas", "tex fam"],
}

class JurisdictionDetector:
    def detect(self, query: str) -> str:
        """Detect jurisdiction from query text. Returns state code or 'UNKNOWN'."""
        lower = query.lower()
        for state, patterns in STATE_PATTERNS.items():
            if any(p in lower for p in patterns):
                return state
        return "UNKNOWN"

    def get_confidence(self, query: str) -> dict:
        state = self.detect(query)
        return {"jurisdiction": state, "confidence": 0.9 if state != "UNKNOWN" else 0.0}
