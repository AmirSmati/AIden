
from aiden.agent.graph.graph import Graph
from aiden.agent.state import AgentState


class GraphExecutor:

    def __init__(
        self,
        graph: Graph,
        start_node: str,
        max_steps: int = 25,
    ):
        self.graph = graph
        self.start_node = start_node
        self.max_steps = max_steps

    async def run(self, state: AgentState) -> AgentState:
        state.current_node = self.start_node
        executions = 0

        while True:
            if state.finished:
                break

            if executions >= self.max_steps:
                raise RuntimeError("Maximum graph steps exceeded.")

            node = self.graph.get_node(state.current_node)
            state = await node.execute(state)

            executions += 1
            state.step += 1

            if state.finished:
                break

            edges = self.graph.get_edges(state.current_node)

            # No outgoing edges: terminal node
            if not edges:
                break

            # Branching will be implemented later
            if len(edges) > 1:
                raise NotImplementedError(
                    "Conditional routing is not implemented yet."
                )

            state.current_node = edges[0].target

        return state
