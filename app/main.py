from fastapi import FastAPI
from app.api.routes import router
from app.db.database import init_db


app = FastAPI(title="AI Agent MVP")

app.include_router(router)


@app.on_event("startup")
async def startup():
    await init_db()