import pytest

from aiden.agent.agent import Agent
from aiden.agent.state import AgentState
from aiden.models.ollama import OllamaProvider


@pytest.mark.asyncio
async def test_real_qwen_runs_full_tool_cycle():
    model = OllamaProvider(model="qwen3:8b")
    agent = Agent(model=model)

    state = AgentState(
        task=(
            "Use the calculator tool exactly once to calculate 25 * 4. "
            "After receiving the result, return a concise final answer. "
            "Do not call the calculator again."
        )
    )

    result = await agent.executor.run(state)

    print("\nFinal answer:", result.final_answer)
    print("Tool observation:", result.observation)
    print("Steps executed:", result.step)

    # The graph completed successfully.
    assert result.finished is True

    # The real calculator was executed.
    assert result.observation == 100

    # Qwen eventually selected a final answer.
    assert result.action is not None
    assert result.action.type == "final"
    assert result.final_answer is not None
    assert "100" in result.final_answer

    # The tool result was added to the conversation.
    assert any(
        message["role"] == "tool"
        and "100" in message["content"]
        for message in result.messages
    )