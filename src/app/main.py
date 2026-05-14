from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Agent MVP")

app.include_router(router)


@router.post("/agent/run")
async def run_agent(payload: AgentRequest):
    result = await agent_service.run(payload.message)
    return result