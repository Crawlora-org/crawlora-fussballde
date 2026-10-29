# @crawlora-org/fussballde — Fussball.de API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted Fussball.de API.
It exposes 27 API endpoints for amateur football clubs, players, matches, statistics, news, and federation data through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=fussballde-javascript-homepage). It does not run a browser or scrape Fussball.de locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Fussball.de or its owners.

## Install

```sh
npm install @crawlora-org/fussballde
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=fussballde-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=fussballde-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { FussballdeClient } from "@crawlora-org/fussballde";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new FussballdeClient({ apiKey });
const result1 = await client.clubSearch({ text: "Bayern" });
console.log(result1);
const result2 = await client.nationalTopScorers({});
console.log(result2);
```

The client also exports `Client` as an alias for `FussballdeClient`. Operation
methods are available directly in camelCase and through the `fussballde`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-fussballde/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-fussballde/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported Fussball.de API endpoints

This package exposes each route below as a direct method and through the `fussballde` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-fussballde/blob/main/docs/usage.md) for complete input details.

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

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
