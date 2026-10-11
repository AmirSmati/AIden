from aiden.agent.graph.node import Node
from aiden.agent.state import AgentState

class finalNode(Node) :
    
    @property
    def name(self) -> str:
        return "final"

    async def execute(self, state: AgentState) -> AgentState:
        action = state.action

        if action is None or action.type != "final" :
            raise ValueError("FinalNode requires a final action.")

        if not action.answer:
            raise ValueError("Final action must contain an answer.")

        state.final_answer = action.answer
        state.messages.append({
            "role": "assistant",
            "content": action.answer,
        })
        state.finished = True

        return state