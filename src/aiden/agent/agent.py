from aiden.agent.graph.edge import Edge
from aiden.agent.graph.graph import Graph
from aiden.agent.graph.executor import GraphExecutor
from aiden.agent.graph.nodes.reason import ReasonNode
from aiden.agent.graph.nodes.tool import ToolNode
from aiden.agent.graph.nodes.final import finalNode
from aiden.agent.state import AgentState
from aiden.models.base import ModelProvider
from aiden.agent.tools.registery import ToolRegistery
from aiden.agent.tools.calculator import CalculatorTool


class Agent:

    def __init__(
        self,
        model: ModelProvider,
        tool_registry: ToolRegistery | None = None,
        max_steps: int = 25,
    ):
        self.model = model

        if tool_registry is None:
            tool_registry = ToolRegistery()
            tool_registry.register(CalculatorTool())

        self.tool_registry = tool_registry

        # Build the default V1 graph.
        self.graph = Graph()
        self.graph.add_node(ReasonNode(model))
        self.graph.add_node(ToolNode(tool_registry))
        self.graph.add_node(finalNode())

        self.graph.add_edge(
            Edge("reason", "tool", route="tool")
        )
        self.graph.add_edge(
            Edge("reason", "final", route="final")
        )
        self.graph.add_edge(
            Edge("tool", "reason")
        )

        self.executor = GraphExecutor(
            graph=self.graph,
            start_node="reason",
            max_steps=max_steps,
        )

    async def run(self, task: str) -> str:
        state = AgentState(task=task)
        result = await self.executor.run(state)

        if result.final_answer is None:
            raise RuntimeError("Agent finished without a final answer.")

        return result.final_answer