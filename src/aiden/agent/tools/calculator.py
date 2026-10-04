from .base import Tool
from typing import Any
from simpleeval import simple_eval
class CalculatorTool(Tool):

    @property
    def name(self) -> str :
        return "Calculator"

    @property
    def desc(self) -> Any :
        return "Perform mathematical calculations."

    async def execute(self, **kwargs : Any) -> Any :
        expression = kwargs["expression"]

        return simple_eval(expression)