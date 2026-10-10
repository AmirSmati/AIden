from typing import Any

from pydantic import BaseModel, Field


class AgentAction(BaseModel):
    type: str
    tool: str | None = None
    arguments: dict[str, Any] = Field(default_factory=dict)
    answer: str | None = None