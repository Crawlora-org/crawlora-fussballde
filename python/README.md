# crawlora-fussballde — Fussball.de API client for Python

Python client for Crawlora's hosted Fussball.de API. It exposes 27 API endpoints covering amateur football clubs, players, matches, statistics, news, and federation data. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=fussballde-python-homepage); the package does not run a browser or scrape
Fussball.de locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
Fussball.de or its owners.

## Install

```sh
python -m pip install crawlora-fussballde
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=fussballde-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=fussballde-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_fussballde import FussballdeClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with FussballdeClient(api_key=api_key) as client:
    result_1 = client.club_search(text='Bayern')
    print(result_1)
    result_2 = client.national_top_scorers()
    print(result_2)
```

The package also exports `Client` as an alias for `FussballdeClient`. Operation
methods are available directly in snake_case and through the `fussballde`
group. The async package client is `AsyncFussballdeClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-fussballde/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-fussballde/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_fussballde import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.club_search(text='Bayern')
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-fussballde/blob/main/examples/python.py) for a complete usage example.

## Supported Fussball.de API endpoints

This package exposes every route below through direct snake_case methods and the `fussballde` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-fussballde/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/fussballde/amateur-stats` | `fussballde-amateur-stats` | Get FUSSBALL.DE amateur top statistics |
| `GET` | `/fussballde/club` | `fussballde-club` | Get a FUSSBALL.DE club |
| `GET` | `/fussballde/club-matches` | `fussballde-club-matches` | Get FUSSBALL.DE fixtures and results of a club |
| `GET` | `/fussballde/club-search` | `fussballde-club-search` | Search FUSSBALL.DE clubs by name or place |
| `GET` | `/fussballde/competition-options` | `fussballde-competition-options` | List FUSSBALL.DE team types, leagues and areas |
| `GET` | `/fussballde/competitions` | `fussballde-competitions` | List FUSSBALL.DE competitions for a league and area |
| `GET` | `/fussballde/federation` | `fussballde-federation` | Get a FUSSBALL.DE federation or regional association |
| `GET` | `/fussballde/filters` | `fussballde-filters` | List FUSSBALL.DE federations, seasons and competition types |
| `GET` | `/fussballde/match` | `fussballde-match` | Get a FUSSBALL.DE match |
| `GET` | `/fussballde/match-calendar` | `fussballde-match-calendar` | Get FUSSBALL.DE matches near a postcode |
| `GET` | `/fussballde/match-comparison` | `fussballde-match-comparison` | Compare the two teams of a FUSSBALL.DE match |
| `GET` | `/fussballde/match-plan` | `fussballde-match-plan` | Get the full FUSSBALL.DE match plan of a competition |
| `GET` | `/fussballde/matchday` | `fussballde-matchday` | Get FUSSBALL.DE matches of a competition matchday |
| `GET` | `/fussballde/national-top-scorers` | `fussballde-national-top-scorers` | Get the nationwide FUSSBALL.DE top scorers by league level |
| `GET` | `/fussballde/news` | `fussballde-news` | List FUSSBALL.DE news |
| `GET` | `/fussballde/news-article` | `fussballde-news-article` | Get a FUSSBALL.DE news article |
| `GET` | `/fussballde/news-search` | `fussballde-news-search` | Search FUSSBALL.DE news |
| `GET` | `/fussballde/player` | `fussballde-player` | Get a FUSSBALL.DE player profile |
| `GET` | `/fussballde/player-matches` | `fussballde-player-matches` | Get a FUSSBALL.DE player's match-by-match record |
| `GET` | `/fussballde/player-search` | `fussballde-player-search` | Search FUSSBALL.DE players by name |
| `GET` | `/fussballde/position-history` | `fussballde-position-history` | Get the FUSSBALL.DE fever curve of a competition |
| `GET` | `/fussballde/postal-codes` | `fussballde-postal-codes` | Look up German postcodes by place name |
| `GET` | `/fussballde/table` | `fussballde-table` | Get a FUSSBALL.DE competition standings table |
| `GET` | `/fussballde/team` | `fussballde-team` | Get a FUSSBALL.DE team |
| `GET` | `/fussballde/team-matches` | `fussballde-team-matches` | Get FUSSBALL.DE fixtures and results of a team |
| `GET` | `/fussballde/team-squad` | `fussballde-team-squad` | Get a FUSSBALL.DE team squad |
| `GET` | `/fussballde/top-scorers` | `fussballde-top-scorers` | Get the FUSSBALL.DE top scorers of a competition |

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
