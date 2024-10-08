from fastapi import APIRouter

from core import settings
from api.dependencies.authentication.my_fastapi_users import fastapi_users
from core.database.dto.user import UserCreate, UserRead

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users"],
)

# /me
# /{id}
router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserCreate,
        # requires_verification=True,
    ),
)
