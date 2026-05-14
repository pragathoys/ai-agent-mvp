from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class AgentRequest(BaseModel):
    """
    Request payload for AI agent execution.
    """

    message: str = Field(
        ...,
        min_length=1,
        max_length=10000,
        description="User input message"
    )

    session_id: Optional[str] = Field(
        default=None,
        description="Optional session identifier"
    )

    user_id: Optional[str] = Field(
        default=None,
        description="Optional user identifier"
    )


class AgentResponse(BaseModel):
    """
    Response payload returned by AI agent.
    """

    success: bool
    response: str

    timestamp: datetime = Field(
        default_factory=datetime.utcnow
    )


class ErrorResponse(BaseModel):
    """
    Standard API error response.
    """

    success: bool = False
    error: str
    detail: Optional[str] = None


class AgentRunLog(BaseModel):
    """
    Admin/debug representation of stored agent runs.
    """

    id: int

    request_text: str
    response_text: Optional[str]

    status: str
    error_message: Optional[str]

    created_at: datetime

    duration_ms: Optional[int]

    class Config:
        from_attributes = True