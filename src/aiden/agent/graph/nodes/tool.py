from aiden.agent.graph.node import Node
from aiden.agent.state import AgentState
from aiden.agent.tools.registery import ToolRegistery

class Tool(Node) : 
    def __init__(self, tool_registry: ToolRegistery):
        self.tool_registry = tool_registry

    @property
    def name(self) -> str :
        return "tool"

    async def execute (self, state : AgentState) -> AgentState : 
        action = state.action

        if action is None or action.type != "tool":
            raise ValueError("ToolNode requires a tool action.")

        if not action.tool:
            raise ValueError("Tool action must specify a tool name.")

        result = await self.tool_registry.execute(
            action.tool,
            **action.arguments
        )

        # Save the latest result.
        state.observation = result

        # Make the result available to the next reasoning step.
        state.messages.append({
            "role": "tool",
            "content": f"Tool '{action.tool}' returned: {result}",
        })

        return state