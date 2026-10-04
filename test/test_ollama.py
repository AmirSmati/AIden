import pytest

from aiden.models.ollama import OllamaProvider


@pytest.mark.asyncio
async def test_ollama_provider():
    model = OllamaProvider(model="qwen3:8b")

    messages = [
        {
            "role": "user",
            "content": "Say hello in one sentence.",
        }
    ]

    response = await model.generate(messages)

    print(response)

    assert response