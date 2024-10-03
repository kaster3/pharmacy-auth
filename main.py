from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from core.settings import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

application = FastAPI()

if __name__ == "__main__":
    settings = get_settings()
    uvicorn.run(
        app=settings.conf.app,
        host=settings.conf.host,
        port=settings.conf.port,
        workers=settings.conf.workers,
        reload=settings.conf.reload,
    )



