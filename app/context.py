import typing as tp
from app.utils import secrets


class AppContext:

    def __init__(self, *, secrets_dir: str):
        self.secrets: secrets.SecretsReader = secrets.SecretsReader(secrets_dir)

    async def on_startup(self, app=None):
        pass

    async def on_shutdown(self, app=None):
        pass