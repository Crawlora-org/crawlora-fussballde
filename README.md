# Fussball.de clients for Crawlora

Official Crawlora client packages for the hosted Fussball.de API. Access 27 API endpoints covering amateur football clubs, players, matches, statistics, news, and federation data from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape Fussball.de locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Fussball.de or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/fussballde`](javascript/README.md)
- Python: [`crawlora-fussballde`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-fussballde`](go.mod)
- Ruby: [`crawlora-fussballde`](ruby/README.md)
- Java: [`net.crawlora:crawlora-fussballde:0.1.0`](java/README.md)
- PHP: [`crawlora/fussballde`](php/README.md)
- Rust: [`crawlora-fussballde`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=fussballde-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=fussballde-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=fussballde-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 27 selected public Fussball.de API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

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

## License

MIT. See [LICENSE](LICENSE).
