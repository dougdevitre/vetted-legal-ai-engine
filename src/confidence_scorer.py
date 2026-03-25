"""Scores confidence of AI responses based on source quality."""

class ConfidenceScorer:
    def score(self, result: dict, citations_valid: list) -> float:
        """Score 0-100 based on source match, citation validity, grounding."""
        if not result.get("context"):
            return 0.0
        source_score = min(len(result.get("context", [])) * 20, 40)
        citation_score = (sum(1 for v in citations_valid if v) / max(len(citations_valid), 1)) * 40
        grounding_score = 20 if result.get("answer") and "could not find" not in result["answer"] else 0
        return min(source_score + citation_score + grounding_score, 100.0)
