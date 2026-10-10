import pytest

from aiden.agent.graph.nodes.reason import ReasonNode
from aiden.agent.state import AgentState
from aiden.models.base import ModelProvider


class FakeModel(ModelProvider):

    async def generate(self, messages, **kwargs) -> str:
        return "The answer is 100."


@pytest.mark.asyncio
async def test_reason_node():
    node = ReasonNode(model=FakeModel())
    state = AgentState(task="What is 25 * 4?")

    result = await node.execute(state)

    assert result.messages[0]["content"] == "What is 25 * 4?"
    assert result.messages[-1]["content"] == "The answer is 100."
    assert node.name == "reason"