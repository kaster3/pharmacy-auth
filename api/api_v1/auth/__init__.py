from fastapi import (
    APIRouter,
    Depends,
)
from fastapi.security import HTTPBearer
from core import settings
from .auth import router as auth_router
from .users import router as users_router

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix=settings.api.v1.prefix,
    dependencies=[Depends(http_bearer)],
)

for part in (auth_router, users_router):
    router.include_router(
        router=part,
    )
