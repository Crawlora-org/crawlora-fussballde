# Crawlora Fussball.de API client for PHP (`crawlora/fussballde`)

This PHP package calls Crawlora's hosted Fussball.de API at `https://api.crawlora.net/api/v1`. It exposes 27 endpoints covering amateur football clubs, players, matches, statistics, news, and federation data. It does not call or scrape Fussball.de directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/fussballde
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=fussballde-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=fussballde-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Fussballde\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("fussballde-club-search", []);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 27 API operations.

## Supported Fussball.de API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-fussballde/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=fussballde-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=fussballde-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-fussballde). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-fussballde/blob/main/docs/usage.md).
