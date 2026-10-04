from src.aiden.models.base import ModelProvider
from src.aiden.agent.state import AgentState

class Agent:
    def __init__(self,model : ModelProvider) :
        self.model = model

    async def run(self,task: str) -> str:
        """Simple Run task;
        Will be the ReAct loop in the future
        """
        state = AgentState(task=task)

        state.messages.append({
            "role" : "user",
            "content" : task
        })

        response = await self.model.generate(state.messages)

        state.messages.append({
                    "role" : "Assistant",
                    "content" : response
                })

        state.finished = True

        return response