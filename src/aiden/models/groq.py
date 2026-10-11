import json
import os
from typing import Any

from groq import AsyncGroq

from .base import ModelProvider


class GroqProvider(ModelProvider):

    def __init__(
        self,
        model: str = "qwen/qwen3.8-27b",
        api_key: str | None = None,
    ):
        api_key = api_key or os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY is not set."
            )

        self.model = model
        self.client = AsyncGroq(api_key=api_key)

    async def generate(
        self,
        messages: list[dict[str, str]],
        **kwargs: Any,
    ) -> str:

        messages = [message.copy() for message in messages]

        # Adapt Ollama-specific structured-output requests to Groq.
        schema = kwargs.pop("format", None)

        if schema is not None:
            schema_instruction = (
                "\nReturn valid JSON matching this JSON Schema:\n"
                + json.dumps(schema)
            )

            system_message = next(
                (
                    message for message in messages
                    if message["role"] == "system"
                ),
                None,
            )

            if system_message:
                system_message["content"] += schema_instruction
            else:
                messages.insert(0, {
                    "role": "system",
                    "content": schema_instruction,
                })

            kwargs.setdefault(
                "response_format",
                {"type": "json_object"},
            )

        # AIden's tool observations are not native Groq tool calls.
        # Represent them as user-visible observations instead.
        for message in messages:
            if message["role"] == "tool":
                message["role"] = "user"
                message["content"] = (
                    "Tool observation: " + message["content"]
                )

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            **kwargs,
        )

        content = response.choices[0].message.content

        if content is None:
            raise RuntimeError("Groq returned an empty response.")

        return content