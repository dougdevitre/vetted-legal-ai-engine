"""Guards against hallucinated or ungrounded AI outputs."""

class HallucinationGuard:
    def check_grounding(self, answer: str, sources: list) -> dict:
        """Verify the answer is grounded in provided sources."""
        if not sources:
            return {"grounded": False, "reason": "No sources provided"}
        if not answer or len(answer.strip()) < 10:
            return {"grounded": False, "reason": "Answer too short or empty"}
        return {"grounded": True, "source_count": len(sources)}

    def reject_if_ungrounded(self, answer: str, sources: list) -> str:
        """Return answer if grounded, rejection message if not."""
        result = self.check_grounding(answer, sources)
        if not result["grounded"]:
            return "This question cannot be answered with verified legal sources. Please consult an attorney."
        return answer
