import pytest

from aiden.agent.action import AgentAction
from aiden.agent.graph.nodes.tool import ToolNode
from aiden.agent.state import AgentState
from aiden.agent.tools.calculator import CalculatorTool
from aiden.agent.tools.registery import ToolRegistery


@pytest.mark.asyncio
async def test_tool_node_executes_action():
    registry = ToolRegistery()
    registry.register(CalculatorTool())

    node = ToolNode(tool_registry=registry)

    state = AgentState(
        task="Calculate 25 * 4",
        action=AgentAction(
            type="tool",
            tool="Calculator",
            arguments={"expression": "25 * 4"},
        ),
    )

    result = await node.execute(state)

    assert result.observation == 100
    assert result.messages[-1]["role"] == "tool"
    assert "100" in result.messages[-1]["content"]