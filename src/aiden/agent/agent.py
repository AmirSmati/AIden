from src.aiden.models.base import ModelProvider

class Agent:
    def __init__(self,model : ModelProvider) :
        self.model = model

    async def run(self,task: str) -> str:
        """Simple Run task;
        Will be the ReAct loop in the future
        """
        messages = [
            {
                "role" : "user",
                "content" :task
            }
        ]
        return await self.model.generate(messages)