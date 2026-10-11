import pytest

from aiden.agent.action import AgentAction
from aiden.agent.graph.nodes.final import finalNode
from aiden.agent.state import AgentState


@pytest.mark.asyncio
async def test_final_node():
    node = finalNode()

    state = AgentState(
        task="What is 25 * 4?",
        action=AgentAction(
            type="final",
            answer="The result is 100.",
        ),
    )

    result = await node.execute(state)

    assert result.final_answer == "The result is 100."
    assert result.finished is True
    assert result.messages[-1]["content"] == "The result is 100."