from core.authentication.mail_manager import MailClient
from core.settings import settings


def get_email_client():
    return MailClient(settings=settings)
