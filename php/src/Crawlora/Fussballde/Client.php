<?php

declare(strict_types=1);

namespace Crawlora\Fussballde;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'fussballde';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 27;
    public const OPERATION_IDS = ["fussballde-amateur-stats", "fussballde-club", "fussballde-club-matches", "fussballde-club-search", "fussballde-competition-options", "fussballde-competitions", "fussballde-federation", "fussballde-filters", "fussballde-match", "fussballde-match-calendar", "fussballde-match-comparison", "fussballde-match-plan", "fussballde-matchday", "fussballde-national-top-scorers", "fussballde-news", "fussballde-news-article", "fussballde-news-search", "fussballde-player", "fussballde-player-matches", "fussballde-player-search", "fussballde-position-history", "fussballde-postal-codes", "fussballde-table", "fussballde-team", "fussballde-team-matches", "fussballde-team-squad", "fussballde-top-scorers"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"fussballde-amateur-stats": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-amateur-stats", "method": "GET", "params": [{"description": "Ranking id", "enum": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], "in": "query", "name": "stat", "required": true, "type": "string", "x-example": "8"}, {"description": "Four-digit season code, 2627 for 2026/27; the site offers the current and previous season", "in": "query", "name": "season", "type": "string", "x-example": "2627"}, {"description": "Team type id; omit for all", "enum": ["1", "3", "6", "8", "4", "5", "7", "9"], "in": "query", "name": "team_type", "type": "string", "x-example": "1"}, {"description": "Federation id; omit for all federations", "enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "type": "string", "x-example": "21"}, {"description": "Rows per call, 1 to 100, default 30", "in": "query", "name": "limit", "type": "integer", "x-example": 30}, {"description": "Number of rows to skip, 0 to 1000, default 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/fussballde/amateur-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], "in": "query", "name": "stat", "required": true, "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["1", "3", "6", "8", "4", "5", "7", "9"], "in": "query", "name": "team_type", "type": "string"}, {"enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fussballde-club": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-club", "method": "GET", "params": [{"description": "Club id from a team or match, e.g. 00ES8GN8N400008VVV0AG08LVUPGND5I", "in": "query", "name": "club_id", "required": true, "type": "string", "x-example": "00ES8GN8N400008VVV0AG08LVUPGND5I"}, {"description": "Four-digit season code such as 2526; default current season", "in": "query", "name": "season", "type": "string", "x-example": "2526"}, {"description": "Competition kind id; omit for all kinds", "enum": ["1", "8", "3", "7", "6", "11", "2", "21", "9"], "in": "query", "name": "competition_kind", "type": "string", "x-example": "1"}], "path": "/fussballde/club", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "club_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["1", "8", "3", "7", "6", "11", "2", "21", "9"], "in": "query", "name": "competition_kind", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-club-matches": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-club-matches", "method": "GET", "params": [{"description": "Club id from fussballde-club or fussballde-club-search", "in": "query", "name": "club_id", "required": true, "type": "string", "x-example": "00ES8GN8N400008VVV0AG08LVUPGND5I"}, {"description": "Match list kind, default all", "enum": ["all", "next", "previous"], "in": "query", "name": "kind", "type": "string", "x-example": "all"}, {"description": "kind all only: first day as YYYY-MM-DD, default 1 July of the current season", "in": "query", "name": "date_from", "type": "string", "x-example": "2026-10-01"}, {"description": "kind all only: last day as YYYY-MM-DD, default 30 June of the season", "in": "query", "name": "date_to", "type": "string", "x-example": "2026-10-31"}, {"description": "kind all only: competition kind id; omit for all kinds", "enum": ["1", "8", "3", "7", "6", "11", "2", "21", "9"], "in": "query", "name": "competition_kind", "type": "string", "x-example": "8"}, {"description": "Matches (kind all only) per call, 1 to 50, default 10", "in": "query", "name": "limit", "type": "integer", "x-example": 10}, {"description": "Number of matches to skip, 0 to 1000, default 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/fussballde/club-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "club_id", "required": true, "type": "string"}, {"enum": ["all", "next", "previous"], "in": "query", "name": "kind", "type": "string"}, {"in": "query", "name": "date_from", "type": "string"}, {"in": "query", "name": "date_to", "type": "string"}, {"enum": ["1", "8", "3", "7", "6", "11", "2", "21", "9"], "in": "query", "name": "competition_kind", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fussballde-club-search": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-club-search", "method": "GET", "params": [{"description": "Club name or part of it; text or place is required", "in": "query", "name": "text", "type": "string", "x-example": "Dortmund"}, {"description": "Postcode or place name; text or place is required", "in": "query", "name": "place", "type": "string", "x-example": "44139"}, {"description": "Clubs per call, 1 to 100, default 20", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Number of clubs to skip, 0 to 2000, default 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/fussballde/club-search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "text", "type": "string"}, {"in": "query", "name": "place", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fussballde-competition-options": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-competition-options", "method": "GET", "params": [{"description": "Federation id", "enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "required": true, "type": "string", "x-example": "89"}, {"description": "Four-digit season code, 2627 for 2026/27", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "2627"}, {"description": "Competition type id, default 1", "enum": ["1", "308", "300", "70", "305", "-300", "-305", "11", "2", "-2", "12"], "in": "query", "name": "competition_type", "type": "string", "x-example": "1"}], "path": "/fussballde/competition-options", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["1", "308", "300", "70", "305", "-300", "-305", "11", "2", "-2", "12"], "in": "query", "name": "competition_type", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-competitions": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-competitions", "method": "GET", "params": [{"description": "Federation id", "enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "required": true, "type": "string", "x-example": "89"}, {"description": "Four-digit season code", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "2627"}, {"description": "Competition type id, default 1", "enum": ["1", "308", "300", "70", "305", "-300", "-305", "11", "2", "-2", "12"], "in": "query", "name": "competition_type", "type": "string", "x-example": "1"}, {"description": "Team type id from fussballde-competition-options", "in": "query", "name": "team_type", "required": true, "type": "string", "x-example": "1"}, {"description": "League id from fussballde-competition-options", "in": "query", "name": "league", "required": true, "type": "string", "x-example": "1"}, {"description": "Area id from fussballde-competition-options", "in": "query", "name": "area", "required": true, "type": "string", "x-example": "0123456789ABCDEF0123456700004010"}], "path": "/fussballde/competitions", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["1", "308", "300", "70", "305", "-300", "-305", "11", "2", "-2", "12"], "in": "query", "name": "competition_type", "type": "string"}, {"in": "query", "name": "team_type", "required": true, "type": "string"}, {"in": "query", "name": "league", "required": true, "type": "string"}, {"in": "query", "name": "area", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-federation": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-federation", "method": "GET", "params": [{"description": "Federation id; provide exactly one of federation_id and regional_association", "enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "type": "string", "x-example": "21"}, {"description": "Regional association; provide exactly one of federation_id and regional_association", "enum": ["nord", "nordost", "sued", "suedwest", "west"], "in": "query", "name": "regional_association", "type": "string", "x-example": "west"}], "path": "/fussballde/federation", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "type": "string"}, {"enum": ["nord", "nordost", "sued", "suedwest", "west"], "in": "query", "name": "regional_association", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-filters": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-filters", "method": "GET", "params": [{"description": "Optional federation id that narrows seasons and competition types to one federation", "enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "type": "string", "x-example": "31"}], "path": "/fussballde/filters", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-match": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-match", "method": "GET", "params": [{"description": "Match id from fussballde-matchday or fussballde-match-plan", "in": "query", "name": "match_id", "required": true, "type": "string", "x-example": "031BFTHDCC000000VS5489BUVUR5FS5A"}], "path": "/fussballde/match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "match_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-match-calendar": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-match-calendar", "method": "GET", "params": [{"description": "Five-digit German postcode; look one up with fussballde-postal-codes", "in": "query", "name": "postal_code", "required": true, "type": "string", "x-example": "44139"}, {"description": "First day as YYYY-MM-DD, default today (Europe/Berlin)", "in": "query", "name": "date_from", "type": "string", "x-example": "2026-10-24"}, {"description": "Last day as YYYY-MM-DD, at most 92 days after date_from, default six days after date_from", "in": "query", "name": "date_to", "type": "string", "x-example": "2026-10-31"}, {"description": "Comma-separated team type ids such as 1,3; omit for all team types", "in": "query", "name": "team_types", "type": "string", "x-example": "1,3"}, {"description": "Competition kind id; omit for all kinds", "enum": ["1", "8", "3", "7", "6", "11", "2", "21", "9"], "in": "query", "name": "competition_kind", "type": "string", "x-example": "1"}], "path": "/fussballde/match-calendar", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "postal_code", "required": true, "type": "string"}, {"in": "query", "name": "date_from", "type": "string"}, {"in": "query", "name": "date_to", "type": "string"}, {"in": "query", "name": "team_types", "type": "string"}, {"enum": ["1", "8", "3", "7", "6", "11", "2", "21", "9"], "in": "query", "name": "competition_kind", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-match-comparison": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-match-comparison", "method": "GET", "params": [{"description": "Match id from fussballde-matchday or fussballde-match-plan", "in": "query", "name": "match_id", "required": true, "type": "string", "x-example": "031BFTHDCC000000VS5489BUVUR5FS5A"}, {"description": "Comparison view, default history", "enum": ["history", "meetings", "season"], "in": "query", "name": "view", "type": "string", "x-example": "history"}], "path": "/fussballde/match-comparison", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "match_id", "required": true, "type": "string"}, {"enum": ["history", "meetings", "season"], "in": "query", "name": "view", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-match-plan": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-match-plan", "method": "GET", "params": [{"description": "Competition id from fussballde-competitions", "in": "query", "name": "competition_id", "required": true, "type": "string", "x-example": "031BFREJC800001BVS5489BUVUR5FS5A-G"}, {"description": "Team id to keep only that team's matches", "in": "query", "name": "team_id", "type": "string", "x-example": "011MI8V6UC000000VTVG0001VTR8C1K7"}, {"description": "Earliest match date as YYYY-MM-DD; default is the whole season", "in": "query", "name": "date_from", "type": "string", "x-example": "2026-10-01"}, {"description": "Latest match date as YYYY-MM-DD; default is the whole season", "in": "query", "name": "date_to", "type": "string", "x-example": "2026-10-31"}], "path": "/fussballde/match-plan", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "competition_id", "required": true, "type": "string"}, {"in": "query", "name": "team_id", "type": "string"}, {"in": "query", "name": "date_from", "type": "string"}, {"in": "query", "name": "date_to", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-matchday": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-matchday", "method": "GET", "params": [{"description": "Competition id from fussballde-competitions", "in": "query", "name": "competition_id", "required": true, "type": "string", "x-example": "031BFREJC800001BVS5489BUVUR5FS5A-G"}, {"description": "Matchday date as YYYY-MM-DD; omit for the current matchday; cannot be combined with matchday", "in": "query", "name": "date", "type": "string", "x-example": "2026-10-03"}, {"description": "Matchday number, 1 to the competition's matchday count (34 for the Bundesliga); cannot be combined with date", "in": "query", "name": "matchday", "type": "integer", "x-example": 3}], "path": "/fussballde/matchday", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "competition_id", "required": true, "type": "string"}, {"in": "query", "name": "date", "type": "string"}, {"in": "query", "name": "matchday", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fussballde-national-top-scorers": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-national-top-scorers", "method": "GET", "params": [{"description": "Ranking to return, default men", "enum": ["men", "women"], "in": "query", "name": "team_type", "type": "string", "x-example": "men"}], "path": "/fussballde/national-top-scorers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["men", "women"], "in": "query", "name": "team_type", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-news": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-news", "method": "GET", "params": [{"description": "News stream, default all_news", "enum": ["all_news", "magazin", "regionalliga", "verbaende", "service", "aktionen", "helpcenter"], "in": "query", "name": "stream", "type": "string", "x-example": "all_news"}, {"description": "Only Regionalliga news of one league (implies stream regionalliga)", "enum": ["nord", "nordost", "west", "suedwest", "bayern"], "in": "query", "name": "regional_league", "type": "string", "x-example": "nord"}, {"description": "Only help-center articles of one category (implies stream helpcenter)", "enum": ["allgemeines", "app", "liveticker", "mannschaftsseite", "profile", "registrierung", "training_service", "widgets"], "in": "query", "name": "help_category", "type": "string", "x-example": "app"}, {"description": "Articles per call, 1 to 50, default 10", "in": "query", "name": "limit", "type": "integer", "x-example": 10}, {"description": "Number of articles to skip, 0 to 5000, default 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/fussballde/news", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["all_news", "magazin", "regionalliga", "verbaende", "service", "aktionen", "helpcenter"], "in": "query", "name": "stream", "type": "string"}, {"enum": ["nord", "nordost", "west", "suedwest", "bayern"], "in": "query", "name": "regional_league", "type": "string"}, {"enum": ["allgemeines", "app", "liveticker", "mannschaftsseite", "profile", "registrierung", "training_service", "widgets"], "in": "query", "name": "help_category", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fussballde-news-article": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-news-article", "method": "GET", "params": [{"description": "Numeric article id from fussballde-news", "in": "query", "name": "article_id", "required": true, "type": "string", "x-example": "10067512"}], "path": "/fussballde/news-article", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "article_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-news-search": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-news-search", "method": "GET", "params": [{"description": "Search text, 2 to 80 characters", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "Dortmund"}, {"description": "News channel, default news", "enum": ["news", "pro_news"], "in": "query", "name": "channel", "type": "string", "x-example": "news"}, {"description": "Articles per call, 1 to 50, default 10", "in": "query", "name": "limit", "type": "integer", "x-example": 10}, {"description": "Number of hits to skip, 0 to 10000, default 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/fussballde/news-search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"enum": ["news", "pro_news"], "in": "query", "name": "channel", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fussballde-player": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-player", "method": "GET", "params": [{"description": "Player id from fussballde-player-search, fussballde-top-scorers, fussballde-team-squad or fussballde-amateur-stats", "in": "query", "name": "player_id", "required": true, "type": "string", "x-example": "01MH0AKR7C000007VV0AG13EVSFDFGE6"}], "path": "/fussballde/player", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-player-matches": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-player-matches", "method": "GET", "params": [{"description": "Player id of a full profile, see fussballde-player", "in": "query", "name": "player_id", "required": true, "type": "string", "x-example": "01MH0AKR7C000007VV0AG13EVSFDFGE6"}, {"description": "Four-digit season code, default current season", "in": "query", "name": "season", "type": "string", "x-example": "2627"}, {"description": "Team id from the teams list of a previous response; default the player's main team", "in": "query", "name": "team_id", "type": "string", "x-example": "030POM2JO0000000VS5489BSVSO3A7B3"}], "path": "/fussballde/player-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"in": "query", "name": "team_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-player-search": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-player-search", "method": "GET", "params": [{"description": "First name; first_name or last_name is required", "in": "query", "name": "first_name", "type": "string", "x-example": "Niclas"}, {"description": "Last name; first_name or last_name is required", "in": "query", "name": "last_name", "type": "string", "x-example": "Füllkrug"}, {"description": "Postcode or place name to narrow the result; cannot be used alone", "in": "query", "name": "place", "type": "string", "x-example": "44139"}, {"description": "Players per call, 1 to 100, default 20", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Number of players to skip, 0 to 2000, default 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/fussballde/player-search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "first_name", "type": "string"}, {"in": "query", "name": "last_name", "type": "string"}, {"in": "query", "name": "place", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fussballde-position-history": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-position-history", "method": "GET", "params": [{"description": "Competition id from fussballde-competitions", "in": "query", "name": "competition_id", "required": true, "type": "string", "x-example": "031BFREJC800001BVS5489BUVUR5FS5A-G"}], "path": "/fussballde/position-history", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "competition_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-postal-codes": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-postal-codes", "method": "GET", "params": [{"description": "Place name or postcode prefix, 2 to 40 characters", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "Dortmund"}], "path": "/fussballde/postal-codes", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-table": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-table", "method": "GET", "params": [{"description": "Competition id from fussballde-competitions", "in": "query", "name": "competition_id", "required": true, "type": "string", "x-example": "031BFREJC800001BVS5489BUVUR5FS5A-G"}, {"description": "Standings view, default overall", "enum": ["overall", "home_away", "rounds", "fairness", "cross"], "in": "query", "name": "view", "type": "string", "x-example": "overall"}, {"description": "Return the standings after this matchday, 1 to the competition's matchday count; not available for the fairness view", "in": "query", "name": "matchday", "type": "integer", "x-example": 3}], "path": "/fussballde/table", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "competition_id", "required": true, "type": "string"}, {"enum": ["overall", "home_away", "rounds", "fairness", "cross"], "in": "query", "name": "view", "type": "string"}, {"in": "query", "name": "matchday", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fussballde-team": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-team", "method": "GET", "params": [{"description": "Team id from fussballde-matchday, fussballde-table or fussballde-club", "in": "query", "name": "team_id", "required": true, "type": "string", "x-example": "011MI8V6UC000000VTVG0001VTR8C1K7"}], "path": "/fussballde/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-team-matches": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-team-matches", "method": "GET", "params": [{"description": "Team id, see fussballde-team", "in": "query", "name": "team_id", "required": true, "type": "string", "x-example": "011MI8V6UC000000VTVG0001VTR8C1K7"}, {"description": "Match list kind, default all", "enum": ["all", "next", "previous", "wins", "draws", "losses"], "in": "query", "name": "kind", "type": "string", "x-example": "all"}, {"description": "kind all only: first day as YYYY-MM-DD, default 1 July of the current season", "in": "query", "name": "date_from", "type": "string", "x-example": "2026-07-01"}, {"description": "kind all only: last day as YYYY-MM-DD, default 30 June of the season", "in": "query", "name": "date_to", "type": "string", "x-example": "2027-06-30"}, {"description": "kind all only: competition kind id; omit for all kinds", "enum": ["1", "8", "3", "7", "6", "11", "2", "21", "9"], "in": "query", "name": "competition_kind", "type": "string", "x-example": "8"}, {"description": "Matches (kind all only) per call, 1 to 50, default 10", "in": "query", "name": "limit", "type": "integer", "x-example": 10}, {"description": "Number of matches to skip, 0 to 1000, default 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/fussballde/team-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "string"}, {"enum": ["all", "next", "previous", "wins", "draws", "losses"], "in": "query", "name": "kind", "type": "string"}, {"in": "query", "name": "date_from", "type": "string"}, {"in": "query", "name": "date_to", "type": "string"}, {"enum": ["1", "8", "3", "7", "6", "11", "2", "21", "9"], "in": "query", "name": "competition_kind", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fussballde-team-squad": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-team-squad", "method": "GET", "params": [{"description": "Team id, see fussballde-team", "in": "query", "name": "team_id", "required": true, "type": "string", "x-example": "011MI8V6UC000000VTVG0001VTR8C1K7"}, {"description": "Four-digit season code, default current season", "in": "query", "name": "season", "type": "string", "x-example": "2627"}, {"description": "Player list kind, default squad", "enum": ["squad", "arrivals", "departures"], "in": "query", "name": "kind", "type": "string", "x-example": "squad"}], "path": "/fussballde/team-squad", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["squad", "arrivals", "departures"], "in": "query", "name": "kind", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-top-scorers": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-top-scorers", "method": "GET", "params": [{"description": "Competition id from fussballde-competitions", "in": "query", "name": "competition_id", "required": true, "type": "string", "x-example": "031BFREJC800001BVS5489BUVUR5FS5A-G"}, {"description": "Scorers per call, 1 to 100, default 30", "in": "query", "name": "limit", "type": "integer", "x-example": 30}, {"description": "Number of scorers to skip, 0 to 1000, default 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/fussballde/top-scorers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "competition_id", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-fussballde-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function amateur_stats(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-amateur-stats", $params, $responseType);
    }
    public function club(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-club", $params, $responseType);
    }
    public function club_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-club-matches", $params, $responseType);
    }
    public function club_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-club-search", $params, $responseType);
    }
    public function competition_options(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-competition-options", $params, $responseType);
    }
    public function competitions(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-competitions", $params, $responseType);
    }
    public function federation(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-federation", $params, $responseType);
    }
    public function filters(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-filters", $params, $responseType);
    }
    public function match(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-match", $params, $responseType);
    }
    public function match_calendar(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-match-calendar", $params, $responseType);
    }
    public function match_comparison(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-match-comparison", $params, $responseType);
    }
    public function match_plan(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-match-plan", $params, $responseType);
    }
    public function matchday(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-matchday", $params, $responseType);
    }
    public function national_top_scorers(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-national-top-scorers", $params, $responseType);
    }
    public function news(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-news", $params, $responseType);
    }
    public function news_article(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-news-article", $params, $responseType);
    }
    public function news_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-news-search", $params, $responseType);
    }
    public function player(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-player", $params, $responseType);
    }
    public function player_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-player-matches", $params, $responseType);
    }
    public function player_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-player-search", $params, $responseType);
    }
    public function position_history(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-position-history", $params, $responseType);
    }
    public function postal_codes(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-postal-codes", $params, $responseType);
    }
    public function table(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-table", $params, $responseType);
    }
    public function team(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-team", $params, $responseType);
    }
    public function team_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-team-matches", $params, $responseType);
    }
    public function team_squad(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-team-squad", $params, $responseType);
    }
    public function top_scorers(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fussballde-top-scorers", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
