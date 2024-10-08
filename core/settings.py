from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    auth: str = "/auth"
    users: str = "/user"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()

    @property
    def bearer_token_url(self) -> str:
        parts = (self.prefix, self.v1.prefix, self.v1.auth, "/login")
        path = "".join(parts)
        return path[1:]


class AccessToken(BaseModel):
    lifetime_seconds: int
    reset_password_token_secret: str
    verification_token_secret: str


class LoggingConfig(BaseModel):
    format: str


class DataBase(BaseModel):
    url: PostgresDsn
    echo: bool
    echo_pool: bool
    pool_size: int
    max_overflow: int

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class LaunchConfig(BaseModel):
    app: str
    host: str
    port: int
    reload: bool
    workers: int


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FASTAPI__"
    )
    conf: LaunchConfig
    db: DataBase
    log: LoggingConfig
    access_token: AccessToken
    api: ApiPrefix = ApiPrefix()


def get_settings() -> Settings:
    return Settings()


settings = get_settings()




