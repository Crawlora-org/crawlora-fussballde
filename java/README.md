# Crawlora Fussball.de API client for Java

The official Java client for Crawlora's hosted Fussball.de API. It exposes 27 endpoints covering amateur football clubs, players, matches, statistics, news, and federation data. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-fussballde</artifactId>
  <version>0.1.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=fussballde-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=fussballde-java-console) to get an API key.

```java
import net.crawlora.fussballde.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.clubSearch(Map.ofEntries(Map.entry("text", "Bayern")));
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported Fussball.de API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-fussballde/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=fussballde-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-fussballde)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=fussballde-java-api-docs)
