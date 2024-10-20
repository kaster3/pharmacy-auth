from fastapi_users import FastAPIUsers

from core import User
from core.my_types.user_id import UserIdType
from .user_manager import get_user_manager
from .backend import authentication_backend

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)

current_active_user = fastapi_users.current_user(
    active=True,
    verified=True,
)

current_active_superuser = fastapi_users.current_user(
    active=True,
    superuser=True,
    verified=True,
)
