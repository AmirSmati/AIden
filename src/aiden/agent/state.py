from dataclasses import dataclass, field

from aiden.agent.action import AgentAction

@dataclass
class AgentState : 
    task : str
    messages : list[dict[str,str]] = field(default_factory=list)
    step : int = 0
    finished : bool = False
    current_node: str | None = None
    action: AgentAction | None = None