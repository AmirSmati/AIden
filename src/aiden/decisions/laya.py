from typing import Any

import laya

from .base import DecisionProvider
from .result import DecisionResult

class LayaDecisionProvider(DecisionProvider):

    def __init__(self, model_id: str = "convaiinnovations/laya"):
        self.agent = laya.load(model_id)

    async def decide(
        self,
        question: str,
        context: str | None = None,
        **kwargs: Any,
    ) -> Any:

        state = {
            "context": context or ""
        }

        questions = {
            "decision": {
                "type": "noul",
                "instructions": question,
            }
        }

        result = self.agent.predict(
            state,
            questions,
        )

        decision = result["answers"]["decision"]

        return DecisionResult(
            type=decision["type"],
            score=decision["noul"],
            confidence=decision["confidence"],
            answer_confidence=decision["answer_confidence"],
            act_probability=decision["action"]["act_probability"]
        )