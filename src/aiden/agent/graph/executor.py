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

            current = state.current_node
            if current is None:
                raise RuntimeError("No current node specified.")

            node = self.graph.get_node(current)
            state = await node.execute(state)

            executions += 1
            state.step += 1

            if state.finished:
                break

            next_node = await self._select_next_node(current, state)

            if next_node is None:
                break

            state.current_node = next_node

        return state

    async def _select_next_node(
        self,
        source: str,
        state: AgentState,
    ) -> str | None:
        edges = self.graph.get_edges(source)

        if not edges:
            return None

        # One unconditional edge.
        if (
            len(edges) == 1
            and edges[0].condition is None
            and edges[0].route is None
        ):
            return edges[0].target

        # Route using Qwen's structured action type.
        if all(
            edge.route is not None and edge.condition is None
            for edge in edges
        ):
            if state.action is None:
                raise RuntimeError(
                    f"Node '{source}' needs an action to route."
                )

            matches = [
                edge for edge in edges
                if edge.route == state.action.type
            ]

        # Route using a Boolean DecisionGate, such as Laya.
        elif all(
            edge.condition is not None and edge.route is None
            for edge in edges
        ):
            gate = self.graph.get_gate(source)

            if gate is None:
                raise RuntimeError(
                    f"No DecisionGate configured for '{source}'."
                )

            decision = await gate.evaluate(state)
            matches = [
                edge for edge in edges
                if edge.condition is decision
            ]

        else:
            raise RuntimeError(
                f"Invalid or mixed routing configuration at '{source}'."
            )

        if len(matches) != 1:
            raise RuntimeError(
                f"Expected exactly one matching edge at '{source}', "
                f"found {len(matches)}."
            )

        return matches[0].target