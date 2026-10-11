import asyncio

from aiden.agent.agent import Agent
from aiden.models.ollama import OllamaProvider

import os

from dotenv import load_dotenv
from aiden.models.groq import GroqProvider
from aiden.net import has_internet
load_dotenv()


def create_model():

    net=has_internet()

    if net == False:
        provider = os.getenv("AIDEN_PROVIDER", "ollama").lower()
        print("Working with on-prem Model : qwen3:8b")
        return OllamaProvider(model="qwen3:8b")

    if net == True:
        print(f"Working with {GroqProvider().model}")
        return GroqProvider()

    raise ValueError(f"Unknown model provider")


async def main():
    model = create_model()
    model = OllamaProvider(model="qwen3:8b")
    agent = Agent(model=model)

    print("AIden is ready! Type 'exit' to quit.\n")

    while True:
        task = input("You: ").strip()

        if task.lower() in {"exit", "quit"}:
            print("AIden: Goodbye!")
            break

        if not task:
            continue

        try:
            answer = await agent.run(task)
            print(f"AIden: {answer}\n")
        except Exception as exc:
            print(f"AIden encountered an error: {exc}\n")


if __name__ == "__main__":
    asyncio.run(main())