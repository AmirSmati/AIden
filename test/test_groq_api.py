import os

import pytest

from aiden.models.groq import GroqProvider


@pytest.mark.asyncio
async def test_groq_provider():
    if not os.getenv("GROQ_API_KEY"):
        pytest.skip("GROQ_API_KEY is not configured")

    model = GroqProvider()
    response = await model.generate([
        {
            "role": "user",
            "content": "Say hello in one sentence.",
        }
    ])

    print("\nGroq response:", response)
    assert response.strip()