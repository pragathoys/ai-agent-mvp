from fastapi import FastAPI
from app.api.routes import router
from app.schemas.agent import AgentRequest, AgentResponse

app = FastAPI(title="AI Agent MVP")

app.include_router(router)


