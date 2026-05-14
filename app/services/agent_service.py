import time

from app.services.llm_service import LLMService
from app.services.logging_service import log_agent_run


async def run_agent(user_message: str) -> str:
    """
    Main AI agent orchestration logic.
    """

    start_time = time.time()

    try:
        response = await LLMService.generate_response(user_message)

        duration_ms = int((time.time() - start_time) * 1000)

        await log_agent_run(
            request_text=user_message,
            response_text=response,
            status="success",
            duration_ms=duration_ms
        )

        return response

    except Exception as e:

        duration_ms = int((time.time() - start_time) * 1000)

        await log_agent_run(
            request_text=user_message,
            response_text=None,
            status="error",
            error_message=str(e),
            duration_ms=duration_ms
        )

        raise e