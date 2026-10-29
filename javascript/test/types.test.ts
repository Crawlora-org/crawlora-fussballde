import { FussballdeClient } from "../src/index.js";

const client = new FussballdeClient({ apiKey: "test-key" });
void client.amateurStats({"stat": "1"});
void client.request("fussballde-amateur-stats", {"stat": "1"});
const streamResponse: Promise<Response> = client.request("fussballde-amateur-stats", {"stat": "1"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("fussballde-amateur-stats", {"stat": "1"}, { responseType: "stream" });
const directStream: Promise<Response> = client.amateurStats({"stat": "1"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("fussballde-amateur-stats", {"stat": "1", "season": "sample", "team_type": "1", "federation_id": "89", "limit": 1, "offset": 1}, { responseType: "text" });
const rawText: Promise<string> = client.request("fussballde-amateur-stats", {"stat": "1"}, { responseType: "text" });
void rawText;


void client.clubSearch();
void client.request("fussballde-club-search");
// @ts-expect-error The selected operation requires its documented params.
void client.amateurStats();
