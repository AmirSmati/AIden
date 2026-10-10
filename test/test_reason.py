import pytest

from aiden.agent.graph.nodes.reason import ReasonNode
from aiden.agent.state import AgentState
from aiden.models.ollama import OllamaProvider


@pytest.mark.asyncio
async def test_qwen_generates_tool_action():
    model = OllamaProvider(model="qwen3:8b")
    node = ReasonNode(model=model)

    state = AgentState(
        task="Calculate 25 multiplied by 4. Use the calculator tool."
    )

    result = await node.execute(state)

    print("\nGenerated action:", result.action)

    assert result.action is not None
    assert result.action.type == "tool"
    assert result.action.tool == "calculator"
    assert result.action.arguments["expression"]