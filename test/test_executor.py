from aiden.agent.graph.edge import Edge
from aiden.agent.graph.graph import Graph
from aiden.agent.graph.node import Node
from aiden.agent.graph.executor import GraphExecutor
from aiden.agent.state import AgentState
import pytest


class DummyNode(Node):

    def __init__(self, node_name: str):
        self._name = node_name

    @property
    def name(self) -> str:
        return self._name

    async def execute(self, state: AgentState) -> AgentState:
        state.messages.append({
            "role": "system",
            "content": f"Executed {self.name}",
        })
        return state


@pytest.mark.asyncio
async def test_linear_graph():
    graph = Graph()

    graph.add_node(DummyNode("A"))
    graph.add_node(DummyNode("B"))
    graph.add_node(DummyNode("C"))

    graph.add_edge(Edge("A", "B"))
    graph.add_edge(Edge("B", "C"))

    executor = GraphExecutor(graph, start_node="A")
    state = AgentState(task="Test graph")

    result = await executor.run(state)

    assert result.step == 3
    assert result.current_node == "C"
    assert len(result.messages) == 3
    assert result.messages[-1]["content"] == "Executed C"