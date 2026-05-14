class AgentBaseError(Exception):
    """
    Base exception for all agent-related errors.
    """
    pass


class LLMError(AgentBaseError):
    """
    Raised when LLM provider fails.
    """
    pass


class DatabaseError(AgentBaseError):
    """
    Raised when DB operations fail.
    """
    pass


class ValidationError(AgentBaseError):
    """
    Raised for invalid input or schema issues.
    """
    pass