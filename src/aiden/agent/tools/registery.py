from .base import Tool

class ToolRegistery : 

    def __init__(self) -> None:
        self._tools : dict[str, Tool] = {}

    def register(self, tool : Tool) -> None : 
        self._tools[tool.name] = tool

    def get(self, name : str) -> Tool :
        if name not in self._tools : 
            raise KeyError(f"Tool not found: {name}")
        
        return self._tools[name]

    def list(self) -> list[Tool] : 
        return list(self._tools.values())

    async def execute(self, name : str, **kwargs) :
        tool = self.get(name)
        return await tool.execute(**kwargs)