from aiden.decisions.base import DecisionProvider
from aiden.agent.state import AgentState

class DecisionGate:

    def __init__(self, question : str, dec_provider : DecisionProvider) -> None:
        self.question = question
        self.dec_provider = dec_provider

    async def evaluate(self, state: AgentState) -> str :
        result = await self.dec_provider.decide(
            self.question,   
            context=str(state)
        )
        return result.is_positive