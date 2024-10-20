import os
import logging
from typing import Optional

from fastapi import Response, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, models

from core import User

from core import settings
from core.my_types.user_id import UserIdType
from core.authentication.mail_manager import MailClient
from api.dependencies.authentication.mail_manager import get_email_client


log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[User, UserIdType]):
    reset_password_token_secret = (
        settings.verification_token.reset_password_token_secret
    )
    verification_token_secret = settings.verification_token.verification_token_secret

    async def on_after_register(
        self,
        user: User,
        request: Optional[Request] = None,
    ):
        log.warning(
            "User %r has registered.",
            user.id,
        )

    async def on_after_request_verify(
        self,
        user: User,
        token: str,
        request: Optional[Request] = None,
    ):
        log.warning(
            "Verification requested for user %r. Verification token: %r",
            user.id,
            token,
        )
        mail_client: MailClient = get_email_client()

        await mail_client.send_email_task(
            to=user.email,
            subject="Link to verification",
            text=f"http://127.0.0.1:8000/verify?token={token}",
        )

    async def on_after_verify(
        self, user: models.UP, request: Optional[Request] = None
    ) -> None:
        log.warning(
            "User %r has been verified.",
            user.id,
        )

    async def on_after_forgot_password(
        self,
        user: User,
        token: str,
        request: Optional[Request] = None,
    ):
        log.warning(
            "User %r has forgot their password. Reset token: %r",
            user.id,
            token,
        )

    async def on_after_login(
        self,
        user: User,
        request: Optional[Request] = None,
        response: Optional[Response] = None,
    ):
        log.warning(
            f"User %r has logged in. {os.getpid()}",
            user.id,
        )

        mail_client: MailClient = get_email_client()
        await mail_client.send_email_task(
            to=user.email,
            subject="Welcome message",
            text="Welcome to our service!",
        )
