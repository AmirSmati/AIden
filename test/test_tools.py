import pytest

from aiden.agent.tools.calculator import CalculatorTool
from aiden.agent.tools.registery import ToolRegistery


@pytest.mark.asyncio
async def test_calculator_tool():

    calculator = CalculatorTool()

    registry = ToolRegistery()
    registry.register(calculator)

    result = await registry.execute(
        "Calculator",
        expression="25 * 4",
    )

    print("\nCalculator result:", result)

    assert result == 100