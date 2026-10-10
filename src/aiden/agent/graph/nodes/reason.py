from aiden.agent.action import AgentAction
from aiden.agent.graph.node import Node
from aiden.agent.state import AgentState
from aiden.models.base import ModelProvider


class ReasonNode(Node):

    def __init__(self, model: ModelProvider):
        self.model = model

    @property
    def name(self) -> str:
        return "reason"

    async def execute(self, state: AgentState) -> AgentState:
        system_prompt = """
            You are the action-selection component of AIden.

            Choose one action:
            - "tool": call an available tool.
            - "final": provide the final answer.

            The available tool is "calculator", which accepts an
            "expression" argument containing a mathematical expression.

            For calculations, prefer the calculator.
            For other tasks you can answer directly, use "final".

            Return only a JSON object matching the requested schema.
            Do not include Markdown fences or additional text.
            """

        if not any(m["role"] == "system" for m in state.messages):
            state.messages.insert(0, {
                "role": "system",
                "content": system_prompt,
            })

        if not any(m["role"] == "user" for m in state.messages):
            state.messages.append({
                "role": "user",
                "content": state.task,
            })

        response = await self.model.generate(
            state.messages,
            format=AgentAction.model_json_schema(),
        )

        action = AgentAction.model_validate_json(response)

        state.action = action

        state.messages.append({
            "role": "assistant",
            "content": action.model_dump_json(),
        })

        return state