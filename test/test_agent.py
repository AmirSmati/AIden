import pytest

from aiden.agent.agent import Agent
from aiden.models.ollama import OllamaProvider


@pytest.mark.asyncio
async def test_agent():
    model = OllamaProvider(model="qwen3:8b")
    agent = Agent(model=model)

    response = await agent.run(
        "Explain what an AI agent is in two sentences."
    )

    print("\nAIden:", response)

    assert response