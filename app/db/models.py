from sqlalchemy import Column, Integer, String, Text, DateTime, func
from app.db.database import Base


class AgentRun(Base):
    """
    Stores every AI agent execution.
    """

    __tablename__ = "agent_runs"

    id = Column(Integer, primary_key=True, index=True)

    request_text = Column(Text, nullable=False)
    response_text = Column(Text, nullable=True)

    status = Column(String(20), nullable=False)  # success | error

    error_message = Column(Text, nullable=True)

    duration_ms = Column(Integer, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )