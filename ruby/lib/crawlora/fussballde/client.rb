require "json"
require "net/http"
require "uri"

module Crawlora
  module Fussballde
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"fussballde-amateur-stats": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-amateur-stats", "method": "GET", "params": [{"description": "Ranking id", "enum": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], "in": "query", "name": "stat", "required": true, "type": "string", "x-example": "8"}, {"description": "Four-digit season code, 2627 for 2026/27; the site offers the current and previous season", "in": "query", "name": "season", "type": "string", "x-example": "2627"}, {"description": "Team type id; omit for all", "enum": ["1", "3", "6", "8", "4", "5", "7", "9"], "in": "query", "name": "team_type", "type": "string", "x-example": "1"}, {"description": "Federation id; omit for all federations", "enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "type": "string", "x-example": "21"}, {"description": "Rows per call, 1 to 100, default 30", "in": "query", "name": "limit", "type": "integer", "x-example": 30}, {"description": "Number of rows to skip, 0 to 1000, default 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/fussballde/amateur-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], "in": "query", "name": "stat", "required": true, "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["1", "3", "6", "8", "4", "5", "7", "9"], "in": "query", "name": "team_type", "type": "string"}, {"enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fussballde-club": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-club", "method": "GET", "params": [{"description": "Club id from a team or match, e.g. 00ES8GN8N400008VVV0AG08LVUPGND5I", "in": "query", "name": "club_id", "required": true, "type": "string", "x-example": "00ES8GN8N400008VVV0AG08LVUPGND5I"}, {"description": "Four-digit season code such as 2526; default current season", "in": "query", "name": "season", "type": "string", "x-example": "2526"}, {"description": "Competition kind id; omit for all kinds", "enum": ["1", "8", "3", "7", "6", "11", "2", "21", "9"], "in": "query", "name": "competition_kind", "type": "string", "x-example": "1"}], "path": "/fussballde/club", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "club_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["1", "8", "3", "7", "6", "11", "2", "21", "9"], "in": "query", "name": "competition_kind", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-club-matches": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-club-matches", "method": "GET", "params": [{"description": "Club id from fussballde-club or fussballde-club-search", "in": "query", "name": "club_id", "required": true, "type": "string", "x-example": "00ES8GN8N400008VVV0AG08LVUPGND5I"}, {"description": "Match list kind, default all", "enum": ["all", "next", "previous"], "in": "query", "name": "kind", "type": "string", "x-example": "all"}, {"description": "kind all only: first day as YYYY-MM-DD, default 1 July of the current season", "in": "query", "name": "date_from", "type": "string", "x-example": "2026-10-01"}, {"description": "kind all only: last day as YYYY-MM-DD, default 30 June of the season", "in": "query", "name": "date_to", "type": "string", "x-example": "2026-10-31"}, {"description": "kind all only: competition kind id; omit for all kinds", "enum": ["1", "8", "3", "7", "6", "11", "2", "21", "9"], "in": "query", "name": "competition_kind", "type": "string", "x-example": "8"}, {"description": "Matches (kind all only) per call, 1 to 50, default 10", "in": "query", "name": "limit", "type": "integer", "x-example": 10}, {"description": "Number of matches to skip, 0 to 1000, default 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/fussballde/club-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "club_id", "required": true, "type": "string"}, {"enum": ["all", "next", "previous"], "in": "query", "name": "kind", "type": "string"}, {"in": "query", "name": "date_from", "type": "string"}, {"in": "query", "name": "date_to", "type": "string"}, {"enum": ["1", "8", "3", "7", "6", "11", "2", "21", "9"], "in": "query", "name": "competition_kind", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fussballde-club-search": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-club-search", "method": "GET", "params": [{"description": "Club name or part of it; text or place is required", "in": "query", "name": "text", "type": "string", "x-example": "Dortmund"}, {"description": "Postcode or place name; text or place is required", "in": "query", "name": "place", "type": "string", "x-example": "44139"}, {"description": "Clubs per call, 1 to 100, default 20", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Number of clubs to skip, 0 to 2000, default 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/fussballde/club-search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "text", "type": "string"}, {"in": "query", "name": "place", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fussballde-competition-options": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-competition-options", "method": "GET", "params": [{"description": "Federation id", "enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "required": true, "type": "string", "x-example": "89"}, {"description": "Four-digit season code, 2627 for 2026/27", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "2627"}, {"description": "Competition type id, default 1", "enum": ["1", "308", "300", "70", "305", "-300", "-305", "11", "2", "-2", "12"], "in": "query", "name": "competition_type", "type": "string", "x-example": "1"}], "path": "/fussballde/competition-options", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["1", "308", "300", "70", "305", "-300", "-305", "11", "2", "-2", "12"], "in": "query", "name": "competition_type", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-competitions": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-competitions", "method": "GET", "params": [{"description": "Federation id", "enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "required": true, "type": "string", "x-example": "89"}, {"description": "Four-digit season code", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "2627"}, {"description": "Competition type id, default 1", "enum": ["1", "308", "300", "70", "305", "-300", "-305", "11", "2", "-2", "12"], "in": "query", "name": "competition_type", "type": "string", "x-example": "1"}, {"description": "Team type id from fussballde-competition-options", "in": "query", "name": "team_type", "required": true, "type": "string", "x-example": "1"}, {"description": "League id from fussballde-competition-options", "in": "query", "name": "league", "required": true, "type": "string", "x-example": "1"}, {"description": "Area id from fussballde-competition-options", "in": "query", "name": "area", "required": true, "type": "string", "x-example": "0123456789ABCDEF0123456700004010"}], "path": "/fussballde/competitions", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["1", "308", "300", "70", "305", "-300", "-305", "11", "2", "-2", "12"], "in": "query", "name": "competition_type", "type": "string"}, {"in": "query", "name": "team_type", "required": true, "type": "string"}, {"in": "query", "name": "league", "required": true, "type": "string"}, {"in": "query", "name": "area", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-federation": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-federation", "method": "GET", "params": [{"description": "Federation id; provide exactly one of federation_id and regional_association", "enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "type": "string", "x-example": "21"}, {"description": "Regional association; provide exactly one of federation_id and regional_association", "enum": ["nord", "nordost", "sued", "suedwest", "west"], "in": "query", "name": "regional_association", "type": "string", "x-example": "west"}], "path": "/fussballde/federation", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "type": "string"}, {"enum": ["nord", "nordost", "sued", "suedwest", "west"], "in": "query", "name": "regional_association", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-filters": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-filters", "method": "GET", "params": [{"description": "Optional federation id that narrows seasons and competition types to one federation", "enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "type": "string", "x-example": "31"}], "path": "/fussballde/filters", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"], "in": "query", "name": "federation_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-match": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-match", "method": "GET", "params": [{"description": "Match id from fussballde-matchday or fussballde-match-plan", "in": "query", "name": "match_id", "required": true, "type": "string", "x-example": "031BFTHDCC000000VS5489BUVUR5FS5A"}], "path": "/fussballde/match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "match_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-match-calendar": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-match-calendar", "method": "GET", "params": [{"description": "Five-digit German postcode; look one up with fussballde-postal-codes", "in": "query", "name": "postal_code", "required": true, "type": "string", "x-example": "44139"}, {"description": "First day as YYYY-MM-DD, default today (Europe/Berlin)", "in": "query", "name": "date_from", "type": "string", "x-example": "2026-10-24"}, {"description": "Last day as YYYY-MM-DD, at most 92 days after date_from, default six days after date_from", "in": "query", "name": "date_to", "type": "string", "x-example": "2026-10-31"}, {"description": "Comma-separated team type ids such as 1,3; omit for all team types", "in": "query", "name": "team_types", "type": "string", "x-example": "1,3"}, {"description": "Competition kind id; omit for all kinds", "enum": ["1", "8", "3", "7", "6", "11", "2", "21", "9"], "in": "query", "name": "competition_kind", "type": "string", "x-example": "1"}], "path": "/fussballde/match-calendar", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "postal_code", "required": true, "type": "string"}, {"in": "query", "name": "date_from", "type": "string"}, {"in": "query", "name": "date_to", "type": "string"}, {"in": "query", "name": "team_types", "type": "string"}, {"enum": ["1", "8", "3", "7", "6", "11", "2", "21", "9"], "in": "query", "name": "competition_kind", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-match-comparison": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-match-comparison", "method": "GET", "params": [{"description": "Match id from fussballde-matchday or fussballde-match-plan", "in": "query", "name": "match_id", "required": true, "type": "string", "x-example": "031BFTHDCC000000VS5489BUVUR5FS5A"}, {"description": "Comparison view, default history", "enum": ["history", "meetings", "season"], "in": "query", "name": "view", "type": "string", "x-example": "history"}], "path": "/fussballde/match-comparison", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "match_id", "required": true, "type": "string"}, {"enum": ["history", "meetings", "season"], "in": "query", "name": "view", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-match-plan": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-match-plan", "method": "GET", "params": [{"description": "Competition id from fussballde-competitions", "in": "query", "name": "competition_id", "required": true, "type": "string", "x-example": "031BFREJC800001BVS5489BUVUR5FS5A-G"}, {"description": "Team id to keep only that team's matches", "in": "query", "name": "team_id", "type": "string", "x-example": "011MI8V6UC000000VTVG0001VTR8C1K7"}, {"description": "Earliest match date as YYYY-MM-DD; default is the whole season", "in": "query", "name": "date_from", "type": "string", "x-example": "2026-10-01"}, {"description": "Latest match date as YYYY-MM-DD; default is the whole season", "in": "query", "name": "date_to", "type": "string", "x-example": "2026-10-31"}], "path": "/fussballde/match-plan", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "competition_id", "required": true, "type": "string"}, {"in": "query", "name": "team_id", "type": "string"}, {"in": "query", "name": "date_from", "type": "string"}, {"in": "query", "name": "date_to", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-matchday": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-matchday", "method": "GET", "params": [{"description": "Competition id from fussballde-competitions", "in": "query", "name": "competition_id", "required": true, "type": "string", "x-example": "031BFREJC800001BVS5489BUVUR5FS5A-G"}, {"description": "Matchday date as YYYY-MM-DD; omit for the current matchday; cannot be combined with matchday", "in": "query", "name": "date", "type": "string", "x-example": "2026-10-03"}, {"description": "Matchday number, 1 to the competition's matchday count (34 for the Bundesliga); cannot be combined with date", "in": "query", "name": "matchday", "type": "integer", "x-example": 3}], "path": "/fussballde/matchday", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "competition_id", "required": true, "type": "string"}, {"in": "query", "name": "date", "type": "string"}, {"in": "query", "name": "matchday", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fussballde-national-top-scorers": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-national-top-scorers", "method": "GET", "params": [{"description": "Ranking to return, default men", "enum": ["men", "women"], "in": "query", "name": "team_type", "type": "string", "x-example": "men"}], "path": "/fussballde/national-top-scorers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["men", "women"], "in": "query", "name": "team_type", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-news": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-news", "method": "GET", "params": [{"description": "News stream, default all_news", "enum": ["all_news", "magazin", "regionalliga", "verbaende", "service", "aktionen", "helpcenter"], "in": "query", "name": "stream", "type": "string", "x-example": "all_news"}, {"description": "Only Regionalliga news of one league (implies stream regionalliga)", "enum": ["nord", "nordost", "west", "suedwest", "bayern"], "in": "query", "name": "regional_league", "type": "string", "x-example": "nord"}, {"description": "Only help-center articles of one category (implies stream helpcenter)", "enum": ["allgemeines", "app", "liveticker", "mannschaftsseite", "profile", "registrierung", "training_service", "widgets"], "in": "query", "name": "help_category", "type": "string", "x-example": "app"}, {"description": "Articles per call, 1 to 50, default 10", "in": "query", "name": "limit", "type": "integer", "x-example": 10}, {"description": "Number of articles to skip, 0 to 5000, default 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/fussballde/news", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["all_news", "magazin", "regionalliga", "verbaende", "service", "aktionen", "helpcenter"], "in": "query", "name": "stream", "type": "string"}, {"enum": ["nord", "nordost", "west", "suedwest", "bayern"], "in": "query", "name": "regional_league", "type": "string"}, {"enum": ["allgemeines", "app", "liveticker", "mannschaftsseite", "profile", "registrierung", "training_service", "widgets"], "in": "query", "name": "help_category", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fussballde-news-article": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-news-article", "method": "GET", "params": [{"description": "Numeric article id from fussballde-news", "in": "query", "name": "article_id", "required": true, "type": "string", "x-example": "10067512"}], "path": "/fussballde/news-article", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "article_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-news-search": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-news-search", "method": "GET", "params": [{"description": "Search text, 2 to 80 characters", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "Dortmund"}, {"description": "News channel, default news", "enum": ["news", "pro_news"], "in": "query", "name": "channel", "type": "string", "x-example": "news"}, {"description": "Articles per call, 1 to 50, default 10", "in": "query", "name": "limit", "type": "integer", "x-example": 10}, {"description": "Number of hits to skip, 0 to 10000, default 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/fussballde/news-search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"enum": ["news", "pro_news"], "in": "query", "name": "channel", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fussballde-player": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-player", "method": "GET", "params": [{"description": "Player id from fussballde-player-search, fussballde-top-scorers, fussballde-team-squad or fussballde-amateur-stats", "in": "query", "name": "player_id", "required": true, "type": "string", "x-example": "01MH0AKR7C000007VV0AG13EVSFDFGE6"}], "path": "/fussballde/player", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-player-matches": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-player-matches", "method": "GET", "params": [{"description": "Player id of a full profile, see fussballde-player", "in": "query", "name": "player_id", "required": true, "type": "string", "x-example": "01MH0AKR7C000007VV0AG13EVSFDFGE6"}, {"description": "Four-digit season code, default current season", "in": "query", "name": "season", "type": "string", "x-example": "2627"}, {"description": "Team id from the teams list of a previous response; default the player's main team", "in": "query", "name": "team_id", "type": "string", "x-example": "030POM2JO0000000VS5489BSVSO3A7B3"}], "path": "/fussballde/player-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"in": "query", "name": "team_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-player-search": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-player-search", "method": "GET", "params": [{"description": "First name; first_name or last_name is required", "in": "query", "name": "first_name", "type": "string", "x-example": "Niclas"}, {"description": "Last name; first_name or last_name is required", "in": "query", "name": "last_name", "type": "string", "x-example": "Füllkrug"}, {"description": "Postcode or place name to narrow the result; cannot be used alone", "in": "query", "name": "place", "type": "string", "x-example": "44139"}, {"description": "Players per call, 1 to 100, default 20", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Number of players to skip, 0 to 2000, default 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/fussballde/player-search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "first_name", "type": "string"}, {"in": "query", "name": "last_name", "type": "string"}, {"in": "query", "name": "place", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fussballde-position-history": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-position-history", "method": "GET", "params": [{"description": "Competition id from fussballde-competitions", "in": "query", "name": "competition_id", "required": true, "type": "string", "x-example": "031BFREJC800001BVS5489BUVUR5FS5A-G"}], "path": "/fussballde/position-history", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "competition_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-postal-codes": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-postal-codes", "method": "GET", "params": [{"description": "Place name or postcode prefix, 2 to 40 characters", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "Dortmund"}], "path": "/fussballde/postal-codes", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-table": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-table", "method": "GET", "params": [{"description": "Competition id from fussballde-competitions", "in": "query", "name": "competition_id", "required": true, "type": "string", "x-example": "031BFREJC800001BVS5489BUVUR5FS5A-G"}, {"description": "Standings view, default overall", "enum": ["overall", "home_away", "rounds", "fairness", "cross"], "in": "query", "name": "view", "type": "string", "x-example": "overall"}, {"description": "Return the standings after this matchday, 1 to the competition's matchday count; not available for the fairness view", "in": "query", "name": "matchday", "type": "integer", "x-example": 3}], "path": "/fussballde/table", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "competition_id", "required": true, "type": "string"}, {"enum": ["overall", "home_away", "rounds", "fairness", "cross"], "in": "query", "name": "view", "type": "string"}, {"in": "query", "name": "matchday", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fussballde-team": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-team", "method": "GET", "params": [{"description": "Team id from fussballde-matchday, fussballde-table or fussballde-club", "in": "query", "name": "team_id", "required": true, "type": "string", "x-example": "011MI8V6UC000000VTVG0001VTR8C1K7"}], "path": "/fussballde/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-team-matches": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-team-matches", "method": "GET", "params": [{"description": "Team id, see fussballde-team", "in": "query", "name": "team_id", "required": true, "type": "string", "x-example": "011MI8V6UC000000VTVG0001VTR8C1K7"}, {"description": "Match list kind, default all", "enum": ["all", "next", "previous", "wins", "draws", "losses"], "in": "query", "name": "kind", "type": "string", "x-example": "all"}, {"description": "kind all only: first day as YYYY-MM-DD, default 1 July of the current season", "in": "query", "name": "date_from", "type": "string", "x-example": "2026-07-01"}, {"description": "kind all only: last day as YYYY-MM-DD, default 30 June of the season", "in": "query", "name": "date_to", "type": "string", "x-example": "2027-06-30"}, {"description": "kind all only: competition kind id; omit for all kinds", "enum": ["1", "8", "3", "7", "6", "11", "2", "21", "9"], "in": "query", "name": "competition_kind", "type": "string", "x-example": "8"}, {"description": "Matches (kind all only) per call, 1 to 50, default 10", "in": "query", "name": "limit", "type": "integer", "x-example": 10}, {"description": "Number of matches to skip, 0 to 1000, default 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/fussballde/team-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "string"}, {"enum": ["all", "next", "previous", "wins", "draws", "losses"], "in": "query", "name": "kind", "type": "string"}, {"in": "query", "name": "date_from", "type": "string"}, {"in": "query", "name": "date_to", "type": "string"}, {"enum": ["1", "8", "3", "7", "6", "11", "2", "21", "9"], "in": "query", "name": "competition_kind", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fussballde-team-squad": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-team-squad", "method": "GET", "params": [{"description": "Team id, see fussballde-team", "in": "query", "name": "team_id", "required": true, "type": "string", "x-example": "011MI8V6UC000000VTVG0001VTR8C1K7"}, {"description": "Four-digit season code, default current season", "in": "query", "name": "season", "type": "string", "x-example": "2627"}, {"description": "Player list kind, default squad", "enum": ["squad", "arrivals", "departures"], "in": "query", "name": "kind", "type": "string", "x-example": "squad"}], "path": "/fussballde/team-squad", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["squad", "arrivals", "departures"], "in": "query", "name": "kind", "type": "string"}], "security": ["ApiKeyAuth"]}, "fussballde-top-scorers": {"bodyParam": null, "bodyRequired": false, "id": "fussballde-top-scorers", "method": "GET", "params": [{"description": "Competition id from fussballde-competitions", "in": "query", "name": "competition_id", "required": true, "type": "string", "x-example": "031BFREJC800001BVS5489BUVUR5FS5A-G"}, {"description": "Scorers per call, 1 to 100, default 30", "in": "query", "name": "limit", "type": "integer", "x-example": 30}, {"description": "Number of scorers to skip, 0 to 1000, default 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/fussballde/top-scorers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "competition_id", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["fussballde-amateur-stats", "fussballde-club", "fussballde-club-matches", "fussballde-club-search", "fussballde-competition-options", "fussballde-competitions", "fussballde-federation", "fussballde-filters", "fussballde-match", "fussballde-match-calendar", "fussballde-match-comparison", "fussballde-match-plan", "fussballde-matchday", "fussballde-national-top-scorers", "fussballde-news", "fussballde-news-article", "fussballde-news-search", "fussballde-player", "fussballde-player-matches", "fussballde-player-search", "fussballde-position-history", "fussballde-postal-codes", "fussballde-table", "fussballde-team", "fussballde-team-matches", "fussballde-team-squad", "fussballde-top-scorers"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-fussballde-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('amateur_stats') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-amateur-stats', params, response_type: response_type)
      end
      define_method('club') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-club', params, response_type: response_type)
      end
      define_method('club_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-club-matches', params, response_type: response_type)
      end
      define_method('club_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-club-search', params, response_type: response_type)
      end
      define_method('competition_options') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-competition-options', params, response_type: response_type)
      end
      define_method('competitions') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-competitions', params, response_type: response_type)
      end
      define_method('federation') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-federation', params, response_type: response_type)
      end
      define_method('filters') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-filters', params, response_type: response_type)
      end
      define_method('match') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-match', params, response_type: response_type)
      end
      define_method('match_calendar') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-match-calendar', params, response_type: response_type)
      end
      define_method('match_comparison') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-match-comparison', params, response_type: response_type)
      end
      define_method('match_plan') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-match-plan', params, response_type: response_type)
      end
      define_method('matchday') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-matchday', params, response_type: response_type)
      end
      define_method('national_top_scorers') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-national-top-scorers', params, response_type: response_type)
      end
      define_method('news') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-news', params, response_type: response_type)
      end
      define_method('news_article') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-news-article', params, response_type: response_type)
      end
      define_method('news_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-news-search', params, response_type: response_type)
      end
      define_method('player') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-player', params, response_type: response_type)
      end
      define_method('player_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-player-matches', params, response_type: response_type)
      end
      define_method('player_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-player-search', params, response_type: response_type)
      end
      define_method('position_history') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-position-history', params, response_type: response_type)
      end
      define_method('postal_codes') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-postal-codes', params, response_type: response_type)
      end
      define_method('table') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-table', params, response_type: response_type)
      end
      define_method('team') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-team', params, response_type: response_type)
      end
      define_method('team_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-team-matches', params, response_type: response_type)
      end
      define_method('team_squad') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-team-squad', params, response_type: response_type)
      end
      define_method('top_scorers') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fussballde-top-scorers', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
