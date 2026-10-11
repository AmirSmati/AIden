import asyncio

from aiden.agent.agent import Agent
from aiden.models.ollama import OllamaProvider


async def main():
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