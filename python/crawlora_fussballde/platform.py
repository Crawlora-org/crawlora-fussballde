"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class FussballdeClient(CrawloraClient):
    """Synchronous Fussball.de API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-fussballde-python/0.1.0')
        super().__init__(*args, **kwargs)

    def amateur_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-amateur-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def club(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-club', params, response_type=response_type, timeout=timeout, headers=headers)

    def club_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-club-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def club_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-club-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def competition_options(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-competition-options', params, response_type=response_type, timeout=timeout, headers=headers)

    def competitions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-competitions', params, response_type=response_type, timeout=timeout, headers=headers)

    def federation(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-federation', params, response_type=response_type, timeout=timeout, headers=headers)

    def filters(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-filters', params, response_type=response_type, timeout=timeout, headers=headers)

    def match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-match', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_calendar(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-match-calendar', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_comparison(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-match-comparison', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_plan(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-match-plan', params, response_type=response_type, timeout=timeout, headers=headers)

    def matchday(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-matchday', params, response_type=response_type, timeout=timeout, headers=headers)

    def national_top_scorers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-national-top-scorers', params, response_type=response_type, timeout=timeout, headers=headers)

    def news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-news', params, response_type=response_type, timeout=timeout, headers=headers)

    def news_article(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-news-article', params, response_type=response_type, timeout=timeout, headers=headers)

    def news_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-news-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-player', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-player-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-player-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def position_history(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-position-history', params, response_type=response_type, timeout=timeout, headers=headers)

    def postal_codes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-postal-codes', params, response_type=response_type, timeout=timeout, headers=headers)

    def table(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-table', params, response_type=response_type, timeout=timeout, headers=headers)

    def team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-team', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-team-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_squad(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-team-squad', params, response_type=response_type, timeout=timeout, headers=headers)

    def top_scorers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fussballde-top-scorers', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncFussballdeClient(AsyncCrawloraClient):
    """Asynchronous Fussball.de API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-fussballde-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def amateur_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-amateur-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def club(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-club', params, response_type=response_type, timeout=timeout, headers=headers)

    async def club_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-club-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def club_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-club-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def competition_options(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-competition-options', params, response_type=response_type, timeout=timeout, headers=headers)

    async def competitions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-competitions', params, response_type=response_type, timeout=timeout, headers=headers)

    async def federation(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-federation', params, response_type=response_type, timeout=timeout, headers=headers)

    async def filters(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-filters', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-match', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_calendar(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-match-calendar', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_comparison(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-match-comparison', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_plan(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-match-plan', params, response_type=response_type, timeout=timeout, headers=headers)

    async def matchday(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-matchday', params, response_type=response_type, timeout=timeout, headers=headers)

    async def national_top_scorers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-national-top-scorers', params, response_type=response_type, timeout=timeout, headers=headers)

    async def news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-news', params, response_type=response_type, timeout=timeout, headers=headers)

    async def news_article(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-news-article', params, response_type=response_type, timeout=timeout, headers=headers)

    async def news_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-news-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-player', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-player-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-player-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def position_history(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-position-history', params, response_type=response_type, timeout=timeout, headers=headers)

    async def postal_codes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-postal-codes', params, response_type=response_type, timeout=timeout, headers=headers)

    async def table(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-table', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-team', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-team-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_squad(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-team-squad', params, response_type=response_type, timeout=timeout, headers=headers)

    async def top_scorers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fussballde-top-scorers', params, response_type=response_type, timeout=timeout, headers=headers)
