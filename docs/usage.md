# Fussball.de API endpoint reference and client usage

This reference lists all 27 public Fussball.de API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/fussballde`, `crawlora-fussballde`, and `crawlora-fussballde` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Fussball.de locally; Crawlora is independent from and not endorsed by Fussball.de or its owners.

The package tracks the public API contract revision `sha256:c0a322b3f5d6832b349dd86359e8c7e3cb9ba91c30cab51a67acc9a0fe3960a1` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `fussballde`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `amateurStats` | `amateur_stats` | `fussballde.amateur_stats` | `GET /fussballde/amateur-stats` | `stat` (query, required; values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`), `season` (query, optional), `team_type` (query, optional; values: `1`, `3`, `6`, `8`, `4`, `5`, `7`, `9`), `federation_id` (query, optional; values: `89`, `32`, `31`, `66`, `61`, `02`, `03`, `34`, `62`, `23`, `22`, `01`, `41`, `43`, `63`, `64`, `04`, `33`, `42`, `65`, `21`, `35`), `limit` (query, optional), `offset` (query, optional) | Get FUSSBALL.DE amateur top statistics |
| `club` | `club` | `fussballde.club` | `GET /fussballde/club` | `club_id` (query, required), `season` (query, optional), `competition_kind` (query, optional; values: `1`, `8`, `3`, `7`, `6`, `11`, `2`, `21`, `9`) | Get a FUSSBALL.DE club |
| `clubMatches` | `club_matches` | `fussballde.club_matches` | `GET /fussballde/club-matches` | `club_id` (query, required), `kind` (query, optional; values: `all`, `next`, `previous`), `date_from` (query, optional), `date_to` (query, optional), `competition_kind` (query, optional; values: `1`, `8`, `3`, `7`, `6`, `11`, `2`, `21`, `9`), `limit` (query, optional), `offset` (query, optional) | Get FUSSBALL.DE fixtures and results of a club |
| `clubSearch` | `club_search` | `fussballde.club_search` | `GET /fussballde/club-search` | `text` (query, optional), `place` (query, optional), `limit` (query, optional), `offset` (query, optional) | Search FUSSBALL.DE clubs by name or place |
| `competitionOptions` | `competition_options` | `fussballde.competition_options` | `GET /fussballde/competition-options` | `federation_id` (query, required; values: `89`, `32`, `31`, `66`, `61`, `02`, `03`, `34`, `62`, `23`, `22`, `01`, `41`, `43`, `63`, `64`, `04`, `33`, `42`, `65`, `21`, `35`), `season` (query, required), `competition_type` (query, optional; values: `1`, `308`, `300`, `70`, `305`, `-300`, `-305`, `11`, `2`, `-2`, `12`) | List FUSSBALL.DE team types, leagues and areas |
| `competitions` | `competitions` | `fussballde.competitions` | `GET /fussballde/competitions` | `federation_id` (query, required; values: `89`, `32`, `31`, `66`, `61`, `02`, `03`, `34`, `62`, `23`, `22`, `01`, `41`, `43`, `63`, `64`, `04`, `33`, `42`, `65`, `21`, `35`), `season` (query, required), `competition_type` (query, optional; values: `1`, `308`, `300`, `70`, `305`, `-300`, `-305`, `11`, `2`, `-2`, `12`), `team_type` (query, required), `league` (query, required), `area` (query, required) | List FUSSBALL.DE competitions for a league and area |
| `federation` | `federation` | `fussballde.federation` | `GET /fussballde/federation` | `federation_id` (query, optional; values: `89`, `32`, `31`, `66`, `61`, `02`, `03`, `34`, `62`, `23`, `22`, `01`, `41`, `43`, `63`, `64`, `04`, `33`, `42`, `65`, `21`, `35`), `regional_association` (query, optional; values: `nord`, `nordost`, `sued`, `suedwest`, `west`) | Get a FUSSBALL.DE federation or regional association |
| `filters` | `filters` | `fussballde.filters` | `GET /fussballde/filters` | `federation_id` (query, optional; values: `89`, `32`, `31`, `66`, `61`, `02`, `03`, `34`, `62`, `23`, `22`, `01`, `41`, `43`, `63`, `64`, `04`, `33`, `42`, `65`, `21`, `35`) | List FUSSBALL.DE federations, seasons and competition types |
| `match` | `match` | `fussballde.match_` | `GET /fussballde/match` | `match_id` (query, required) | Get a FUSSBALL.DE match |
| `matchCalendar` | `match_calendar` | `fussballde.match_calendar` | `GET /fussballde/match-calendar` | `postal_code` (query, required), `date_from` (query, optional), `date_to` (query, optional), `team_types` (query, optional), `competition_kind` (query, optional; values: `1`, `8`, `3`, `7`, `6`, `11`, `2`, `21`, `9`) | Get FUSSBALL.DE matches near a postcode |
| `matchComparison` | `match_comparison` | `fussballde.match_comparison` | `GET /fussballde/match-comparison` | `match_id` (query, required), `view` (query, optional; values: `history`, `meetings`, `season`) | Compare the two teams of a FUSSBALL.DE match |
| `matchday` | `matchday` | `fussballde.matchday` | `GET /fussballde/matchday` | `competition_id` (query, required), `date` (query, optional), `matchday` (query, optional) | Get FUSSBALL.DE matches of a competition matchday |
| `matchPlan` | `match_plan` | `fussballde.match_plan` | `GET /fussballde/match-plan` | `competition_id` (query, required), `team_id` (query, optional), `date_from` (query, optional), `date_to` (query, optional) | Get the full FUSSBALL.DE match plan of a competition |
| `nationalTopScorers` | `national_top_scorers` | `fussballde.national_top_scorers` | `GET /fussballde/national-top-scorers` | `team_type` (query, optional; values: `men`, `women`) | Get the nationwide FUSSBALL.DE top scorers by league level |
| `news` | `news` | `fussballde.news` | `GET /fussballde/news` | `stream` (query, optional; values: `all_news`, `magazin`, `regionalliga`, `verbaende`, `service`, `aktionen`, `helpcenter`), `regional_league` (query, optional; values: `nord`, `nordost`, `west`, `suedwest`, `bayern`), `help_category` (query, optional; values: `allgemeines`, `app`, `liveticker`, `mannschaftsseite`, `profile`, `registrierung`, `training_service`, `widgets`), `limit` (query, optional), `offset` (query, optional) | List FUSSBALL.DE news |
| `newsArticle` | `news_article` | `fussballde.news_article` | `GET /fussballde/news-article` | `article_id` (query, required) | Get a FUSSBALL.DE news article |
| `newsSearch` | `news_search` | `fussballde.news_search` | `GET /fussballde/news-search` | `q` (query, required), `channel` (query, optional; values: `news`, `pro_news`), `limit` (query, optional), `offset` (query, optional) | Search FUSSBALL.DE news |
| `player` | `player` | `fussballde.player` | `GET /fussballde/player` | `player_id` (query, required) | Get a FUSSBALL.DE player profile |
| `playerMatches` | `player_matches` | `fussballde.player_matches` | `GET /fussballde/player-matches` | `player_id` (query, required), `season` (query, optional), `team_id` (query, optional) | Get a FUSSBALL.DE player's match-by-match record |
| `playerSearch` | `player_search` | `fussballde.player_search` | `GET /fussballde/player-search` | `first_name` (query, optional), `last_name` (query, optional), `place` (query, optional), `limit` (query, optional), `offset` (query, optional) | Search FUSSBALL.DE players by name |
| `positionHistory` | `position_history` | `fussballde.position_history` | `GET /fussballde/position-history` | `competition_id` (query, required) | Get the FUSSBALL.DE fever curve of a competition |
| `postalCodes` | `postal_codes` | `fussballde.postal_codes` | `GET /fussballde/postal-codes` | `q` (query, required) | Look up German postcodes by place name |
| `table` | `table` | `fussballde.table` | `GET /fussballde/table` | `competition_id` (query, required), `view` (query, optional; values: `overall`, `home_away`, `rounds`, `fairness`, `cross`), `matchday` (query, optional) | Get a FUSSBALL.DE competition standings table |
| `team` | `team` | `fussballde.team` | `GET /fussballde/team` | `team_id` (query, required) | Get a FUSSBALL.DE team |
| `teamMatches` | `team_matches` | `fussballde.team_matches` | `GET /fussballde/team-matches` | `team_id` (query, required), `kind` (query, optional; values: `all`, `next`, `previous`, `wins`, `draws`, `losses`), `date_from` (query, optional), `date_to` (query, optional), `competition_kind` (query, optional; values: `1`, `8`, `3`, `7`, `6`, `11`, `2`, `21`, `9`), `limit` (query, optional), `offset` (query, optional) | Get FUSSBALL.DE fixtures and results of a team |
| `teamSquad` | `team_squad` | `fussballde.team_squad` | `GET /fussballde/team-squad` | `team_id` (query, required), `season` (query, optional), `kind` (query, optional; values: `squad`, `arrivals`, `departures`) | Get a FUSSBALL.DE team squad |
| `topScorers` | `top_scorers` | `fussballde.top_scorers` | `GET /fussballde/top-scorers` | `competition_id` (query, required), `limit` (query, optional), `offset` (query, optional) | Get the FUSSBALL.DE top scorers of a competition |

## Client forms

- JavaScript: import `FussballdeClient` (also exported as `Client`) from `@crawlora-org/fussballde`; use `new FussballdeClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `FussballdeClient` (also exported as `Client`) from `crawlora_fussballde`; use `with FussballdeClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncFussballdeClient`, used with `async with` and `await`.
- Rust: add `crawlora-fussballde` with Cargo; import `Client` and the generated operation parameter struct, then call `client.fussballde.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-fussballde/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
