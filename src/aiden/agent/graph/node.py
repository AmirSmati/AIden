from abc import ABC, abstractmethod
from aiden.agent.state import AgentState

class Node(ABC):
    
    @property
    @abstractmethod
    def name(self) -> str :
        """Node Name"""
        raise NotImplementedError


    @abstractmethod
    async def execute(self, state:AgentState) -> AgentState:
        """Execution of the node against the Agent's current state"""
        raise NotImplementedError

    