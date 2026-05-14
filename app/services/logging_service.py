from sqlalchemy import select, desc

from app.db.database import AsyncSessionLocal
from app.db.models import AgentRun


async def log_agent_run(
    request_text: str,
    response_text: str = None,
    status: str = "success",
    error_message: str = None,
    duration_ms: int = None
):
    """
    Stores agent execution logs in PostgreSQL.
    """

    async with AsyncSessionLocal() as session:

        run = AgentRun(
            request_text=request_text,
            response_text=response_text,
            status=status,
            error_message=error_message,
            duration_ms=duration_ms
        )

        session.add(run)

        await session.commit()

        await session.refresh(run)

        return run


async def get_recent_runs(limit: int = 20):
    """
    Returns recent agent executions.
    """

    async with AsyncSessionLocal() as session:

        query = (
            select(AgentRun)
            .order_by(desc(AgentRun.created_at))
            .limit(limit)
        )

        result = await session.execute(query)

        runs = result.scalars().all()

        return [
            {
                "id": run.id,
                "request_text": run.request_text,
                "response_text": run.response_text,
                "status": run.status,
                "error_message": run.error_message,
                "created_at": run.created_at,
                "duration_ms": run.duration_ms
            }
            for run in runs
        ]


async def get_run_by_id(run_id: int):
    """
    Returns a single run by ID.
    """

    async with AsyncSessionLocal() as session:

        query = select(AgentRun).where(AgentRun.id == run_id)

        result = await session.execute(query)

        run = result.scalar_one_or_none()

        if not run:
            return None

        return {
            "id": run.id,
            "request_text": run.request_text,
            "response_text": run.response_text,
            "status": run.status,
            "error_message": run.error_message,
            "created_at": run.created_at,
            "duration_ms": run.duration_ms
        }