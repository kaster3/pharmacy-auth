from fastapi_users.authentication import JWTStrategy

from core import settings


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.jwt_token.private_key.read_text(),
        lifetime_seconds=settings.jwt_token.lifetime_seconds,
        algorithm="RS256",
        public_key=settings.jwt_token.public_key.read_text(),
    )
