import pytest

from aiden.agent.graph.edge import Edge
from aiden.agent.graph.graph import Graph
from aiden.agent.graph.node import Node
from aiden.agent.graph.executor import GraphExecutor
from aiden.agent.state import AgentState


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


class StubGate:
    """Fake gate for testing routing without calling Laya."""

    def __init__(self, decision: bool):
        self.decision = decision

    async def evaluate(self, state: AgentState) -> bool:
        return self.decision


@pytest.mark.asyncio
async def test_routes_to_calculator_when_positive():
    graph = Graph()

    graph.add_node(DummyNode("reason"))
    graph.add_node(DummyNode("calculator"))
    graph.add_node(DummyNode("final"))

    graph.add_edge(Edge("reason", "calculator", condition=True))
    graph.add_edge(Edge("reason", "final", condition=False))

    graph.add_gate("reason", StubGate(decision=True))

    executor = GraphExecutor(graph, start_node="reason")
    result = await executor.run(AgentState(task="Calculate 25 * 4"))

    assert result.current_node == "calculator"
    assert result.step == 2


@pytest.mark.asyncio
async def test_routes_to_final_when_negative():
    graph = Graph()

    graph.add_node(DummyNode("reason"))
    graph.add_node(DummyNode("calculator"))
    graph.add_node(DummyNode("final"))

    graph.add_edge(Edge("reason", "calculator", condition=True))
    graph.add_edge(Edge("reason", "final", condition=False))

    graph.add_gate("reason", StubGate(decision=False))

    executor = GraphExecutor(graph, start_node="reason")
    result = await executor.run(AgentState(task="Hello"))

    assert result.current_node == "final"
    assert result.step == 2