import pytest

from aiden.agent.graph.node import Node
from aiden.agent.state import AgentState


class TestNode(Node):

    @property
    def name(self) -> str:
        return "test"

    async def execute(self, state: AgentState) -> AgentState:
        state.step += 1
        return state


@pytest.mark.asyncio
async def test_node():

    node = TestNode()
    state = AgentState(task="Test task")

    result = await node.execute(state)

    assert result.step == 1