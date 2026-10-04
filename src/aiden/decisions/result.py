from pydantic import BaseModel

class DecisionResult(BaseModel) :
    """The goal here is to access the result as if it had getters decisio.Something"""
    type : str
    score : float
    confidence : float
    answer_confidence : float
    act_probability : float

    @property
    def is_positive(self) -> bool:
        return self.score >= 0.5