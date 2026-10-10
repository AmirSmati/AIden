from aiden.agent.graph.node import Node
from aiden.agent.state import AgentState
from aiden.models.base import ModelProvider


class ReasonNode(Node):

    def __init__(self, model: ModelProvider):
        self.model = model

    @property
    def name(self) -> str:
        return "reason"

    async def execute(self, state: AgentState) -> AgentState:
        # Add the task to the conversation on the first execution.
        if not state.messages:
            state.messages.append({
                "role": "user",
                "content": state.task,
            })

        response = await self.model.generate(state.messages)

        state.messages.append({
            "role": "assistant",
            "content": response,
        })

        return state