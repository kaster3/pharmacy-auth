from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper, AccessToken


async def get_access_token_db(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    yield AccessToken.get_db(session=session)
