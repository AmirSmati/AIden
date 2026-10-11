import pytest

from aiden.agent.agent import Agent
from aiden.models.base import ModelProvider


class SequenceModel(ModelProvider):

    def __init__(self, responses: list[str]):
        self.responses = responses
        self.calls = 0

    async def generate(self, messages, **kwargs) -> str:
        self.calls += 1
        return self.responses.pop(0)


@pytest.mark.asyncio
async def test_agent_runs_tool_then_returns_final_answer():
    model = SequenceModel([
        (
            '{"type":"tool","tool":"Calculator",'
            '"arguments":{"expression":"25 * 4"},'
            '"answer":null}'
        ),
        (
            '{"type":"final","tool":null,'
            '"arguments":{},'
            '"answer":"The result is 100."}'
        ),
    ])

    agent = Agent(model=model)
    answer = await agent.run("Calculate 25 * 4")

    assert answer == "The result is 100."
    assert model.calls == 2