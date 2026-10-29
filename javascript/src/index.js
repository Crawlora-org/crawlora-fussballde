import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class FussballdeClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-fussballde-js/0.1.0" });
    this["amateurStats"] = (...args) => this.request("fussballde-amateur-stats", ...args);
    this["club"] = (...args) => this.request("fussballde-club", ...args);
    this["clubMatches"] = (...args) => this.request("fussballde-club-matches", ...args);
    this["clubSearch"] = (...args) => this.request("fussballde-club-search", ...args);
    this["competitionOptions"] = (...args) => this.request("fussballde-competition-options", ...args);
    this["competitions"] = (...args) => this.request("fussballde-competitions", ...args);
    this["federation"] = (...args) => this.request("fussballde-federation", ...args);
    this["filters"] = (...args) => this.request("fussballde-filters", ...args);
    this["match"] = (...args) => this.request("fussballde-match", ...args);
    this["matchCalendar"] = (...args) => this.request("fussballde-match-calendar", ...args);
    this["matchComparison"] = (...args) => this.request("fussballde-match-comparison", ...args);
    this["matchPlan"] = (...args) => this.request("fussballde-match-plan", ...args);
    this["matchday"] = (...args) => this.request("fussballde-matchday", ...args);
    this["nationalTopScorers"] = (...args) => this.request("fussballde-national-top-scorers", ...args);
    this["news"] = (...args) => this.request("fussballde-news", ...args);
    this["newsArticle"] = (...args) => this.request("fussballde-news-article", ...args);
    this["newsSearch"] = (...args) => this.request("fussballde-news-search", ...args);
    this["player"] = (...args) => this.request("fussballde-player", ...args);
    this["playerMatches"] = (...args) => this.request("fussballde-player-matches", ...args);
    this["playerSearch"] = (...args) => this.request("fussballde-player-search", ...args);
    this["positionHistory"] = (...args) => this.request("fussballde-position-history", ...args);
    this["postalCodes"] = (...args) => this.request("fussballde-postal-codes", ...args);
    this["table"] = (...args) => this.request("fussballde-table", ...args);
    this["team"] = (...args) => this.request("fussballde-team", ...args);
    this["teamMatches"] = (...args) => this.request("fussballde-team-matches", ...args);
    this["teamSquad"] = (...args) => this.request("fussballde-team-squad", ...args);
    this["topScorers"] = (...args) => this.request("fussballde-top-scorers", ...args);
  }
}

export { FussballdeClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default FussballdeClient;
