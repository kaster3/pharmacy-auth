import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.api_v1.auth import router as user_auth_router
from core.settings import settings
from core.logger_setup import LoggerSetup


logger_setup = LoggerSetup()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application starts successfully!")
    yield
    logger.info("Application ends successfully!")


application = FastAPI(
    root_path="/user",
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

for router in (user_auth_router,):
    application.include_router(
        router=router,
        prefix="/user",
    )


if __name__ == "__main__":
    uvicorn.run(
        app=settings.conf.app,
        host=settings.conf.host,
        port=settings.conf.port,
        workers=settings.conf.workers,
        reload=settings.conf.reload,
    )
