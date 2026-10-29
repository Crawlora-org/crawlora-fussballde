import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class FussballdeClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  amateurStats(params: OperationParamsMap["fussballde-amateur-stats"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  club(params: OperationParamsMap["fussballde-club"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  clubMatches(params: OperationParamsMap["fussballde-club-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  clubSearch(params?: OperationParamsMap["fussballde-club-search"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  competitionOptions(params: OperationParamsMap["fussballde-competition-options"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  competitions(params: OperationParamsMap["fussballde-competitions"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  federation(params?: OperationParamsMap["fussballde-federation"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  filters(params?: OperationParamsMap["fussballde-filters"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  match(params: OperationParamsMap["fussballde-match"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchCalendar(params: OperationParamsMap["fussballde-match-calendar"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchComparison(params: OperationParamsMap["fussballde-match-comparison"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchPlan(params: OperationParamsMap["fussballde-match-plan"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchday(params: OperationParamsMap["fussballde-matchday"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  nationalTopScorers(params?: OperationParamsMap["fussballde-national-top-scorers"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  news(params?: OperationParamsMap["fussballde-news"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  newsArticle(params: OperationParamsMap["fussballde-news-article"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  newsSearch(params: OperationParamsMap["fussballde-news-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  player(params: OperationParamsMap["fussballde-player"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerMatches(params: OperationParamsMap["fussballde-player-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerSearch(params?: OperationParamsMap["fussballde-player-search"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  positionHistory(params: OperationParamsMap["fussballde-position-history"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  postalCodes(params: OperationParamsMap["fussballde-postal-codes"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  table(params: OperationParamsMap["fussballde-table"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  team(params: OperationParamsMap["fussballde-team"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamMatches(params: OperationParamsMap["fussballde-team-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamSquad(params: OperationParamsMap["fussballde-team-squad"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  topScorers(params: OperationParamsMap["fussballde-top-scorers"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  amateurStats(params: OperationParamsMap["fussballde-amateur-stats"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  club(params: OperationParamsMap["fussballde-club"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  clubMatches(params: OperationParamsMap["fussballde-club-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  clubSearch(params?: OperationParamsMap["fussballde-club-search"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  competitionOptions(params: OperationParamsMap["fussballde-competition-options"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  competitions(params: OperationParamsMap["fussballde-competitions"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  federation(params?: OperationParamsMap["fussballde-federation"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  filters(params?: OperationParamsMap["fussballde-filters"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  match(params: OperationParamsMap["fussballde-match"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchCalendar(params: OperationParamsMap["fussballde-match-calendar"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchComparison(params: OperationParamsMap["fussballde-match-comparison"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchPlan(params: OperationParamsMap["fussballde-match-plan"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchday(params: OperationParamsMap["fussballde-matchday"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  nationalTopScorers(params?: OperationParamsMap["fussballde-national-top-scorers"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  news(params?: OperationParamsMap["fussballde-news"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  newsArticle(params: OperationParamsMap["fussballde-news-article"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  newsSearch(params: OperationParamsMap["fussballde-news-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  player(params: OperationParamsMap["fussballde-player"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerMatches(params: OperationParamsMap["fussballde-player-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerSearch(params?: OperationParamsMap["fussballde-player-search"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  positionHistory(params: OperationParamsMap["fussballde-position-history"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  postalCodes(params: OperationParamsMap["fussballde-postal-codes"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  table(params: OperationParamsMap["fussballde-table"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  team(params: OperationParamsMap["fussballde-team"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamMatches(params: OperationParamsMap["fussballde-team-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamSquad(params: OperationParamsMap["fussballde-team-squad"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  topScorers(params: OperationParamsMap["fussballde-top-scorers"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  amateurStats(...args: OperationRequestArgs<"fussballde-amateur-stats">): Promise<OperationResponseMap["fussballde-amateur-stats"]>;
  club(...args: OperationRequestArgs<"fussballde-club">): Promise<OperationResponseMap["fussballde-club"]>;
  clubMatches(...args: OperationRequestArgs<"fussballde-club-matches">): Promise<OperationResponseMap["fussballde-club-matches"]>;
  clubSearch(...args: OperationRequestArgs<"fussballde-club-search">): Promise<OperationResponseMap["fussballde-club-search"]>;
  competitionOptions(...args: OperationRequestArgs<"fussballde-competition-options">): Promise<OperationResponseMap["fussballde-competition-options"]>;
  competitions(...args: OperationRequestArgs<"fussballde-competitions">): Promise<OperationResponseMap["fussballde-competitions"]>;
  federation(...args: OperationRequestArgs<"fussballde-federation">): Promise<OperationResponseMap["fussballde-federation"]>;
  filters(...args: OperationRequestArgs<"fussballde-filters">): Promise<OperationResponseMap["fussballde-filters"]>;
  match(...args: OperationRequestArgs<"fussballde-match">): Promise<OperationResponseMap["fussballde-match"]>;
  matchCalendar(...args: OperationRequestArgs<"fussballde-match-calendar">): Promise<OperationResponseMap["fussballde-match-calendar"]>;
  matchComparison(...args: OperationRequestArgs<"fussballde-match-comparison">): Promise<OperationResponseMap["fussballde-match-comparison"]>;
  matchPlan(...args: OperationRequestArgs<"fussballde-match-plan">): Promise<OperationResponseMap["fussballde-match-plan"]>;
  matchday(...args: OperationRequestArgs<"fussballde-matchday">): Promise<OperationResponseMap["fussballde-matchday"]>;
  nationalTopScorers(...args: OperationRequestArgs<"fussballde-national-top-scorers">): Promise<OperationResponseMap["fussballde-national-top-scorers"]>;
  news(...args: OperationRequestArgs<"fussballde-news">): Promise<OperationResponseMap["fussballde-news"]>;
  newsArticle(...args: OperationRequestArgs<"fussballde-news-article">): Promise<OperationResponseMap["fussballde-news-article"]>;
  newsSearch(...args: OperationRequestArgs<"fussballde-news-search">): Promise<OperationResponseMap["fussballde-news-search"]>;
  player(...args: OperationRequestArgs<"fussballde-player">): Promise<OperationResponseMap["fussballde-player"]>;
  playerMatches(...args: OperationRequestArgs<"fussballde-player-matches">): Promise<OperationResponseMap["fussballde-player-matches"]>;
  playerSearch(...args: OperationRequestArgs<"fussballde-player-search">): Promise<OperationResponseMap["fussballde-player-search"]>;
  positionHistory(...args: OperationRequestArgs<"fussballde-position-history">): Promise<OperationResponseMap["fussballde-position-history"]>;
  postalCodes(...args: OperationRequestArgs<"fussballde-postal-codes">): Promise<OperationResponseMap["fussballde-postal-codes"]>;
  table(...args: OperationRequestArgs<"fussballde-table">): Promise<OperationResponseMap["fussballde-table"]>;
  team(...args: OperationRequestArgs<"fussballde-team">): Promise<OperationResponseMap["fussballde-team"]>;
  teamMatches(...args: OperationRequestArgs<"fussballde-team-matches">): Promise<OperationResponseMap["fussballde-team-matches"]>;
  teamSquad(...args: OperationRequestArgs<"fussballde-team-squad">): Promise<OperationResponseMap["fussballde-team-squad"]>;
  topScorers(...args: OperationRequestArgs<"fussballde-top-scorers">): Promise<OperationResponseMap["fussballde-top-scorers"]>;
}
export { FussballdeClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default FussballdeClient;
