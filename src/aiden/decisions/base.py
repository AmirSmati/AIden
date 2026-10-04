from abc import abstractmethod, ABC
from typing import Any

class DecisionProvider(ABC):

    @abstractmethod
    async def decide (self,question : str, context : str | None= None , **kwargs : Any) -> Any :
        """Makes a decision based on question and context"""

        raise NotImplementedError