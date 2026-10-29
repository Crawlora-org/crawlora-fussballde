from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelFussballdeTopScorersResponseDoc = TypedDict('ModelFussballdeTopScorersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeTopScorersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeTopScorersResponse = TypedDict('ModelFussballdeTopScorersResponse', {
    'competition_id': NotRequired[str],
    'count': NotRequired[int],
    'final': NotRequired[bool],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'scorers': NotRequired[list[ModelFussballdeScorerRow]],
    'title': NotRequired[str],
}, total=False)

ModelFussballdeScorerRow = TypedDict('ModelFussballdeScorerRow', {
    'goals': NotRequired[int],
    'name': NotRequired[str],
    'player_id': NotRequired[str],
    'position': NotRequired[int],
    'team': NotRequired[ModelFussballdeTeamRef],
}, total=False)

ModelFussballdeTeamRef = TypedDict('ModelFussballdeTeamRef', {
    'club_id': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'team_id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFussballdeTeamSquadResponseDoc = TypedDict('ModelFussballdeTeamSquadResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeTeamSquadResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeTeamSquadResponse = TypedDict('ModelFussballdeTeamSquadResponse', {
    'columns': NotRequired[list[str]],
    'count': NotRequired[int],
    'kind': NotRequired[str],
    'players': NotRequired[list[ModelFussballdeSquadPlayer]],
    'season': NotRequired[str],
    'team_id': NotRequired[str],
}, total=False)

ModelFussballdeSquadPlayer = TypedDict('ModelFussballdeSquadPlayer', {
    'appearances': NotRequired[int],
    'cells': NotRequired[list[str]],
    'goals': NotRequired[int],
    'minutes': NotRequired[int],
    'name': NotRequired[str],
    'player_id': NotRequired[str],
}, total=False)

ModelFussballdeTeamMatchesResponseDoc = TypedDict('ModelFussballdeTeamMatchesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeTeamMatchesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeTeamMatchesResponse = TypedDict('ModelFussballdeTeamMatchesResponse', {
    'count': NotRequired[int],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'final': NotRequired[bool],
    'kind': NotRequired[str],
    'limit': NotRequired[int],
    'matches': NotRequired[list[ModelFussballdeMatchRow]],
    'offset': NotRequired[int],
    'team_id': NotRequired[str],
}, total=False)

ModelFussballdeMatchRow = TypedDict('ModelFussballdeMatchRow', {
    'away': NotRequired[ModelFussballdeTeamRef],
    'away_score': NotRequired[int],
    'competition': NotRequired[str],
    'date': NotRequired[str],
    'home': NotRequired[ModelFussballdeTeamRef],
    'home_score': NotRequired[int],
    'id': NotRequired[str],
    'league': NotRequired[str],
    'match_number': NotRequired[str],
    'note': NotRequired[str],
    'result_qualifier': NotRequired[Literal['after_extra_time', 'after_penalties', 'awarded', 'court_ruling', 'administrative_decision', 'test_match']],
    'round': NotRequired[str],
    'status': NotRequired[Literal['finished', 'scheduled', 'cancelled', 'annulled', 'abandoned', 'no_show', 'other']],
    'team_type': NotRequired[str],
    'time': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFussballdeTeamResponseDoc = TypedDict('ModelFussballdeTeamResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeTeamDetail],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeTeamDetail = TypedDict('ModelFussballdeTeamDetail', {
    'club_id': NotRequired[str],
    'club_profile': NotRequired[list[ModelFussballdeFactRow]],
    'club_url': NotRequired[str],
    'competitions': NotRequired[list[ModelFussballdeCompetitionLink]],
    'federation': NotRequired[str],
    'federation_id': NotRequired[str],
    'highest_league': NotRequired[str],
    'history': NotRequired[list[ModelFussballdeSeasonResult]],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'summary': NotRequired[list[ModelFussballdeFactRow]],
    'team_id': NotRequired[str],
    'team_type': NotRequired[str],
    'url': NotRequired[str],
    'venues': NotRequired[list[ModelFussballdeFactRow]],
}, total=False)

ModelFussballdeFactRow = TypedDict('ModelFussballdeFactRow', {
    'label': NotRequired[str],
    'url': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelFussballdeSeasonResult = TypedDict('ModelFussballdeSeasonResult', {
    'competition': NotRequired[str],
    'result': NotRequired[str],
    'season': NotRequired[str],
}, total=False)

ModelFussballdeCompetitionLink = TypedDict('ModelFussballdeCompetitionLink', {
    'id': NotRequired[str],
    'kind': NotRequired[str],
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFussballdeTableResponseDoc = TypedDict('ModelFussballdeTableResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeTableResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeTableResponse = TypedDict('ModelFussballdeTableResponse', {
    'competition_id': NotRequired[str],
    'matchday': NotRequired[int],
    'tables': NotRequired[list[ModelFussballdeStandingsTable]],
    'view': NotRequired[str],
}, total=False)

ModelFussballdeStandingsTable = TypedDict('ModelFussballdeStandingsTable', {
    'columns': NotRequired[list[str]],
    'rows': NotRequired[list[ModelFussballdeStandingsRow]],
    'title': NotRequired[str],
}, total=False)

ModelFussballdeStandingsRow = TypedDict('ModelFussballdeStandingsRow', {
    'cells': NotRequired[list[str]],
    'drawn': NotRequired[int],
    'goal_difference': NotRequired[int],
    'goals_against': NotRequired[int],
    'goals_for': NotRequired[int],
    'lost': NotRequired[int],
    'played': NotRequired[int],
    'points': NotRequired[int],
    'position': NotRequired[int],
    'team': NotRequired[ModelFussballdeTeamRef],
    'won': NotRequired[int],
}, total=False)

ModelFussballdePostalCodesResponseDoc = TypedDict('ModelFussballdePostalCodesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdePostalCodesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdePostalCodesResponse = TypedDict('ModelFussballdePostalCodesResponse', {
    'count': NotRequired[int],
    'postal_codes': NotRequired[list[ModelFussballdePostalCode]],
    'q': NotRequired[str],
}, total=False)

ModelFussballdePostalCode = TypedDict('ModelFussballdePostalCode', {
    'city': NotRequired[str],
    'district': NotRequired[str],
    'postal_code': NotRequired[str],
}, total=False)

ModelFussballdePositionHistoryResponseDoc = TypedDict('ModelFussballdePositionHistoryResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdePositionHistoryResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdePositionHistoryResponse = TypedDict('ModelFussballdePositionHistoryResponse', {
    'competition_id': NotRequired[str],
    'matchdays': NotRequired[int],
    'teams': NotRequired[list[ModelFussballdeTeamPositions]],
}, total=False)

ModelFussballdeTeamPositions = TypedDict('ModelFussballdeTeamPositions', {
    'positions': NotRequired[list[int]],
    'team': NotRequired[ModelFussballdeTeamRef],
}, total=False)

ModelFussballdePlayerSearchResponseDoc = TypedDict('ModelFussballdePlayerSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdePlayerSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdePlayerSearchResponse = TypedDict('ModelFussballdePlayerSearchResponse', {
    'count': NotRequired[int],
    'final': NotRequired[bool],
    'first_name': NotRequired[str],
    'last_name': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'place': NotRequired[str],
    'players': NotRequired[list[ModelFussballdePlayerHit]],
    'total': NotRequired[int],
}, total=False)

ModelFussballdePlayerHit = TypedDict('ModelFussballdePlayerHit', {
    'birth_date': NotRequired[str],
    'name': NotRequired[str],
    'player_id': NotRequired[str],
    'team': NotRequired[str],
    'team_type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFussballdePlayerMatchesResponseDoc = TypedDict('ModelFussballdePlayerMatchesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdePlayerMatchesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdePlayerMatchesResponse = TypedDict('ModelFussballdePlayerMatchesResponse', {
    'appearances': NotRequired[list[ModelFussballdePlayerAppearance]],
    'competition': NotRequired[str],
    'competitions': NotRequired[list[ModelFussballdeOption]],
    'count': NotRequired[int],
    'player_id': NotRequired[str],
    'season': NotRequired[str],
    'team_id': NotRequired[str],
    'teams': NotRequired[list[ModelFussballdeOption]],
}, total=False)

ModelFussballdeOption = TypedDict('ModelFussballdeOption', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelFussballdePlayerAppearance = TypedDict('ModelFussballdePlayerAppearance', {
    'goals': NotRequired[int],
    'match': NotRequired[ModelFussballdeMatchRow],
    'minutes': NotRequired[int],
    'subbed_in_minute': NotRequired[int],
    'subbed_out_minute': NotRequired[int],
}, total=False)

ModelFussballdePlayerResponseDoc = TypedDict('ModelFussballdePlayerResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdePlayerDetail],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdePlayerDetail = TypedDict('ModelFussballdePlayerDetail', {
    'birth_date': NotRequired[str],
    'facts': NotRequired[list[ModelFussballdeFactRow]],
    'name': NotRequired[str],
    'player_id': NotRequired[str],
    'profile_type': NotRequired[str],
    'stats': NotRequired[list[ModelFussballdeStatEntry]],
    'stats_season': NotRequired[str],
    'team': NotRequired[str],
    'team_id': NotRequired[str],
    'team_type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFussballdeStatEntry = TypedDict('ModelFussballdeStatEntry', {
    'label': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelFussballdeNewsSearchResponseDoc = TypedDict('ModelFussballdeNewsSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeNewsSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeNewsSearchResponse = TypedDict('ModelFussballdeNewsSearchResponse', {
    'channel': NotRequired[str],
    'count': NotRequired[int],
    'final': NotRequired[bool],
    'items': NotRequired[list[ModelFussballdeNewsItem]],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'q': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelFussballdeNewsItem = TypedDict('ModelFussballdeNewsItem', {
    'category': NotRequired[str],
    'date': NotRequired[str],
    'excerpt': NotRequired[str],
    'id': NotRequired[str],
    'time': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFussballdeNewsArticleResponseDoc = TypedDict('ModelFussballdeNewsArticleResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeNewsArticle],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeNewsArticle = TypedDict('ModelFussballdeNewsArticle', {
    'category': NotRequired[str],
    'date': NotRequired[str],
    'id': NotRequired[str],
    'image_caption': NotRequired[str],
    'image_url': NotRequired[str],
    'paragraphs': NotRequired[list[str]],
    'time': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFussballdeNewsResponseDoc = TypedDict('ModelFussballdeNewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeNewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeNewsResponse = TypedDict('ModelFussballdeNewsResponse', {
    'count': NotRequired[int],
    'final': NotRequired[bool],
    'items': NotRequired[list[ModelFussballdeNewsItem]],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'stream': NotRequired[str],
}, total=False)

ModelFussballdeNationalTopScorersResponseDoc = TypedDict('ModelFussballdeNationalTopScorersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeNationalTopScorersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeNationalTopScorersResponse = TypedDict('ModelFussballdeNationalTopScorersResponse', {
    'levels': NotRequired[list[ModelFussballdeScorerLevel]],
    'note': NotRequired[str],
    'team_type': NotRequired[str],
}, total=False)

ModelFussballdeScorerLevel = TypedDict('ModelFussballdeScorerLevel', {
    'level': NotRequired[str],
    'scorers': NotRequired[list[ModelFussballdeNationalScorer]],
}, total=False)

ModelFussballdeNationalScorer = TypedDict('ModelFussballdeNationalScorer', {
    'club': NotRequired[str],
    'club_id': NotRequired[str],
    'goals': NotRequired[int],
    'matches': NotRequired[int],
    'name': NotRequired[str],
    'player_id': NotRequired[str],
    'position': NotRequired[int],
}, total=False)

ModelFussballdeMatchdayResponseDoc = TypedDict('ModelFussballdeMatchdayResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeMatchdayResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeMatchdayResponse = TypedDict('ModelFussballdeMatchdayResponse', {
    'competition_id': NotRequired[str],
    'count': NotRequired[int],
    'date': NotRequired[str],
    'matchday': NotRequired[int],
    'matchday_count': NotRequired[int],
    'matches': NotRequired[list[ModelFussballdeMatchRow]],
    'rounds': NotRequired[list[ModelFussballdeRoundRef]],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFussballdeRoundRef = TypedDict('ModelFussballdeRoundRef', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'open': NotRequired[bool],
}, total=False)

ModelFussballdeMatchPlanResponseDoc = TypedDict('ModelFussballdeMatchPlanResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeMatchPlanResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeMatchPlanResponse = TypedDict('ModelFussballdeMatchPlanResponse', {
    'competition_id': NotRequired[str],
    'count': NotRequired[int],
    'matches': NotRequired[list[ModelFussballdeMatchRow]],
    'rounds': NotRequired[list[ModelFussballdeRoundRef]],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFussballdeMatchComparisonResponseDoc = TypedDict('ModelFussballdeMatchComparisonResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeMatchComparisonResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeMatchComparisonResponse = TypedDict('ModelFussballdeMatchComparisonResponse', {
    'match_id': NotRequired[str],
    'meetings': NotRequired[list[ModelFussballdeMatchRow]],
    'rows': NotRequired[list[ModelFussballdeComparisonRow]],
    'view': NotRequired[str],
}, total=False)

ModelFussballdeComparisonRow = TypedDict('ModelFussballdeComparisonRow', {
    'away': NotRequired[str],
    'home': NotRequired[str],
    'label': NotRequired[str],
}, total=False)

ModelFussballdeMatchCalendarResponseDoc = TypedDict('ModelFussballdeMatchCalendarResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeMatchCalendarResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeMatchCalendarResponse = TypedDict('ModelFussballdeMatchCalendarResponse', {
    'count': NotRequired[int],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'matches': NotRequired[list[ModelFussballdeMatchRow]],
    'postal_code': NotRequired[str],
    'truncated': NotRequired[bool],
}, total=False)

ModelFussballdeMatchResponseDoc = TypedDict('ModelFussballdeMatchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeMatchDetail],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeMatchDetail = TypedDict('ModelFussballdeMatchDetail', {
    'assistants': NotRequired[list[str]],
    'away': NotRequired[ModelFussballdeTeamRef],
    'away_goals': NotRequired[list[ModelFussballdeGoalEntry]],
    'away_score': NotRequired[int],
    'competition': NotRequired[str],
    'competition_id': NotRequired[str],
    'date': NotRequired[str],
    'events': NotRequired[list[ModelFussballdeMatchEvent]],
    'fourth_official': NotRequired[str],
    'halftime_score': NotRequired[str],
    'home': NotRequired[ModelFussballdeTeamRef],
    'home_goals': NotRequired[list[ModelFussballdeGoalEntry]],
    'home_score': NotRequired[int],
    'id': NotRequired[str],
    'match_number': NotRequired[str],
    'matchday': NotRequired[str],
    'note': NotRequired[str],
    'referee': NotRequired[str],
    'result_qualifier': NotRequired[Literal['after_extra_time', 'after_penalties', 'awarded', 'court_ruling', 'administrative_decision', 'test_match']],
    'spectators': NotRequired[str],
    'status': NotRequired[Literal['finished', 'scheduled', 'cancelled', 'annulled', 'abandoned', 'no_show', 'other']],
    'time': NotRequired[str],
    'url': NotRequired[str],
    'venue': NotRequired[str],
}, total=False)

ModelFussballdeGoalEntry = TypedDict('ModelFussballdeGoalEntry', {
    'minute': NotRequired[int],
    'player': NotRequired[str],
    'stoppage_minute': NotRequired[int],
}, total=False)

ModelFussballdeMatchEvent = TypedDict('ModelFussballdeMatchEvent', {
    'minute': NotRequired[int],
    'side': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelFussballdeFiltersResponseDoc = TypedDict('ModelFussballdeFiltersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeFiltersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeFiltersResponse = TypedDict('ModelFussballdeFiltersResponse', {
    'competition_types': NotRequired[dict[str, dict[str, list[ModelFussballdeOption]]]],
    'current_season': NotRequired[str],
    'default_competition_type': NotRequired[str],
    'federations': NotRequired[list[ModelFussballdeFederation]],
    'seasons': NotRequired[dict[str, list[ModelFussballdeOption]]],
}, total=False)

ModelFussballdeFederation = TypedDict('ModelFussballdeFederation', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelFussballdeFederationResponseDoc = TypedDict('ModelFussballdeFederationResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeFederationDetail],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeFederationDetail = TypedDict('ModelFussballdeFederationDetail', {
    'federation_id': NotRequired[str],
    'name': NotRequired[str],
    'news': NotRequired[list[ModelFussballdeNewsItem]],
    'profile': NotRequired[list[ModelFussballdeFactRow]],
    'regional_association': NotRequired[str],
    'summary': NotRequired[list[ModelFussballdeFactRow]],
    'url': NotRequired[str],
    'verband_id': NotRequired[str],
}, total=False)

ModelFussballdeCompetitionsResponseDoc = TypedDict('ModelFussballdeCompetitionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeCompetitionsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeCompetitionsResponse = TypedDict('ModelFussballdeCompetitionsResponse', {
    'area': NotRequired[str],
    'competition_type': NotRequired[str],
    'competitions': NotRequired[list[ModelFussballdeCompetitionRef]],
    'federation_id': NotRequired[str],
    'league': NotRequired[str],
    'season': NotRequired[str],
    'team_type': NotRequired[str],
}, total=False)

ModelFussballdeCompetitionRef = TypedDict('ModelFussballdeCompetitionRef', {
    'area_id': NotRequired[str],
    'id': NotRequired[str],
    'league_id': NotRequired[str],
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFussballdeCompetitionOptionsResponseDoc = TypedDict('ModelFussballdeCompetitionOptionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeCompetitionOptionsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeCompetitionOptionsResponse = TypedDict('ModelFussballdeCompetitionOptionsResponse', {
    'competition_type': NotRequired[str],
    'federation_id': NotRequired[str],
    'season': NotRequired[str],
    'team_types': NotRequired[list[ModelFussballdeTeamTypeOption]],
}, total=False)

ModelFussballdeTeamTypeOption = TypedDict('ModelFussballdeTeamTypeOption', {
    'id': NotRequired[str],
    'leagues': NotRequired[list[ModelFussballdeLeagueOption]],
    'name': NotRequired[str],
}, total=False)

ModelFussballdeLeagueOption = TypedDict('ModelFussballdeLeagueOption', {
    'areas': NotRequired[list[ModelFussballdeOption]],
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelFussballdeClubSearchResponseDoc = TypedDict('ModelFussballdeClubSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeClubSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeClubSearchResponse = TypedDict('ModelFussballdeClubSearchResponse', {
    'clubs': NotRequired[list[ModelFussballdeClubHit]],
    'count': NotRequired[int],
    'final': NotRequired[bool],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'place': NotRequired[str],
    'text': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelFussballdeClubHit = TypedDict('ModelFussballdeClubHit', {
    'city': NotRequired[str],
    'club_id': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'postal_code': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFussballdeClubMatchesResponseDoc = TypedDict('ModelFussballdeClubMatchesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeClubMatchesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeClubMatchesResponse = TypedDict('ModelFussballdeClubMatchesResponse', {
    'club_id': NotRequired[str],
    'count': NotRequired[int],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'final': NotRequired[bool],
    'kind': NotRequired[str],
    'limit': NotRequired[int],
    'matches': NotRequired[list[ModelFussballdeMatchRow]],
    'offset': NotRequired[int],
}, total=False)

ModelFussballdeClubResponseDoc = TypedDict('ModelFussballdeClubResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeClubDetail],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeClubDetail = TypedDict('ModelFussballdeClubDetail', {
    'club_id': NotRequired[str],
    'federation': NotRequired[str],
    'federation_id': NotRequired[str],
    'junior_team_count': NotRequired[int],
    'name': NotRequired[str],
    'profile': NotRequired[list[ModelFussballdeFactRow]],
    'season': NotRequired[str],
    'senior_team_count': NotRequired[int],
    'team_count': NotRequired[int],
    'teams': NotRequired[list[ModelFussballdeClubTeam]],
    'url': NotRequired[str],
}, total=False)

ModelFussballdeClubTeam = TypedDict('ModelFussballdeClubTeam', {
    'competition': NotRequired[str],
    'competition_id': NotRequired[str],
    'competition_type': NotRequired[str],
    'name': NotRequired[str],
    'team_id': NotRequired[str],
    'team_type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFussballdeAmateurStatsResponseDoc = TypedDict('ModelFussballdeAmateurStatsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFussballdeAmateurStatsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFussballdeAmateurStatsResponse = TypedDict('ModelFussballdeAmateurStatsResponse', {
    'count': NotRequired[int],
    'federation_id': NotRequired[str],
    'final': NotRequired[bool],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'rows': NotRequired[list[ModelFussballdeAmateurStatRow]],
    'season': NotRequired[str],
    'stat': NotRequired[str],
    'stat_name': NotRequired[str],
    'team_type': NotRequired[str],
}, total=False)

ModelFussballdeAmateurStatRow = TypedDict('ModelFussballdeAmateurStatRow', {
    'away': NotRequired[ModelFussballdeTeamRef],
    'competition_id': NotRequired[str],
    'home': NotRequired[ModelFussballdeTeamRef],
    'league': NotRequired[str],
    'match_id': NotRequired[str],
    'player': NotRequired[str],
    'player_id': NotRequired[str],
    'position': NotRequired[int],
    'result': NotRequired[str],
    'team': NotRequired[ModelFussballdeTeamRef],
    'team_type': NotRequired[str],
    'values': NotRequired[list[ModelFussballdeStatValue]],
}, total=False)

ModelFussballdeStatValue = TypedDict('ModelFussballdeStatValue', {
    'label': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

FussballdeAmateurStatsResponse = ModelFussballdeAmateurStatsResponseDoc
FussballdeAmateurStatsParams = TypedDict('FussballdeAmateurStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'stat': Required[Literal['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']],
    'season': NotRequired[str],
    'team_type': NotRequired[Literal['1', '3', '6', '8', '4', '5', '7', '9']],
    'federation_id': NotRequired[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeClubResponse = ModelFussballdeClubResponseDoc
FussballdeClubParams = TypedDict('FussballdeClubParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'club_id': Required[str],
    'season': NotRequired[str],
    'competition_kind': NotRequired[Literal['1', '8', '3', '7', '6', '11', '2', '21', '9']],
}, total=False)

FussballdeClubMatchesResponse = ModelFussballdeClubMatchesResponseDoc
FussballdeClubMatchesParams = TypedDict('FussballdeClubMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'club_id': Required[str],
    'kind': NotRequired[Literal['all', 'next', 'previous']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'competition_kind': NotRequired[Literal['1', '8', '3', '7', '6', '11', '2', '21', '9']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeClubSearchResponse = ModelFussballdeClubSearchResponseDoc
FussballdeClubSearchParams = TypedDict('FussballdeClubSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'text': NotRequired[str],
    'place': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeCompetitionOptionsResponse = ModelFussballdeCompetitionOptionsResponseDoc
FussballdeCompetitionOptionsParams = TypedDict('FussballdeCompetitionOptionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'federation_id': Required[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
    'season': Required[str],
    'competition_type': NotRequired[Literal['1', '308', '300', '70', '305', '-300', '-305', '11', '2', '-2', '12']],
}, total=False)

FussballdeCompetitionsResponse = ModelFussballdeCompetitionsResponseDoc
FussballdeCompetitionsParams = TypedDict('FussballdeCompetitionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'federation_id': Required[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
    'season': Required[str],
    'competition_type': NotRequired[Literal['1', '308', '300', '70', '305', '-300', '-305', '11', '2', '-2', '12']],
    'team_type': Required[str],
    'league': Required[str],
    'area': Required[str],
}, total=False)

FussballdeFederationResponse = ModelFussballdeFederationResponseDoc
FussballdeFederationParams = TypedDict('FussballdeFederationParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'federation_id': NotRequired[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
    'regional_association': NotRequired[Literal['nord', 'nordost', 'sued', 'suedwest', 'west']],
}, total=False)

FussballdeFiltersResponse = ModelFussballdeFiltersResponseDoc
FussballdeFiltersParams = TypedDict('FussballdeFiltersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'federation_id': NotRequired[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
}, total=False)

FussballdeMatchResponse = ModelFussballdeMatchResponseDoc
FussballdeMatchParams = TypedDict('FussballdeMatchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'match_id': Required[str],
}, total=False)

FussballdeMatchCalendarResponse = ModelFussballdeMatchCalendarResponseDoc
FussballdeMatchCalendarParams = TypedDict('FussballdeMatchCalendarParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'postal_code': Required[str],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'team_types': NotRequired[str],
    'competition_kind': NotRequired[Literal['1', '8', '3', '7', '6', '11', '2', '21', '9']],
}, total=False)

FussballdeMatchComparisonResponse = ModelFussballdeMatchComparisonResponseDoc
FussballdeMatchComparisonParams = TypedDict('FussballdeMatchComparisonParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'match_id': Required[str],
    'view': NotRequired[Literal['history', 'meetings', 'season']],
}, total=False)

FussballdeMatchPlanResponse = ModelFussballdeMatchPlanResponseDoc
FussballdeMatchPlanParams = TypedDict('FussballdeMatchPlanParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'competition_id': Required[str],
    'team_id': NotRequired[str],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

FussballdeMatchdayResponse = ModelFussballdeMatchdayResponseDoc
FussballdeMatchdayParams = TypedDict('FussballdeMatchdayParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'competition_id': Required[str],
    'date': NotRequired[str],
    'matchday': NotRequired[int],
}, total=False)

FussballdeNationalTopScorersResponse = ModelFussballdeNationalTopScorersResponseDoc
FussballdeNationalTopScorersParams = TypedDict('FussballdeNationalTopScorersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_type': NotRequired[Literal['men', 'women']],
}, total=False)

FussballdeNewsResponse = ModelFussballdeNewsResponseDoc
FussballdeNewsParams = TypedDict('FussballdeNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'stream': NotRequired[Literal['all_news', 'magazin', 'regionalliga', 'verbaende', 'service', 'aktionen', 'helpcenter']],
    'regional_league': NotRequired[Literal['nord', 'nordost', 'west', 'suedwest', 'bayern']],
    'help_category': NotRequired[Literal['allgemeines', 'app', 'liveticker', 'mannschaftsseite', 'profile', 'registrierung', 'training_service', 'widgets']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeNewsArticleResponse = ModelFussballdeNewsArticleResponseDoc
FussballdeNewsArticleParams = TypedDict('FussballdeNewsArticleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'article_id': Required[str],
}, total=False)

FussballdeNewsSearchResponse = ModelFussballdeNewsSearchResponseDoc
FussballdeNewsSearchParams = TypedDict('FussballdeNewsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'channel': NotRequired[Literal['news', 'pro_news']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdePlayerResponse = ModelFussballdePlayerResponseDoc
FussballdePlayerParams = TypedDict('FussballdePlayerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[str],
}, total=False)

FussballdePlayerMatchesResponse = ModelFussballdePlayerMatchesResponseDoc
FussballdePlayerMatchesParams = TypedDict('FussballdePlayerMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[str],
    'season': NotRequired[str],
    'team_id': NotRequired[str],
}, total=False)

FussballdePlayerSearchResponse = ModelFussballdePlayerSearchResponseDoc
FussballdePlayerSearchParams = TypedDict('FussballdePlayerSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'first_name': NotRequired[str],
    'last_name': NotRequired[str],
    'place': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdePositionHistoryResponse = ModelFussballdePositionHistoryResponseDoc
FussballdePositionHistoryParams = TypedDict('FussballdePositionHistoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'competition_id': Required[str],
}, total=False)

FussballdePostalCodesResponse = ModelFussballdePostalCodesResponseDoc
FussballdePostalCodesParams = TypedDict('FussballdePostalCodesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
}, total=False)

FussballdeTableResponse = ModelFussballdeTableResponseDoc
FussballdeTableParams = TypedDict('FussballdeTableParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'competition_id': Required[str],
    'view': NotRequired[Literal['overall', 'home_away', 'rounds', 'fairness', 'cross']],
    'matchday': NotRequired[int],
}, total=False)

FussballdeTeamResponse = ModelFussballdeTeamResponseDoc
FussballdeTeamParams = TypedDict('FussballdeTeamParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[str],
}, total=False)

FussballdeTeamMatchesResponse = ModelFussballdeTeamMatchesResponseDoc
FussballdeTeamMatchesParams = TypedDict('FussballdeTeamMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[str],
    'kind': NotRequired[Literal['all', 'next', 'previous', 'wins', 'draws', 'losses']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'competition_kind': NotRequired[Literal['1', '8', '3', '7', '6', '11', '2', '21', '9']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeTeamSquadResponse = ModelFussballdeTeamSquadResponseDoc
FussballdeTeamSquadParams = TypedDict('FussballdeTeamSquadParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[str],
    'season': NotRequired[str],
    'kind': NotRequired[Literal['squad', 'arrivals', 'departures']],
}, total=False)

FussballdeTopScorersResponse = ModelFussballdeTopScorersResponseDoc
FussballdeTopScorersParams = TypedDict('FussballdeTopScorersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'competition_id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

class FussballdeGroup:
    @overload
    def amateur_stats(self, **params: Unpack[FussballdeAmateurStatsStreamParams]) -> BinaryIO: ...
    @overload
    def amateur_stats(self, **params: Unpack[FussballdeAmateurStatsTextResponseParams]) -> str: ...
    @overload
    def amateur_stats(self, **params: Unpack[FussballdeAmateurStatsDefaultParams]) -> FussballdeAmateurStatsResponse: ...
    @overload
    def club(self, **params: Unpack[FussballdeClubStreamParams]) -> BinaryIO: ...
    @overload
    def club(self, **params: Unpack[FussballdeClubTextResponseParams]) -> str: ...
    @overload
    def club(self, **params: Unpack[FussballdeClubDefaultParams]) -> FussballdeClubResponse: ...
    @overload
    def club_matches(self, **params: Unpack[FussballdeClubMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def club_matches(self, **params: Unpack[FussballdeClubMatchesTextResponseParams]) -> str: ...
    @overload
    def club_matches(self, **params: Unpack[FussballdeClubMatchesDefaultParams]) -> FussballdeClubMatchesResponse: ...
    @overload
    def club_search(self, **params: Unpack[FussballdeClubSearchStreamParams]) -> BinaryIO: ...
    @overload
    def club_search(self, **params: Unpack[FussballdeClubSearchTextResponseParams]) -> str: ...
    @overload
    def club_search(self, **params: Unpack[FussballdeClubSearchDefaultParams]) -> FussballdeClubSearchResponse: ...
    @overload
    def competition_options(self, **params: Unpack[FussballdeCompetitionOptionsStreamParams]) -> BinaryIO: ...
    @overload
    def competition_options(self, **params: Unpack[FussballdeCompetitionOptionsTextResponseParams]) -> str: ...
    @overload
    def competition_options(self, **params: Unpack[FussballdeCompetitionOptionsDefaultParams]) -> FussballdeCompetitionOptionsResponse: ...
    @overload
    def competitions(self, **params: Unpack[FussballdeCompetitionsStreamParams]) -> BinaryIO: ...
    @overload
    def competitions(self, **params: Unpack[FussballdeCompetitionsTextResponseParams]) -> str: ...
    @overload
    def competitions(self, **params: Unpack[FussballdeCompetitionsDefaultParams]) -> FussballdeCompetitionsResponse: ...
    @overload
    def federation(self, **params: Unpack[FussballdeFederationStreamParams]) -> BinaryIO: ...
    @overload
    def federation(self, **params: Unpack[FussballdeFederationTextResponseParams]) -> str: ...
    @overload
    def federation(self, **params: Unpack[FussballdeFederationDefaultParams]) -> FussballdeFederationResponse: ...
    @overload
    def filters(self, **params: Unpack[FussballdeFiltersStreamParams]) -> BinaryIO: ...
    @overload
    def filters(self, **params: Unpack[FussballdeFiltersTextResponseParams]) -> str: ...
    @overload
    def filters(self, **params: Unpack[FussballdeFiltersDefaultParams]) -> FussballdeFiltersResponse: ...
    @overload
    def match(self, **params: Unpack[FussballdeMatchStreamParams]) -> BinaryIO: ...
    @overload
    def match(self, **params: Unpack[FussballdeMatchTextResponseParams]) -> str: ...
    @overload
    def match(self, **params: Unpack[FussballdeMatchDefaultParams]) -> FussballdeMatchResponse: ...
    @overload
    def match_calendar(self, **params: Unpack[FussballdeMatchCalendarStreamParams]) -> BinaryIO: ...
    @overload
    def match_calendar(self, **params: Unpack[FussballdeMatchCalendarTextResponseParams]) -> str: ...
    @overload
    def match_calendar(self, **params: Unpack[FussballdeMatchCalendarDefaultParams]) -> FussballdeMatchCalendarResponse: ...
    @overload
    def match_comparison(self, **params: Unpack[FussballdeMatchComparisonStreamParams]) -> BinaryIO: ...
    @overload
    def match_comparison(self, **params: Unpack[FussballdeMatchComparisonTextResponseParams]) -> str: ...
    @overload
    def match_comparison(self, **params: Unpack[FussballdeMatchComparisonDefaultParams]) -> FussballdeMatchComparisonResponse: ...
    @overload
    def match_plan(self, **params: Unpack[FussballdeMatchPlanStreamParams]) -> BinaryIO: ...
    @overload
    def match_plan(self, **params: Unpack[FussballdeMatchPlanTextResponseParams]) -> str: ...
    @overload
    def match_plan(self, **params: Unpack[FussballdeMatchPlanDefaultParams]) -> FussballdeMatchPlanResponse: ...
    @overload
    def matchday(self, **params: Unpack[FussballdeMatchdayStreamParams]) -> BinaryIO: ...
    @overload
    def matchday(self, **params: Unpack[FussballdeMatchdayTextResponseParams]) -> str: ...
    @overload
    def matchday(self, **params: Unpack[FussballdeMatchdayDefaultParams]) -> FussballdeMatchdayResponse: ...
    @overload
    def national_top_scorers(self, **params: Unpack[FussballdeNationalTopScorersStreamParams]) -> BinaryIO: ...
    @overload
    def national_top_scorers(self, **params: Unpack[FussballdeNationalTopScorersTextResponseParams]) -> str: ...
    @overload
    def national_top_scorers(self, **params: Unpack[FussballdeNationalTopScorersDefaultParams]) -> FussballdeNationalTopScorersResponse: ...
    @overload
    def news(self, **params: Unpack[FussballdeNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[FussballdeNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[FussballdeNewsDefaultParams]) -> FussballdeNewsResponse: ...
    @overload
    def news_article(self, **params: Unpack[FussballdeNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    def news_article(self, **params: Unpack[FussballdeNewsArticleTextResponseParams]) -> str: ...
    @overload
    def news_article(self, **params: Unpack[FussballdeNewsArticleDefaultParams]) -> FussballdeNewsArticleResponse: ...
    @overload
    def news_search(self, **params: Unpack[FussballdeNewsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def news_search(self, **params: Unpack[FussballdeNewsSearchTextResponseParams]) -> str: ...
    @overload
    def news_search(self, **params: Unpack[FussballdeNewsSearchDefaultParams]) -> FussballdeNewsSearchResponse: ...
    @overload
    def player(self, **params: Unpack[FussballdePlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[FussballdePlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[FussballdePlayerDefaultParams]) -> FussballdePlayerResponse: ...
    @overload
    def player_matches(self, **params: Unpack[FussballdePlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def player_matches(self, **params: Unpack[FussballdePlayerMatchesTextResponseParams]) -> str: ...
    @overload
    def player_matches(self, **params: Unpack[FussballdePlayerMatchesDefaultParams]) -> FussballdePlayerMatchesResponse: ...
    @overload
    def player_search(self, **params: Unpack[FussballdePlayerSearchStreamParams]) -> BinaryIO: ...
    @overload
    def player_search(self, **params: Unpack[FussballdePlayerSearchTextResponseParams]) -> str: ...
    @overload
    def player_search(self, **params: Unpack[FussballdePlayerSearchDefaultParams]) -> FussballdePlayerSearchResponse: ...
    @overload
    def position_history(self, **params: Unpack[FussballdePositionHistoryStreamParams]) -> BinaryIO: ...
    @overload
    def position_history(self, **params: Unpack[FussballdePositionHistoryTextResponseParams]) -> str: ...
    @overload
    def position_history(self, **params: Unpack[FussballdePositionHistoryDefaultParams]) -> FussballdePositionHistoryResponse: ...
    @overload
    def postal_codes(self, **params: Unpack[FussballdePostalCodesStreamParams]) -> BinaryIO: ...
    @overload
    def postal_codes(self, **params: Unpack[FussballdePostalCodesTextResponseParams]) -> str: ...
    @overload
    def postal_codes(self, **params: Unpack[FussballdePostalCodesDefaultParams]) -> FussballdePostalCodesResponse: ...
    @overload
    def table(self, **params: Unpack[FussballdeTableStreamParams]) -> BinaryIO: ...
    @overload
    def table(self, **params: Unpack[FussballdeTableTextResponseParams]) -> str: ...
    @overload
    def table(self, **params: Unpack[FussballdeTableDefaultParams]) -> FussballdeTableResponse: ...
    @overload
    def team(self, **params: Unpack[FussballdeTeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[FussballdeTeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[FussballdeTeamDefaultParams]) -> FussballdeTeamResponse: ...
    @overload
    def team_matches(self, **params: Unpack[FussballdeTeamMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def team_matches(self, **params: Unpack[FussballdeTeamMatchesTextResponseParams]) -> str: ...
    @overload
    def team_matches(self, **params: Unpack[FussballdeTeamMatchesDefaultParams]) -> FussballdeTeamMatchesResponse: ...
    @overload
    def team_squad(self, **params: Unpack[FussballdeTeamSquadStreamParams]) -> BinaryIO: ...
    @overload
    def team_squad(self, **params: Unpack[FussballdeTeamSquadTextResponseParams]) -> str: ...
    @overload
    def team_squad(self, **params: Unpack[FussballdeTeamSquadDefaultParams]) -> FussballdeTeamSquadResponse: ...
    @overload
    def top_scorers(self, **params: Unpack[FussballdeTopScorersStreamParams]) -> BinaryIO: ...
    @overload
    def top_scorers(self, **params: Unpack[FussballdeTopScorersTextResponseParams]) -> str: ...
    @overload
    def top_scorers(self, **params: Unpack[FussballdeTopScorersDefaultParams]) -> FussballdeTopScorersResponse: ...

OperationId = Literal[
    'fussballde-amateur-stats',
    'fussballde-club',
    'fussballde-club-matches',
    'fussballde-club-search',
    'fussballde-competition-options',
    'fussballde-competitions',
    'fussballde-federation',
    'fussballde-filters',
    'fussballde-match',
    'fussballde-match-calendar',
    'fussballde-match-comparison',
    'fussballde-match-plan',
    'fussballde-matchday',
    'fussballde-national-top-scorers',
    'fussballde-news',
    'fussballde-news-article',
    'fussballde-news-search',
    'fussballde-player',
    'fussballde-player-matches',
    'fussballde-player-search',
    'fussballde-position-history',
    'fussballde-postal-codes',
    'fussballde-table',
    'fussballde-team',
    'fussballde-team-matches',
    'fussballde-team-squad',
    'fussballde-top-scorers',
]

class CrawloraClient:
    fussballde: FussballdeGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-amateur-stats'],
        params: FussballdeAmateurStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeAmateurStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-club'],
        params: FussballdeClubParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeClubResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-club-matches'],
        params: FussballdeClubMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeClubMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-club-search'],
        params: FussballdeClubSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeClubSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-competition-options'],
        params: FussballdeCompetitionOptionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeCompetitionOptionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-competitions'],
        params: FussballdeCompetitionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeCompetitionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-federation'],
        params: FussballdeFederationParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeFederationResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-filters'],
        params: FussballdeFiltersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeFiltersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-match'],
        params: FussballdeMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeMatchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-match-calendar'],
        params: FussballdeMatchCalendarParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeMatchCalendarResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-match-comparison'],
        params: FussballdeMatchComparisonParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeMatchComparisonResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-match-plan'],
        params: FussballdeMatchPlanParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeMatchPlanResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-matchday'],
        params: FussballdeMatchdayParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeMatchdayResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-national-top-scorers'],
        params: FussballdeNationalTopScorersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeNationalTopScorersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-news'],
        params: FussballdeNewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-news-article'],
        params: FussballdeNewsArticleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeNewsArticleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-news-search'],
        params: FussballdeNewsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeNewsSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-player'],
        params: FussballdePlayerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdePlayerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-player-matches'],
        params: FussballdePlayerMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdePlayerMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-player-search'],
        params: FussballdePlayerSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdePlayerSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-position-history'],
        params: FussballdePositionHistoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdePositionHistoryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-postal-codes'],
        params: FussballdePostalCodesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdePostalCodesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-table'],
        params: FussballdeTableParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeTableResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-team'],
        params: FussballdeTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeTeamResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-team-matches'],
        params: FussballdeTeamMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeTeamMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-team-squad'],
        params: FussballdeTeamSquadParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeTeamSquadResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fussballde-top-scorers'],
        params: FussballdeTopScorersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeTopScorersResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-amateur-stats'],
        params: FussballdeAmateurStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeAmateurStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-club'],
        params: FussballdeClubParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeClubResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-club-matches'],
        params: FussballdeClubMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeClubMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-club-search'],
        params: FussballdeClubSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeClubSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-competition-options'],
        params: FussballdeCompetitionOptionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeCompetitionOptionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-competitions'],
        params: FussballdeCompetitionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeCompetitionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-federation'],
        params: FussballdeFederationParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeFederationResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-filters'],
        params: FussballdeFiltersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeFiltersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-match'],
        params: FussballdeMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeMatchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-match-calendar'],
        params: FussballdeMatchCalendarParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeMatchCalendarResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-match-comparison'],
        params: FussballdeMatchComparisonParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeMatchComparisonResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-match-plan'],
        params: FussballdeMatchPlanParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeMatchPlanResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-matchday'],
        params: FussballdeMatchdayParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeMatchdayResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-national-top-scorers'],
        params: FussballdeNationalTopScorersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeNationalTopScorersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-news'],
        params: FussballdeNewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-news-article'],
        params: FussballdeNewsArticleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeNewsArticleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-news-search'],
        params: FussballdeNewsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeNewsSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-player'],
        params: FussballdePlayerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdePlayerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-player-matches'],
        params: FussballdePlayerMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdePlayerMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-player-search'],
        params: FussballdePlayerSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdePlayerSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-position-history'],
        params: FussballdePositionHistoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdePositionHistoryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-postal-codes'],
        params: FussballdePostalCodesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdePostalCodesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-table'],
        params: FussballdeTableParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeTableResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-team'],
        params: FussballdeTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeTeamResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-team-matches'],
        params: FussballdeTeamMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeTeamMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-team-squad'],
        params: FussballdeTeamSquadParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeTeamSquadResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fussballde-top-scorers'],
        params: FussballdeTopScorersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FussballdeTopScorersResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class FussballdeClient(CrawloraClient):
    def __enter__(self) -> FussballdeClient: ...
    @overload
    def amateur_stats(self, **params: Unpack[FussballdeAmateurStatsStreamParams]) -> BinaryIO: ...
    @overload
    def amateur_stats(self, **params: Unpack[FussballdeAmateurStatsTextResponseParams]) -> str: ...
    @overload
    def amateur_stats(self, **params: Unpack[FussballdeAmateurStatsDefaultParams]) -> FussballdeAmateurStatsResponse: ...
    @overload
    def club(self, **params: Unpack[FussballdeClubStreamParams]) -> BinaryIO: ...
    @overload
    def club(self, **params: Unpack[FussballdeClubTextResponseParams]) -> str: ...
    @overload
    def club(self, **params: Unpack[FussballdeClubDefaultParams]) -> FussballdeClubResponse: ...
    @overload
    def club_matches(self, **params: Unpack[FussballdeClubMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def club_matches(self, **params: Unpack[FussballdeClubMatchesTextResponseParams]) -> str: ...
    @overload
    def club_matches(self, **params: Unpack[FussballdeClubMatchesDefaultParams]) -> FussballdeClubMatchesResponse: ...
    @overload
    def club_search(self, **params: Unpack[FussballdeClubSearchStreamParams]) -> BinaryIO: ...
    @overload
    def club_search(self, **params: Unpack[FussballdeClubSearchTextResponseParams]) -> str: ...
    @overload
    def club_search(self, **params: Unpack[FussballdeClubSearchDefaultParams]) -> FussballdeClubSearchResponse: ...
    @overload
    def competition_options(self, **params: Unpack[FussballdeCompetitionOptionsStreamParams]) -> BinaryIO: ...
    @overload
    def competition_options(self, **params: Unpack[FussballdeCompetitionOptionsTextResponseParams]) -> str: ...
    @overload
    def competition_options(self, **params: Unpack[FussballdeCompetitionOptionsDefaultParams]) -> FussballdeCompetitionOptionsResponse: ...
    @overload
    def competitions(self, **params: Unpack[FussballdeCompetitionsStreamParams]) -> BinaryIO: ...
    @overload
    def competitions(self, **params: Unpack[FussballdeCompetitionsTextResponseParams]) -> str: ...
    @overload
    def competitions(self, **params: Unpack[FussballdeCompetitionsDefaultParams]) -> FussballdeCompetitionsResponse: ...
    @overload
    def federation(self, **params: Unpack[FussballdeFederationStreamParams]) -> BinaryIO: ...
    @overload
    def federation(self, **params: Unpack[FussballdeFederationTextResponseParams]) -> str: ...
    @overload
    def federation(self, **params: Unpack[FussballdeFederationDefaultParams]) -> FussballdeFederationResponse: ...
    @overload
    def filters(self, **params: Unpack[FussballdeFiltersStreamParams]) -> BinaryIO: ...
    @overload
    def filters(self, **params: Unpack[FussballdeFiltersTextResponseParams]) -> str: ...
    @overload
    def filters(self, **params: Unpack[FussballdeFiltersDefaultParams]) -> FussballdeFiltersResponse: ...
    @overload
    def match(self, **params: Unpack[FussballdeMatchStreamParams]) -> BinaryIO: ...
    @overload
    def match(self, **params: Unpack[FussballdeMatchTextResponseParams]) -> str: ...
    @overload
    def match(self, **params: Unpack[FussballdeMatchDefaultParams]) -> FussballdeMatchResponse: ...
    @overload
    def match_calendar(self, **params: Unpack[FussballdeMatchCalendarStreamParams]) -> BinaryIO: ...
    @overload
    def match_calendar(self, **params: Unpack[FussballdeMatchCalendarTextResponseParams]) -> str: ...
    @overload
    def match_calendar(self, **params: Unpack[FussballdeMatchCalendarDefaultParams]) -> FussballdeMatchCalendarResponse: ...
    @overload
    def match_comparison(self, **params: Unpack[FussballdeMatchComparisonStreamParams]) -> BinaryIO: ...
    @overload
    def match_comparison(self, **params: Unpack[FussballdeMatchComparisonTextResponseParams]) -> str: ...
    @overload
    def match_comparison(self, **params: Unpack[FussballdeMatchComparisonDefaultParams]) -> FussballdeMatchComparisonResponse: ...
    @overload
    def match_plan(self, **params: Unpack[FussballdeMatchPlanStreamParams]) -> BinaryIO: ...
    @overload
    def match_plan(self, **params: Unpack[FussballdeMatchPlanTextResponseParams]) -> str: ...
    @overload
    def match_plan(self, **params: Unpack[FussballdeMatchPlanDefaultParams]) -> FussballdeMatchPlanResponse: ...
    @overload
    def matchday(self, **params: Unpack[FussballdeMatchdayStreamParams]) -> BinaryIO: ...
    @overload
    def matchday(self, **params: Unpack[FussballdeMatchdayTextResponseParams]) -> str: ...
    @overload
    def matchday(self, **params: Unpack[FussballdeMatchdayDefaultParams]) -> FussballdeMatchdayResponse: ...
    @overload
    def national_top_scorers(self, **params: Unpack[FussballdeNationalTopScorersStreamParams]) -> BinaryIO: ...
    @overload
    def national_top_scorers(self, **params: Unpack[FussballdeNationalTopScorersTextResponseParams]) -> str: ...
    @overload
    def national_top_scorers(self, **params: Unpack[FussballdeNationalTopScorersDefaultParams]) -> FussballdeNationalTopScorersResponse: ...
    @overload
    def news(self, **params: Unpack[FussballdeNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[FussballdeNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[FussballdeNewsDefaultParams]) -> FussballdeNewsResponse: ...
    @overload
    def news_article(self, **params: Unpack[FussballdeNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    def news_article(self, **params: Unpack[FussballdeNewsArticleTextResponseParams]) -> str: ...
    @overload
    def news_article(self, **params: Unpack[FussballdeNewsArticleDefaultParams]) -> FussballdeNewsArticleResponse: ...
    @overload
    def news_search(self, **params: Unpack[FussballdeNewsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def news_search(self, **params: Unpack[FussballdeNewsSearchTextResponseParams]) -> str: ...
    @overload
    def news_search(self, **params: Unpack[FussballdeNewsSearchDefaultParams]) -> FussballdeNewsSearchResponse: ...
    @overload
    def player(self, **params: Unpack[FussballdePlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[FussballdePlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[FussballdePlayerDefaultParams]) -> FussballdePlayerResponse: ...
    @overload
    def player_matches(self, **params: Unpack[FussballdePlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def player_matches(self, **params: Unpack[FussballdePlayerMatchesTextResponseParams]) -> str: ...
    @overload
    def player_matches(self, **params: Unpack[FussballdePlayerMatchesDefaultParams]) -> FussballdePlayerMatchesResponse: ...
    @overload
    def player_search(self, **params: Unpack[FussballdePlayerSearchStreamParams]) -> BinaryIO: ...
    @overload
    def player_search(self, **params: Unpack[FussballdePlayerSearchTextResponseParams]) -> str: ...
    @overload
    def player_search(self, **params: Unpack[FussballdePlayerSearchDefaultParams]) -> FussballdePlayerSearchResponse: ...
    @overload
    def position_history(self, **params: Unpack[FussballdePositionHistoryStreamParams]) -> BinaryIO: ...
    @overload
    def position_history(self, **params: Unpack[FussballdePositionHistoryTextResponseParams]) -> str: ...
    @overload
    def position_history(self, **params: Unpack[FussballdePositionHistoryDefaultParams]) -> FussballdePositionHistoryResponse: ...
    @overload
    def postal_codes(self, **params: Unpack[FussballdePostalCodesStreamParams]) -> BinaryIO: ...
    @overload
    def postal_codes(self, **params: Unpack[FussballdePostalCodesTextResponseParams]) -> str: ...
    @overload
    def postal_codes(self, **params: Unpack[FussballdePostalCodesDefaultParams]) -> FussballdePostalCodesResponse: ...
    @overload
    def table(self, **params: Unpack[FussballdeTableStreamParams]) -> BinaryIO: ...
    @overload
    def table(self, **params: Unpack[FussballdeTableTextResponseParams]) -> str: ...
    @overload
    def table(self, **params: Unpack[FussballdeTableDefaultParams]) -> FussballdeTableResponse: ...
    @overload
    def team(self, **params: Unpack[FussballdeTeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[FussballdeTeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[FussballdeTeamDefaultParams]) -> FussballdeTeamResponse: ...
    @overload
    def team_matches(self, **params: Unpack[FussballdeTeamMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def team_matches(self, **params: Unpack[FussballdeTeamMatchesTextResponseParams]) -> str: ...
    @overload
    def team_matches(self, **params: Unpack[FussballdeTeamMatchesDefaultParams]) -> FussballdeTeamMatchesResponse: ...
    @overload
    def team_squad(self, **params: Unpack[FussballdeTeamSquadStreamParams]) -> BinaryIO: ...
    @overload
    def team_squad(self, **params: Unpack[FussballdeTeamSquadTextResponseParams]) -> str: ...
    @overload
    def team_squad(self, **params: Unpack[FussballdeTeamSquadDefaultParams]) -> FussballdeTeamSquadResponse: ...
    @overload
    def top_scorers(self, **params: Unpack[FussballdeTopScorersStreamParams]) -> BinaryIO: ...
    @overload
    def top_scorers(self, **params: Unpack[FussballdeTopScorersTextResponseParams]) -> str: ...
    @overload
    def top_scorers(self, **params: Unpack[FussballdeTopScorersDefaultParams]) -> FussballdeTopScorersResponse: ...

class AsyncFussballdeClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncFussballdeClient: ...
    fussballde: _AsyncFussballdeGroup
    @overload
    async def amateur_stats(self, **params: Unpack[FussballdeAmateurStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def amateur_stats(self, **params: Unpack[FussballdeAmateurStatsTextResponseParams]) -> str: ...
    @overload
    async def amateur_stats(self, **params: Unpack[FussballdeAmateurStatsDefaultParams]) -> FussballdeAmateurStatsResponse: ...
    @overload
    async def club(self, **params: Unpack[FussballdeClubStreamParams]) -> BinaryIO: ...
    @overload
    async def club(self, **params: Unpack[FussballdeClubTextResponseParams]) -> str: ...
    @overload
    async def club(self, **params: Unpack[FussballdeClubDefaultParams]) -> FussballdeClubResponse: ...
    @overload
    async def club_matches(self, **params: Unpack[FussballdeClubMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def club_matches(self, **params: Unpack[FussballdeClubMatchesTextResponseParams]) -> str: ...
    @overload
    async def club_matches(self, **params: Unpack[FussballdeClubMatchesDefaultParams]) -> FussballdeClubMatchesResponse: ...
    @overload
    async def club_search(self, **params: Unpack[FussballdeClubSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def club_search(self, **params: Unpack[FussballdeClubSearchTextResponseParams]) -> str: ...
    @overload
    async def club_search(self, **params: Unpack[FussballdeClubSearchDefaultParams]) -> FussballdeClubSearchResponse: ...
    @overload
    async def competition_options(self, **params: Unpack[FussballdeCompetitionOptionsStreamParams]) -> BinaryIO: ...
    @overload
    async def competition_options(self, **params: Unpack[FussballdeCompetitionOptionsTextResponseParams]) -> str: ...
    @overload
    async def competition_options(self, **params: Unpack[FussballdeCompetitionOptionsDefaultParams]) -> FussballdeCompetitionOptionsResponse: ...
    @overload
    async def competitions(self, **params: Unpack[FussballdeCompetitionsStreamParams]) -> BinaryIO: ...
    @overload
    async def competitions(self, **params: Unpack[FussballdeCompetitionsTextResponseParams]) -> str: ...
    @overload
    async def competitions(self, **params: Unpack[FussballdeCompetitionsDefaultParams]) -> FussballdeCompetitionsResponse: ...
    @overload
    async def federation(self, **params: Unpack[FussballdeFederationStreamParams]) -> BinaryIO: ...
    @overload
    async def federation(self, **params: Unpack[FussballdeFederationTextResponseParams]) -> str: ...
    @overload
    async def federation(self, **params: Unpack[FussballdeFederationDefaultParams]) -> FussballdeFederationResponse: ...
    @overload
    async def filters(self, **params: Unpack[FussballdeFiltersStreamParams]) -> BinaryIO: ...
    @overload
    async def filters(self, **params: Unpack[FussballdeFiltersTextResponseParams]) -> str: ...
    @overload
    async def filters(self, **params: Unpack[FussballdeFiltersDefaultParams]) -> FussballdeFiltersResponse: ...
    @overload
    async def match(self, **params: Unpack[FussballdeMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def match(self, **params: Unpack[FussballdeMatchTextResponseParams]) -> str: ...
    @overload
    async def match(self, **params: Unpack[FussballdeMatchDefaultParams]) -> FussballdeMatchResponse: ...
    @overload
    async def match_calendar(self, **params: Unpack[FussballdeMatchCalendarStreamParams]) -> BinaryIO: ...
    @overload
    async def match_calendar(self, **params: Unpack[FussballdeMatchCalendarTextResponseParams]) -> str: ...
    @overload
    async def match_calendar(self, **params: Unpack[FussballdeMatchCalendarDefaultParams]) -> FussballdeMatchCalendarResponse: ...
    @overload
    async def match_comparison(self, **params: Unpack[FussballdeMatchComparisonStreamParams]) -> BinaryIO: ...
    @overload
    async def match_comparison(self, **params: Unpack[FussballdeMatchComparisonTextResponseParams]) -> str: ...
    @overload
    async def match_comparison(self, **params: Unpack[FussballdeMatchComparisonDefaultParams]) -> FussballdeMatchComparisonResponse: ...
    @overload
    async def match_plan(self, **params: Unpack[FussballdeMatchPlanStreamParams]) -> BinaryIO: ...
    @overload
    async def match_plan(self, **params: Unpack[FussballdeMatchPlanTextResponseParams]) -> str: ...
    @overload
    async def match_plan(self, **params: Unpack[FussballdeMatchPlanDefaultParams]) -> FussballdeMatchPlanResponse: ...
    @overload
    async def matchday(self, **params: Unpack[FussballdeMatchdayStreamParams]) -> BinaryIO: ...
    @overload
    async def matchday(self, **params: Unpack[FussballdeMatchdayTextResponseParams]) -> str: ...
    @overload
    async def matchday(self, **params: Unpack[FussballdeMatchdayDefaultParams]) -> FussballdeMatchdayResponse: ...
    @overload
    async def national_top_scorers(self, **params: Unpack[FussballdeNationalTopScorersStreamParams]) -> BinaryIO: ...
    @overload
    async def national_top_scorers(self, **params: Unpack[FussballdeNationalTopScorersTextResponseParams]) -> str: ...
    @overload
    async def national_top_scorers(self, **params: Unpack[FussballdeNationalTopScorersDefaultParams]) -> FussballdeNationalTopScorersResponse: ...
    @overload
    async def news(self, **params: Unpack[FussballdeNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[FussballdeNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[FussballdeNewsDefaultParams]) -> FussballdeNewsResponse: ...
    @overload
    async def news_article(self, **params: Unpack[FussballdeNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    async def news_article(self, **params: Unpack[FussballdeNewsArticleTextResponseParams]) -> str: ...
    @overload
    async def news_article(self, **params: Unpack[FussballdeNewsArticleDefaultParams]) -> FussballdeNewsArticleResponse: ...
    @overload
    async def news_search(self, **params: Unpack[FussballdeNewsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def news_search(self, **params: Unpack[FussballdeNewsSearchTextResponseParams]) -> str: ...
    @overload
    async def news_search(self, **params: Unpack[FussballdeNewsSearchDefaultParams]) -> FussballdeNewsSearchResponse: ...
    @overload
    async def player(self, **params: Unpack[FussballdePlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[FussballdePlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[FussballdePlayerDefaultParams]) -> FussballdePlayerResponse: ...
    @overload
    async def player_matches(self, **params: Unpack[FussballdePlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_matches(self, **params: Unpack[FussballdePlayerMatchesTextResponseParams]) -> str: ...
    @overload
    async def player_matches(self, **params: Unpack[FussballdePlayerMatchesDefaultParams]) -> FussballdePlayerMatchesResponse: ...
    @overload
    async def player_search(self, **params: Unpack[FussballdePlayerSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def player_search(self, **params: Unpack[FussballdePlayerSearchTextResponseParams]) -> str: ...
    @overload
    async def player_search(self, **params: Unpack[FussballdePlayerSearchDefaultParams]) -> FussballdePlayerSearchResponse: ...
    @overload
    async def position_history(self, **params: Unpack[FussballdePositionHistoryStreamParams]) -> BinaryIO: ...
    @overload
    async def position_history(self, **params: Unpack[FussballdePositionHistoryTextResponseParams]) -> str: ...
    @overload
    async def position_history(self, **params: Unpack[FussballdePositionHistoryDefaultParams]) -> FussballdePositionHistoryResponse: ...
    @overload
    async def postal_codes(self, **params: Unpack[FussballdePostalCodesStreamParams]) -> BinaryIO: ...
    @overload
    async def postal_codes(self, **params: Unpack[FussballdePostalCodesTextResponseParams]) -> str: ...
    @overload
    async def postal_codes(self, **params: Unpack[FussballdePostalCodesDefaultParams]) -> FussballdePostalCodesResponse: ...
    @overload
    async def table(self, **params: Unpack[FussballdeTableStreamParams]) -> BinaryIO: ...
    @overload
    async def table(self, **params: Unpack[FussballdeTableTextResponseParams]) -> str: ...
    @overload
    async def table(self, **params: Unpack[FussballdeTableDefaultParams]) -> FussballdeTableResponse: ...
    @overload
    async def team(self, **params: Unpack[FussballdeTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[FussballdeTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[FussballdeTeamDefaultParams]) -> FussballdeTeamResponse: ...
    @overload
    async def team_matches(self, **params: Unpack[FussballdeTeamMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_matches(self, **params: Unpack[FussballdeTeamMatchesTextResponseParams]) -> str: ...
    @overload
    async def team_matches(self, **params: Unpack[FussballdeTeamMatchesDefaultParams]) -> FussballdeTeamMatchesResponse: ...
    @overload
    async def team_squad(self, **params: Unpack[FussballdeTeamSquadStreamParams]) -> BinaryIO: ...
    @overload
    async def team_squad(self, **params: Unpack[FussballdeTeamSquadTextResponseParams]) -> str: ...
    @overload
    async def team_squad(self, **params: Unpack[FussballdeTeamSquadDefaultParams]) -> FussballdeTeamSquadResponse: ...
    @overload
    async def top_scorers(self, **params: Unpack[FussballdeTopScorersStreamParams]) -> BinaryIO: ...
    @overload
    async def top_scorers(self, **params: Unpack[FussballdeTopScorersTextResponseParams]) -> str: ...
    @overload
    async def top_scorers(self, **params: Unpack[FussballdeTopScorersDefaultParams]) -> FussballdeTopScorersResponse: ...

class _AsyncFussballdeGroup:
    @overload
    async def amateur_stats(self, **params: Unpack[FussballdeAmateurStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def amateur_stats(self, **params: Unpack[FussballdeAmateurStatsTextResponseParams]) -> str: ...
    @overload
    async def amateur_stats(self, **params: Unpack[FussballdeAmateurStatsDefaultParams]) -> FussballdeAmateurStatsResponse: ...
    @overload
    async def club(self, **params: Unpack[FussballdeClubStreamParams]) -> BinaryIO: ...
    @overload
    async def club(self, **params: Unpack[FussballdeClubTextResponseParams]) -> str: ...
    @overload
    async def club(self, **params: Unpack[FussballdeClubDefaultParams]) -> FussballdeClubResponse: ...
    @overload
    async def club_matches(self, **params: Unpack[FussballdeClubMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def club_matches(self, **params: Unpack[FussballdeClubMatchesTextResponseParams]) -> str: ...
    @overload
    async def club_matches(self, **params: Unpack[FussballdeClubMatchesDefaultParams]) -> FussballdeClubMatchesResponse: ...
    @overload
    async def club_search(self, **params: Unpack[FussballdeClubSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def club_search(self, **params: Unpack[FussballdeClubSearchTextResponseParams]) -> str: ...
    @overload
    async def club_search(self, **params: Unpack[FussballdeClubSearchDefaultParams]) -> FussballdeClubSearchResponse: ...
    @overload
    async def competition_options(self, **params: Unpack[FussballdeCompetitionOptionsStreamParams]) -> BinaryIO: ...
    @overload
    async def competition_options(self, **params: Unpack[FussballdeCompetitionOptionsTextResponseParams]) -> str: ...
    @overload
    async def competition_options(self, **params: Unpack[FussballdeCompetitionOptionsDefaultParams]) -> FussballdeCompetitionOptionsResponse: ...
    @overload
    async def competitions(self, **params: Unpack[FussballdeCompetitionsStreamParams]) -> BinaryIO: ...
    @overload
    async def competitions(self, **params: Unpack[FussballdeCompetitionsTextResponseParams]) -> str: ...
    @overload
    async def competitions(self, **params: Unpack[FussballdeCompetitionsDefaultParams]) -> FussballdeCompetitionsResponse: ...
    @overload
    async def federation(self, **params: Unpack[FussballdeFederationStreamParams]) -> BinaryIO: ...
    @overload
    async def federation(self, **params: Unpack[FussballdeFederationTextResponseParams]) -> str: ...
    @overload
    async def federation(self, **params: Unpack[FussballdeFederationDefaultParams]) -> FussballdeFederationResponse: ...
    @overload
    async def filters(self, **params: Unpack[FussballdeFiltersStreamParams]) -> BinaryIO: ...
    @overload
    async def filters(self, **params: Unpack[FussballdeFiltersTextResponseParams]) -> str: ...
    @overload
    async def filters(self, **params: Unpack[FussballdeFiltersDefaultParams]) -> FussballdeFiltersResponse: ...
    @overload
    async def match(self, **params: Unpack[FussballdeMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def match(self, **params: Unpack[FussballdeMatchTextResponseParams]) -> str: ...
    @overload
    async def match(self, **params: Unpack[FussballdeMatchDefaultParams]) -> FussballdeMatchResponse: ...
    @overload
    async def match_calendar(self, **params: Unpack[FussballdeMatchCalendarStreamParams]) -> BinaryIO: ...
    @overload
    async def match_calendar(self, **params: Unpack[FussballdeMatchCalendarTextResponseParams]) -> str: ...
    @overload
    async def match_calendar(self, **params: Unpack[FussballdeMatchCalendarDefaultParams]) -> FussballdeMatchCalendarResponse: ...
    @overload
    async def match_comparison(self, **params: Unpack[FussballdeMatchComparisonStreamParams]) -> BinaryIO: ...
    @overload
    async def match_comparison(self, **params: Unpack[FussballdeMatchComparisonTextResponseParams]) -> str: ...
    @overload
    async def match_comparison(self, **params: Unpack[FussballdeMatchComparisonDefaultParams]) -> FussballdeMatchComparisonResponse: ...
    @overload
    async def match_plan(self, **params: Unpack[FussballdeMatchPlanStreamParams]) -> BinaryIO: ...
    @overload
    async def match_plan(self, **params: Unpack[FussballdeMatchPlanTextResponseParams]) -> str: ...
    @overload
    async def match_plan(self, **params: Unpack[FussballdeMatchPlanDefaultParams]) -> FussballdeMatchPlanResponse: ...
    @overload
    async def matchday(self, **params: Unpack[FussballdeMatchdayStreamParams]) -> BinaryIO: ...
    @overload
    async def matchday(self, **params: Unpack[FussballdeMatchdayTextResponseParams]) -> str: ...
    @overload
    async def matchday(self, **params: Unpack[FussballdeMatchdayDefaultParams]) -> FussballdeMatchdayResponse: ...
    @overload
    async def national_top_scorers(self, **params: Unpack[FussballdeNationalTopScorersStreamParams]) -> BinaryIO: ...
    @overload
    async def national_top_scorers(self, **params: Unpack[FussballdeNationalTopScorersTextResponseParams]) -> str: ...
    @overload
    async def national_top_scorers(self, **params: Unpack[FussballdeNationalTopScorersDefaultParams]) -> FussballdeNationalTopScorersResponse: ...
    @overload
    async def news(self, **params: Unpack[FussballdeNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[FussballdeNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[FussballdeNewsDefaultParams]) -> FussballdeNewsResponse: ...
    @overload
    async def news_article(self, **params: Unpack[FussballdeNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    async def news_article(self, **params: Unpack[FussballdeNewsArticleTextResponseParams]) -> str: ...
    @overload
    async def news_article(self, **params: Unpack[FussballdeNewsArticleDefaultParams]) -> FussballdeNewsArticleResponse: ...
    @overload
    async def news_search(self, **params: Unpack[FussballdeNewsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def news_search(self, **params: Unpack[FussballdeNewsSearchTextResponseParams]) -> str: ...
    @overload
    async def news_search(self, **params: Unpack[FussballdeNewsSearchDefaultParams]) -> FussballdeNewsSearchResponse: ...
    @overload
    async def player(self, **params: Unpack[FussballdePlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[FussballdePlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[FussballdePlayerDefaultParams]) -> FussballdePlayerResponse: ...
    @overload
    async def player_matches(self, **params: Unpack[FussballdePlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_matches(self, **params: Unpack[FussballdePlayerMatchesTextResponseParams]) -> str: ...
    @overload
    async def player_matches(self, **params: Unpack[FussballdePlayerMatchesDefaultParams]) -> FussballdePlayerMatchesResponse: ...
    @overload
    async def player_search(self, **params: Unpack[FussballdePlayerSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def player_search(self, **params: Unpack[FussballdePlayerSearchTextResponseParams]) -> str: ...
    @overload
    async def player_search(self, **params: Unpack[FussballdePlayerSearchDefaultParams]) -> FussballdePlayerSearchResponse: ...
    @overload
    async def position_history(self, **params: Unpack[FussballdePositionHistoryStreamParams]) -> BinaryIO: ...
    @overload
    async def position_history(self, **params: Unpack[FussballdePositionHistoryTextResponseParams]) -> str: ...
    @overload
    async def position_history(self, **params: Unpack[FussballdePositionHistoryDefaultParams]) -> FussballdePositionHistoryResponse: ...
    @overload
    async def postal_codes(self, **params: Unpack[FussballdePostalCodesStreamParams]) -> BinaryIO: ...
    @overload
    async def postal_codes(self, **params: Unpack[FussballdePostalCodesTextResponseParams]) -> str: ...
    @overload
    async def postal_codes(self, **params: Unpack[FussballdePostalCodesDefaultParams]) -> FussballdePostalCodesResponse: ...
    @overload
    async def table(self, **params: Unpack[FussballdeTableStreamParams]) -> BinaryIO: ...
    @overload
    async def table(self, **params: Unpack[FussballdeTableTextResponseParams]) -> str: ...
    @overload
    async def table(self, **params: Unpack[FussballdeTableDefaultParams]) -> FussballdeTableResponse: ...
    @overload
    async def team(self, **params: Unpack[FussballdeTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[FussballdeTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[FussballdeTeamDefaultParams]) -> FussballdeTeamResponse: ...
    @overload
    async def team_matches(self, **params: Unpack[FussballdeTeamMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_matches(self, **params: Unpack[FussballdeTeamMatchesTextResponseParams]) -> str: ...
    @overload
    async def team_matches(self, **params: Unpack[FussballdeTeamMatchesDefaultParams]) -> FussballdeTeamMatchesResponse: ...
    @overload
    async def team_squad(self, **params: Unpack[FussballdeTeamSquadStreamParams]) -> BinaryIO: ...
    @overload
    async def team_squad(self, **params: Unpack[FussballdeTeamSquadTextResponseParams]) -> str: ...
    @overload
    async def team_squad(self, **params: Unpack[FussballdeTeamSquadDefaultParams]) -> FussballdeTeamSquadResponse: ...
    @overload
    async def top_scorers(self, **params: Unpack[FussballdeTopScorersStreamParams]) -> BinaryIO: ...
    @overload
    async def top_scorers(self, **params: Unpack[FussballdeTopScorersTextResponseParams]) -> str: ...
    @overload
    async def top_scorers(self, **params: Unpack[FussballdeTopScorersDefaultParams]) -> FussballdeTopScorersResponse: ...

FussballdeAmateurStatsDefaultParams = TypedDict('FussballdeAmateurStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'stat': Required[Literal['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']],
    'season': NotRequired[str],
    'team_type': NotRequired[Literal['1', '3', '6', '8', '4', '5', '7', '9']],
    'federation_id': NotRequired[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeAmateurStatsTextResponseParams = TypedDict('FussballdeAmateurStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'stat': Required[Literal['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']],
    'season': NotRequired[str],
    'team_type': NotRequired[Literal['1', '3', '6', '8', '4', '5', '7', '9']],
    'federation_id': NotRequired[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeAmateurStatsStreamParams = TypedDict('FussballdeAmateurStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'stat': Required[Literal['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']],
    'season': NotRequired[str],
    'team_type': NotRequired[Literal['1', '3', '6', '8', '4', '5', '7', '9']],
    'federation_id': NotRequired[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeClubDefaultParams = TypedDict('FussballdeClubDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'club_id': Required[str],
    'season': NotRequired[str],
    'competition_kind': NotRequired[Literal['1', '8', '3', '7', '6', '11', '2', '21', '9']],
}, total=False)

FussballdeClubTextResponseParams = TypedDict('FussballdeClubTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'club_id': Required[str],
    'season': NotRequired[str],
    'competition_kind': NotRequired[Literal['1', '8', '3', '7', '6', '11', '2', '21', '9']],
}, total=False)

FussballdeClubStreamParams = TypedDict('FussballdeClubStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'club_id': Required[str],
    'season': NotRequired[str],
    'competition_kind': NotRequired[Literal['1', '8', '3', '7', '6', '11', '2', '21', '9']],
}, total=False)

FussballdeClubMatchesDefaultParams = TypedDict('FussballdeClubMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'club_id': Required[str],
    'kind': NotRequired[Literal['all', 'next', 'previous']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'competition_kind': NotRequired[Literal['1', '8', '3', '7', '6', '11', '2', '21', '9']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeClubMatchesTextResponseParams = TypedDict('FussballdeClubMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'club_id': Required[str],
    'kind': NotRequired[Literal['all', 'next', 'previous']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'competition_kind': NotRequired[Literal['1', '8', '3', '7', '6', '11', '2', '21', '9']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeClubMatchesStreamParams = TypedDict('FussballdeClubMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'club_id': Required[str],
    'kind': NotRequired[Literal['all', 'next', 'previous']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'competition_kind': NotRequired[Literal['1', '8', '3', '7', '6', '11', '2', '21', '9']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeClubSearchDefaultParams = TypedDict('FussballdeClubSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'text': NotRequired[str],
    'place': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeClubSearchTextResponseParams = TypedDict('FussballdeClubSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'text': NotRequired[str],
    'place': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeClubSearchStreamParams = TypedDict('FussballdeClubSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'text': NotRequired[str],
    'place': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeCompetitionOptionsDefaultParams = TypedDict('FussballdeCompetitionOptionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'federation_id': Required[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
    'season': Required[str],
    'competition_type': NotRequired[Literal['1', '308', '300', '70', '305', '-300', '-305', '11', '2', '-2', '12']],
}, total=False)

FussballdeCompetitionOptionsTextResponseParams = TypedDict('FussballdeCompetitionOptionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'federation_id': Required[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
    'season': Required[str],
    'competition_type': NotRequired[Literal['1', '308', '300', '70', '305', '-300', '-305', '11', '2', '-2', '12']],
}, total=False)

FussballdeCompetitionOptionsStreamParams = TypedDict('FussballdeCompetitionOptionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'federation_id': Required[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
    'season': Required[str],
    'competition_type': NotRequired[Literal['1', '308', '300', '70', '305', '-300', '-305', '11', '2', '-2', '12']],
}, total=False)

FussballdeCompetitionsDefaultParams = TypedDict('FussballdeCompetitionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'federation_id': Required[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
    'season': Required[str],
    'competition_type': NotRequired[Literal['1', '308', '300', '70', '305', '-300', '-305', '11', '2', '-2', '12']],
    'team_type': Required[str],
    'league': Required[str],
    'area': Required[str],
}, total=False)

FussballdeCompetitionsTextResponseParams = TypedDict('FussballdeCompetitionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'federation_id': Required[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
    'season': Required[str],
    'competition_type': NotRequired[Literal['1', '308', '300', '70', '305', '-300', '-305', '11', '2', '-2', '12']],
    'team_type': Required[str],
    'league': Required[str],
    'area': Required[str],
}, total=False)

FussballdeCompetitionsStreamParams = TypedDict('FussballdeCompetitionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'federation_id': Required[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
    'season': Required[str],
    'competition_type': NotRequired[Literal['1', '308', '300', '70', '305', '-300', '-305', '11', '2', '-2', '12']],
    'team_type': Required[str],
    'league': Required[str],
    'area': Required[str],
}, total=False)

FussballdeFederationDefaultParams = TypedDict('FussballdeFederationDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'federation_id': NotRequired[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
    'regional_association': NotRequired[Literal['nord', 'nordost', 'sued', 'suedwest', 'west']],
}, total=False)

FussballdeFederationTextResponseParams = TypedDict('FussballdeFederationTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'federation_id': NotRequired[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
    'regional_association': NotRequired[Literal['nord', 'nordost', 'sued', 'suedwest', 'west']],
}, total=False)

FussballdeFederationStreamParams = TypedDict('FussballdeFederationStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'federation_id': NotRequired[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
    'regional_association': NotRequired[Literal['nord', 'nordost', 'sued', 'suedwest', 'west']],
}, total=False)

FussballdeFiltersDefaultParams = TypedDict('FussballdeFiltersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'federation_id': NotRequired[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
}, total=False)

FussballdeFiltersTextResponseParams = TypedDict('FussballdeFiltersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'federation_id': NotRequired[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
}, total=False)

FussballdeFiltersStreamParams = TypedDict('FussballdeFiltersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'federation_id': NotRequired[Literal['89', '32', '31', '66', '61', '02', '03', '34', '62', '23', '22', '01', '41', '43', '63', '64', '04', '33', '42', '65', '21', '35']],
}, total=False)

FussballdeMatchDefaultParams = TypedDict('FussballdeMatchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'match_id': Required[str],
}, total=False)

FussballdeMatchTextResponseParams = TypedDict('FussballdeMatchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'match_id': Required[str],
}, total=False)

FussballdeMatchStreamParams = TypedDict('FussballdeMatchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'match_id': Required[str],
}, total=False)

FussballdeMatchCalendarDefaultParams = TypedDict('FussballdeMatchCalendarDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'postal_code': Required[str],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'team_types': NotRequired[str],
    'competition_kind': NotRequired[Literal['1', '8', '3', '7', '6', '11', '2', '21', '9']],
}, total=False)

FussballdeMatchCalendarTextResponseParams = TypedDict('FussballdeMatchCalendarTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'postal_code': Required[str],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'team_types': NotRequired[str],
    'competition_kind': NotRequired[Literal['1', '8', '3', '7', '6', '11', '2', '21', '9']],
}, total=False)

FussballdeMatchCalendarStreamParams = TypedDict('FussballdeMatchCalendarStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'postal_code': Required[str],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'team_types': NotRequired[str],
    'competition_kind': NotRequired[Literal['1', '8', '3', '7', '6', '11', '2', '21', '9']],
}, total=False)

FussballdeMatchComparisonDefaultParams = TypedDict('FussballdeMatchComparisonDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'match_id': Required[str],
    'view': NotRequired[Literal['history', 'meetings', 'season']],
}, total=False)

FussballdeMatchComparisonTextResponseParams = TypedDict('FussballdeMatchComparisonTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'match_id': Required[str],
    'view': NotRequired[Literal['history', 'meetings', 'season']],
}, total=False)

FussballdeMatchComparisonStreamParams = TypedDict('FussballdeMatchComparisonStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'match_id': Required[str],
    'view': NotRequired[Literal['history', 'meetings', 'season']],
}, total=False)

FussballdeMatchPlanDefaultParams = TypedDict('FussballdeMatchPlanDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'competition_id': Required[str],
    'team_id': NotRequired[str],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

FussballdeMatchPlanTextResponseParams = TypedDict('FussballdeMatchPlanTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'competition_id': Required[str],
    'team_id': NotRequired[str],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

FussballdeMatchPlanStreamParams = TypedDict('FussballdeMatchPlanStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'competition_id': Required[str],
    'team_id': NotRequired[str],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

FussballdeMatchdayDefaultParams = TypedDict('FussballdeMatchdayDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'competition_id': Required[str],
    'date': NotRequired[str],
    'matchday': NotRequired[int],
}, total=False)

FussballdeMatchdayTextResponseParams = TypedDict('FussballdeMatchdayTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'competition_id': Required[str],
    'date': NotRequired[str],
    'matchday': NotRequired[int],
}, total=False)

FussballdeMatchdayStreamParams = TypedDict('FussballdeMatchdayStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'competition_id': Required[str],
    'date': NotRequired[str],
    'matchday': NotRequired[int],
}, total=False)

FussballdeNationalTopScorersDefaultParams = TypedDict('FussballdeNationalTopScorersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_type': NotRequired[Literal['men', 'women']],
}, total=False)

FussballdeNationalTopScorersTextResponseParams = TypedDict('FussballdeNationalTopScorersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_type': NotRequired[Literal['men', 'women']],
}, total=False)

FussballdeNationalTopScorersStreamParams = TypedDict('FussballdeNationalTopScorersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_type': NotRequired[Literal['men', 'women']],
}, total=False)

FussballdeNewsDefaultParams = TypedDict('FussballdeNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'stream': NotRequired[Literal['all_news', 'magazin', 'regionalliga', 'verbaende', 'service', 'aktionen', 'helpcenter']],
    'regional_league': NotRequired[Literal['nord', 'nordost', 'west', 'suedwest', 'bayern']],
    'help_category': NotRequired[Literal['allgemeines', 'app', 'liveticker', 'mannschaftsseite', 'profile', 'registrierung', 'training_service', 'widgets']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeNewsTextResponseParams = TypedDict('FussballdeNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'stream': NotRequired[Literal['all_news', 'magazin', 'regionalliga', 'verbaende', 'service', 'aktionen', 'helpcenter']],
    'regional_league': NotRequired[Literal['nord', 'nordost', 'west', 'suedwest', 'bayern']],
    'help_category': NotRequired[Literal['allgemeines', 'app', 'liveticker', 'mannschaftsseite', 'profile', 'registrierung', 'training_service', 'widgets']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeNewsStreamParams = TypedDict('FussballdeNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'stream': NotRequired[Literal['all_news', 'magazin', 'regionalliga', 'verbaende', 'service', 'aktionen', 'helpcenter']],
    'regional_league': NotRequired[Literal['nord', 'nordost', 'west', 'suedwest', 'bayern']],
    'help_category': NotRequired[Literal['allgemeines', 'app', 'liveticker', 'mannschaftsseite', 'profile', 'registrierung', 'training_service', 'widgets']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeNewsArticleDefaultParams = TypedDict('FussballdeNewsArticleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'article_id': Required[str],
}, total=False)

FussballdeNewsArticleTextResponseParams = TypedDict('FussballdeNewsArticleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'article_id': Required[str],
}, total=False)

FussballdeNewsArticleStreamParams = TypedDict('FussballdeNewsArticleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'article_id': Required[str],
}, total=False)

FussballdeNewsSearchDefaultParams = TypedDict('FussballdeNewsSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'channel': NotRequired[Literal['news', 'pro_news']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeNewsSearchTextResponseParams = TypedDict('FussballdeNewsSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'channel': NotRequired[Literal['news', 'pro_news']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeNewsSearchStreamParams = TypedDict('FussballdeNewsSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'channel': NotRequired[Literal['news', 'pro_news']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdePlayerDefaultParams = TypedDict('FussballdePlayerDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_id': Required[str],
}, total=False)

FussballdePlayerTextResponseParams = TypedDict('FussballdePlayerTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_id': Required[str],
}, total=False)

FussballdePlayerStreamParams = TypedDict('FussballdePlayerStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_id': Required[str],
}, total=False)

FussballdePlayerMatchesDefaultParams = TypedDict('FussballdePlayerMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_id': Required[str],
    'season': NotRequired[str],
    'team_id': NotRequired[str],
}, total=False)

FussballdePlayerMatchesTextResponseParams = TypedDict('FussballdePlayerMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_id': Required[str],
    'season': NotRequired[str],
    'team_id': NotRequired[str],
}, total=False)

FussballdePlayerMatchesStreamParams = TypedDict('FussballdePlayerMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_id': Required[str],
    'season': NotRequired[str],
    'team_id': NotRequired[str],
}, total=False)

FussballdePlayerSearchDefaultParams = TypedDict('FussballdePlayerSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'first_name': NotRequired[str],
    'last_name': NotRequired[str],
    'place': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdePlayerSearchTextResponseParams = TypedDict('FussballdePlayerSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'first_name': NotRequired[str],
    'last_name': NotRequired[str],
    'place': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdePlayerSearchStreamParams = TypedDict('FussballdePlayerSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'first_name': NotRequired[str],
    'last_name': NotRequired[str],
    'place': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdePositionHistoryDefaultParams = TypedDict('FussballdePositionHistoryDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'competition_id': Required[str],
}, total=False)

FussballdePositionHistoryTextResponseParams = TypedDict('FussballdePositionHistoryTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'competition_id': Required[str],
}, total=False)

FussballdePositionHistoryStreamParams = TypedDict('FussballdePositionHistoryStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'competition_id': Required[str],
}, total=False)

FussballdePostalCodesDefaultParams = TypedDict('FussballdePostalCodesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
}, total=False)

FussballdePostalCodesTextResponseParams = TypedDict('FussballdePostalCodesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
}, total=False)

FussballdePostalCodesStreamParams = TypedDict('FussballdePostalCodesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
}, total=False)

FussballdeTableDefaultParams = TypedDict('FussballdeTableDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'competition_id': Required[str],
    'view': NotRequired[Literal['overall', 'home_away', 'rounds', 'fairness', 'cross']],
    'matchday': NotRequired[int],
}, total=False)

FussballdeTableTextResponseParams = TypedDict('FussballdeTableTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'competition_id': Required[str],
    'view': NotRequired[Literal['overall', 'home_away', 'rounds', 'fairness', 'cross']],
    'matchday': NotRequired[int],
}, total=False)

FussballdeTableStreamParams = TypedDict('FussballdeTableStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'competition_id': Required[str],
    'view': NotRequired[Literal['overall', 'home_away', 'rounds', 'fairness', 'cross']],
    'matchday': NotRequired[int],
}, total=False)

FussballdeTeamDefaultParams = TypedDict('FussballdeTeamDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[str],
}, total=False)

FussballdeTeamTextResponseParams = TypedDict('FussballdeTeamTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[str],
}, total=False)

FussballdeTeamStreamParams = TypedDict('FussballdeTeamStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[str],
}, total=False)

FussballdeTeamMatchesDefaultParams = TypedDict('FussballdeTeamMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[str],
    'kind': NotRequired[Literal['all', 'next', 'previous', 'wins', 'draws', 'losses']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'competition_kind': NotRequired[Literal['1', '8', '3', '7', '6', '11', '2', '21', '9']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeTeamMatchesTextResponseParams = TypedDict('FussballdeTeamMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[str],
    'kind': NotRequired[Literal['all', 'next', 'previous', 'wins', 'draws', 'losses']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'competition_kind': NotRequired[Literal['1', '8', '3', '7', '6', '11', '2', '21', '9']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeTeamMatchesStreamParams = TypedDict('FussballdeTeamMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[str],
    'kind': NotRequired[Literal['all', 'next', 'previous', 'wins', 'draws', 'losses']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'competition_kind': NotRequired[Literal['1', '8', '3', '7', '6', '11', '2', '21', '9']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeTeamSquadDefaultParams = TypedDict('FussballdeTeamSquadDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[str],
    'season': NotRequired[str],
    'kind': NotRequired[Literal['squad', 'arrivals', 'departures']],
}, total=False)

FussballdeTeamSquadTextResponseParams = TypedDict('FussballdeTeamSquadTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[str],
    'season': NotRequired[str],
    'kind': NotRequired[Literal['squad', 'arrivals', 'departures']],
}, total=False)

FussballdeTeamSquadStreamParams = TypedDict('FussballdeTeamSquadStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[str],
    'season': NotRequired[str],
    'kind': NotRequired[Literal['squad', 'arrivals', 'departures']],
}, total=False)

FussballdeTopScorersDefaultParams = TypedDict('FussballdeTopScorersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'competition_id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeTopScorersTextResponseParams = TypedDict('FussballdeTopScorersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'competition_id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FussballdeTopScorersStreamParams = TypedDict('FussballdeTopScorersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'competition_id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)
