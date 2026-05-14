import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://agent:password@postgres:5432/agent_db"
)

# Async SQLAlchemy engine
engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True
)

# Async session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base model for all ORM models
Base = declarative_base()


async def init_db():
    """
    Creates database tables on startup (MVP-friendly).
    In production, replace with Alembic migrations.
    """

    import app.db.models  # noqa: F401 (ensures models are registered)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)