import os
import ssl
import logging
from typing import TYPE_CHECKING
from email.message import EmailMessage

import aiosmtplib
from aiosmtplib.errors import SMTPConnectError

from core.settings import Settings

if TYPE_CHECKING:
    from core.settings import Settings


class MailClient:
    def __init__(self, settings: "Settings"):
        self.settings = settings
        self.log = logging.getLogger(__name__)

    async def send_email_task(self, subject: str, text: str, to: str) -> None:
        message = self._build_message(subject, text, to)
        try:
            await self._send_message(message=message)
        except SMTPConnectError as e:
            self.log.error(
                f"Failed to send email to {message['To']}: {str(e)} {os.getpid()}"
            )
        else:
            self.log.info(f"Email sent to {message['To']} successfully! {os.getpid()}")

    def _build_message(self, subject: str, text: str, to: str) -> EmailMessage:
        message = EmailMessage()
        message["From"] = self.settings.email.from_email
        message["To"] = to
        message["Subject"] = subject
        message.set_content(text)
        return message

    async def _send_message(self, message: EmailMessage) -> None:
        context = ssl.create_default_context()
        await aiosmtplib.send(
            message,
            hostname=self.settings.email.smtp_server,
            port=self.settings.email.smtp_port,
            start_tls=True,
            username=self.settings.email.from_email,
            password=self.settings.email.smtp_password,
            timeout=10,
            tls_context=context,
        )
