package net.crawlora.fussballde;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the Fussball.de endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 27;
    public static final List<String> OPERATION_IDS = List.of(
            "fussballde-amateur-stats",
            "fussballde-club",
            "fussballde-club-matches",
            "fussballde-club-search",
            "fussballde-competition-options",
            "fussballde-competitions",
            "fussballde-federation",
            "fussballde-filters",
            "fussballde-match",
            "fussballde-match-calendar",
            "fussballde-match-comparison",
            "fussballde-match-plan",
            "fussballde-matchday",
            "fussballde-national-top-scorers",
            "fussballde-news",
            "fussballde-news-article",
            "fussballde-news-search",
            "fussballde-player",
            "fussballde-player-matches",
            "fussballde-player-search",
            "fussballde-position-history",
            "fussballde-postal-codes",
            "fussballde-table",
            "fussballde-team",
            "fussballde-team-matches",
            "fussballde-team-squad",
            "fussballde-top-scorers"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("fussballde-amateur-stats", new Operation("fussballde-amateur-stats", "GET", "/fussballde/amateur-stats", Map.ofEntries(Map.entry("stat", new Param("stat", "query", true, "string", List.of("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("team_type", new Param("team_type", "query", false, "string", List.of("1", "3", "6", "8", "4", "5", "7", "9"), "csv")), Map.entry("federation_id", new Param("federation_id", "query", false, "string", List.of("89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fussballde-club", new Operation("fussballde-club", "GET", "/fussballde/club", Map.ofEntries(Map.entry("club_id", new Param("club_id", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("competition_kind", new Param("competition_kind", "query", false, "string", List.of("1", "8", "3", "7", "6", "11", "2", "21", "9"), "csv"))), List.of("application/json")));
        operations.put("fussballde-club-matches", new Operation("fussballde-club-matches", "GET", "/fussballde/club-matches", Map.ofEntries(Map.entry("club_id", new Param("club_id", "query", true, "string", List.of(), "csv")), Map.entry("kind", new Param("kind", "query", false, "string", List.of("all", "next", "previous"), "csv")), Map.entry("date_from", new Param("date_from", "query", false, "string", List.of(), "csv")), Map.entry("date_to", new Param("date_to", "query", false, "string", List.of(), "csv")), Map.entry("competition_kind", new Param("competition_kind", "query", false, "string", List.of("1", "8", "3", "7", "6", "11", "2", "21", "9"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fussballde-club-search", new Operation("fussballde-club-search", "GET", "/fussballde/club-search", Map.ofEntries(Map.entry("text", new Param("text", "query", false, "string", List.of(), "csv")), Map.entry("place", new Param("place", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fussballde-competition-options", new Operation("fussballde-competition-options", "GET", "/fussballde/competition-options", Map.ofEntries(Map.entry("federation_id", new Param("federation_id", "query", true, "string", List.of("89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"), "csv")), Map.entry("season", new Param("season", "query", true, "string", List.of(), "csv")), Map.entry("competition_type", new Param("competition_type", "query", false, "string", List.of("1", "308", "300", "70", "305", "-300", "-305", "11", "2", "-2", "12"), "csv"))), List.of("application/json")));
        operations.put("fussballde-competitions", new Operation("fussballde-competitions", "GET", "/fussballde/competitions", Map.ofEntries(Map.entry("federation_id", new Param("federation_id", "query", true, "string", List.of("89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"), "csv")), Map.entry("season", new Param("season", "query", true, "string", List.of(), "csv")), Map.entry("competition_type", new Param("competition_type", "query", false, "string", List.of("1", "308", "300", "70", "305", "-300", "-305", "11", "2", "-2", "12"), "csv")), Map.entry("team_type", new Param("team_type", "query", true, "string", List.of(), "csv")), Map.entry("league", new Param("league", "query", true, "string", List.of(), "csv")), Map.entry("area", new Param("area", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fussballde-federation", new Operation("fussballde-federation", "GET", "/fussballde/federation", Map.ofEntries(Map.entry("federation_id", new Param("federation_id", "query", false, "string", List.of("89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"), "csv")), Map.entry("regional_association", new Param("regional_association", "query", false, "string", List.of("nord", "nordost", "sued", "suedwest", "west"), "csv"))), List.of("application/json")));
        operations.put("fussballde-filters", new Operation("fussballde-filters", "GET", "/fussballde/filters", Map.ofEntries(Map.entry("federation_id", new Param("federation_id", "query", false, "string", List.of("89", "32", "31", "66", "61", "02", "03", "34", "62", "23", "22", "01", "41", "43", "63", "64", "04", "33", "42", "65", "21", "35"), "csv"))), List.of("application/json")));
        operations.put("fussballde-match", new Operation("fussballde-match", "GET", "/fussballde/match", Map.ofEntries(Map.entry("match_id", new Param("match_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fussballde-match-calendar", new Operation("fussballde-match-calendar", "GET", "/fussballde/match-calendar", Map.ofEntries(Map.entry("postal_code", new Param("postal_code", "query", true, "string", List.of(), "csv")), Map.entry("date_from", new Param("date_from", "query", false, "string", List.of(), "csv")), Map.entry("date_to", new Param("date_to", "query", false, "string", List.of(), "csv")), Map.entry("team_types", new Param("team_types", "query", false, "string", List.of(), "csv")), Map.entry("competition_kind", new Param("competition_kind", "query", false, "string", List.of("1", "8", "3", "7", "6", "11", "2", "21", "9"), "csv"))), List.of("application/json")));
        operations.put("fussballde-match-comparison", new Operation("fussballde-match-comparison", "GET", "/fussballde/match-comparison", Map.ofEntries(Map.entry("match_id", new Param("match_id", "query", true, "string", List.of(), "csv")), Map.entry("view", new Param("view", "query", false, "string", List.of("history", "meetings", "season"), "csv"))), List.of("application/json")));
        operations.put("fussballde-match-plan", new Operation("fussballde-match-plan", "GET", "/fussballde/match-plan", Map.ofEntries(Map.entry("competition_id", new Param("competition_id", "query", true, "string", List.of(), "csv")), Map.entry("team_id", new Param("team_id", "query", false, "string", List.of(), "csv")), Map.entry("date_from", new Param("date_from", "query", false, "string", List.of(), "csv")), Map.entry("date_to", new Param("date_to", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fussballde-matchday", new Operation("fussballde-matchday", "GET", "/fussballde/matchday", Map.ofEntries(Map.entry("competition_id", new Param("competition_id", "query", true, "string", List.of(), "csv")), Map.entry("date", new Param("date", "query", false, "string", List.of(), "csv")), Map.entry("matchday", new Param("matchday", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fussballde-national-top-scorers", new Operation("fussballde-national-top-scorers", "GET", "/fussballde/national-top-scorers", Map.ofEntries(Map.entry("team_type", new Param("team_type", "query", false, "string", List.of("men", "women"), "csv"))), List.of("application/json")));
        operations.put("fussballde-news", new Operation("fussballde-news", "GET", "/fussballde/news", Map.ofEntries(Map.entry("stream", new Param("stream", "query", false, "string", List.of("all_news", "magazin", "regionalliga", "verbaende", "service", "aktionen", "helpcenter"), "csv")), Map.entry("regional_league", new Param("regional_league", "query", false, "string", List.of("nord", "nordost", "west", "suedwest", "bayern"), "csv")), Map.entry("help_category", new Param("help_category", "query", false, "string", List.of("allgemeines", "app", "liveticker", "mannschaftsseite", "profile", "registrierung", "training_service", "widgets"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fussballde-news-article", new Operation("fussballde-news-article", "GET", "/fussballde/news-article", Map.ofEntries(Map.entry("article_id", new Param("article_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fussballde-news-search", new Operation("fussballde-news-search", "GET", "/fussballde/news-search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("channel", new Param("channel", "query", false, "string", List.of("news", "pro_news"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fussballde-player", new Operation("fussballde-player", "GET", "/fussballde/player", Map.ofEntries(Map.entry("player_id", new Param("player_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fussballde-player-matches", new Operation("fussballde-player-matches", "GET", "/fussballde/player-matches", Map.ofEntries(Map.entry("player_id", new Param("player_id", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("team_id", new Param("team_id", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fussballde-player-search", new Operation("fussballde-player-search", "GET", "/fussballde/player-search", Map.ofEntries(Map.entry("first_name", new Param("first_name", "query", false, "string", List.of(), "csv")), Map.entry("last_name", new Param("last_name", "query", false, "string", List.of(), "csv")), Map.entry("place", new Param("place", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fussballde-position-history", new Operation("fussballde-position-history", "GET", "/fussballde/position-history", Map.ofEntries(Map.entry("competition_id", new Param("competition_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fussballde-postal-codes", new Operation("fussballde-postal-codes", "GET", "/fussballde/postal-codes", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fussballde-table", new Operation("fussballde-table", "GET", "/fussballde/table", Map.ofEntries(Map.entry("competition_id", new Param("competition_id", "query", true, "string", List.of(), "csv")), Map.entry("view", new Param("view", "query", false, "string", List.of("overall", "home_away", "rounds", "fairness", "cross"), "csv")), Map.entry("matchday", new Param("matchday", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fussballde-team", new Operation("fussballde-team", "GET", "/fussballde/team", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fussballde-team-matches", new Operation("fussballde-team-matches", "GET", "/fussballde/team-matches", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "string", List.of(), "csv")), Map.entry("kind", new Param("kind", "query", false, "string", List.of("all", "next", "previous", "wins", "draws", "losses"), "csv")), Map.entry("date_from", new Param("date_from", "query", false, "string", List.of(), "csv")), Map.entry("date_to", new Param("date_to", "query", false, "string", List.of(), "csv")), Map.entry("competition_kind", new Param("competition_kind", "query", false, "string", List.of("1", "8", "3", "7", "6", "11", "2", "21", "9"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fussballde-team-squad", new Operation("fussballde-team-squad", "GET", "/fussballde/team-squad", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("kind", new Param("kind", "query", false, "string", List.of("squad", "arrivals", "departures"), "csv"))), List.of("application/json")));
        operations.put("fussballde-top-scorers", new Operation("fussballde-top-scorers", "GET", "/fussballde/top-scorers", Map.ofEntries(Map.entry("competition_id", new Param("competition_id", "query", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown Fussball.de operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object amateurStats(Map<String, ?> params) { return request("fussballde-amateur-stats", params); }
    public Object club(Map<String, ?> params) { return request("fussballde-club", params); }
    public Object clubMatches(Map<String, ?> params) { return request("fussballde-club-matches", params); }
    public Object clubSearch(Map<String, ?> params) { return request("fussballde-club-search", params); }
    public Object competitionOptions(Map<String, ?> params) { return request("fussballde-competition-options", params); }
    public Object competitions(Map<String, ?> params) { return request("fussballde-competitions", params); }
    public Object federation(Map<String, ?> params) { return request("fussballde-federation", params); }
    public Object filters(Map<String, ?> params) { return request("fussballde-filters", params); }
    public Object match(Map<String, ?> params) { return request("fussballde-match", params); }
    public Object matchCalendar(Map<String, ?> params) { return request("fussballde-match-calendar", params); }
    public Object matchComparison(Map<String, ?> params) { return request("fussballde-match-comparison", params); }
    public Object matchPlan(Map<String, ?> params) { return request("fussballde-match-plan", params); }
    public Object matchday(Map<String, ?> params) { return request("fussballde-matchday", params); }
    public Object nationalTopScorers(Map<String, ?> params) { return request("fussballde-national-top-scorers", params); }
    public Object news(Map<String, ?> params) { return request("fussballde-news", params); }
    public Object newsArticle(Map<String, ?> params) { return request("fussballde-news-article", params); }
    public Object newsSearch(Map<String, ?> params) { return request("fussballde-news-search", params); }
    public Object player(Map<String, ?> params) { return request("fussballde-player", params); }
    public Object playerMatches(Map<String, ?> params) { return request("fussballde-player-matches", params); }
    public Object playerSearch(Map<String, ?> params) { return request("fussballde-player-search", params); }
    public Object positionHistory(Map<String, ?> params) { return request("fussballde-position-history", params); }
    public Object postalCodes(Map<String, ?> params) { return request("fussballde-postal-codes", params); }
    public Object table(Map<String, ?> params) { return request("fussballde-table", params); }
    public Object team(Map<String, ?> params) { return request("fussballde-team", params); }
    public Object teamMatches(Map<String, ?> params) { return request("fussballde-team-matches", params); }
    public Object teamSquad(Map<String, ?> params) { return request("fussballde-team-squad", params); }
    public Object topScorers(Map<String, ?> params) { return request("fussballde-top-scorers", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
