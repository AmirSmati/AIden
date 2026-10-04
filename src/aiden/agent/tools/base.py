from abc import abstractmethod, ABC
from typing import Any

class Tool(ABC) : 

    @property
    @abstractmethod
    def name(self) -> str :
        """Name of the func"""
        raise NotImplementedError

    @property
    @abstractmethod
    def desc(self) -> str :
        """func desc"""
        raise NotImplementedError

    @abstractmethod
    def execute(self, **kwargs: Any) -> Any : 
        """Execution for any fucntion (MCP, Local, Etc..)"""
        raise NotImplementedError