from typing import Any

from pydantic import BaseModel


class AgentAction(BaseModel):
    type: str
    tool: str | None = None
    arguments: dict[str, Any] = {}
    answer: str | None = None