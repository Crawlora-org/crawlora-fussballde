"""Typed Fussball.de client for the Crawlora hosted API."""

from .platform import FussballdeClient, AsyncFussballdeClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = FussballdeClient
AsyncClient = AsyncFussballdeClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Fussball.de'
PLATFORM = 'fussballde'
CONTRACT_REVISION = 'sha256:c0a322b3f5d6832b349dd86359e8c7e3cb9ba91c30cab51a67acc9a0fe3960a1'

__all__ = [
    "FussballdeClient", "AsyncFussballdeClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
