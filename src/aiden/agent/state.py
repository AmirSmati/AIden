from dataclasses import dataclass, field

@dataclass
class AgentState : 
    task : str
    messages : list[dict[str,str]] = field(default_factory=list)
    step : int = 0
    finished : bool = False