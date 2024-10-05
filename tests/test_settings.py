import re

from fast_depends import Depends, inject
from pydantic_core import MultiHostUrl

from core.settings import get_settings, Settings


@inject
def test_settings(settings: Settings = Depends(get_settings)):

    assert isinstance(settings, Settings)
    assert isinstance(settings.conf.app, str)
    assert isinstance(settings.conf.host, str)
    assert isinstance(settings.conf.port, int)
    assert isinstance(settings.conf.reload, bool)
    assert isinstance(settings.conf.workers, int)

    assert isinstance(settings.db.url, MultiHostUrl)
    assert isinstance(settings.db.echo, bool)
    assert isinstance(settings.db.echo_pool, bool)
    assert isinstance(settings.db.pool_size, int)
    assert isinstance(settings.db.max_overflow, int)

    assert settings.conf.app == "main:application"
    assert settings.conf.host == "0.0.0.0"
    assert settings.conf.port in (8000, 8001)

    assert re.fullmatch(r'^postgresql\+asyncpg://[^:@]+:[^@]+@[^:]+:\d+/[^/]+$', str(settings.db.url))

