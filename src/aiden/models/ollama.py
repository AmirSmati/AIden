from typing import Any

from ollama import AsyncClient

from src.aiden.models.base import ModelProvider

class OllamaProvider(ModelProvider):
    def __init__(
        self,
        model: str,
        host: str = "http://localhost:11434",
    ):
        self.model = model
        self.client = AsyncClient(host=host)

    async def generate(
        self,
        messages: list[dict[str, str]],
        **kwargs: Any,
    ) -> str:

        response = await self.client.chat(
            model=self.model,
            messages=messages,
            **kwargs,
        )

        return response["message"]["content"]