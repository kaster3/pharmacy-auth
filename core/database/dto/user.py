from fastapi_users import schemas

from core.my_types import UserIdType


class UserCreate(schemas.BaseUserCreate):
    pass


class UserRead(schemas.BaseUser[UserIdType]):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
