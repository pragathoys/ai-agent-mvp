from fastapi import APIRouter, HTTPException
from app.schemas.agent import AgentRequest, AgentResponse
from app.services.agent_service import run_agent
from app.services.logging_service import get_recent_runs

router = APIRouter()


@router.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }


@router.post("/agent/run", response_model=AgentResponse)
async def agent_run(payload: AgentRequest):
    """
    Main AI agent endpoint.
    Accepts user input and returns LLM-generated response.
    """

    try:
        result = await run_agent(payload.message)

        return AgentResponse(
            success=True,
            response=result
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/admin/runs")
async def admin_runs(limit: int = 20):
    """
    Returns recent agent executions.
    """

    try:
        runs = await get_recent_runs(limit)

        return {
            "success": True,
            "count": len(runs),
            "runs": runs
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/admin/runs/{run_id}")
async def admin_run_details(run_id: int):
    """
    Returns details for a specific agent execution.
    """

    try:
        from app.services.logging_service import get_run_by_id

        run = await get_run_by_id(run_id)

        if not run:
            raise HTTPException(
                status_code=404,
                detail="Run not found"
            )

        return {
            "success": True,
            "run": run
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )