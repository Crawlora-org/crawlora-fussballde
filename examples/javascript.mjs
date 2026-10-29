import { FussballdeClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new FussballdeClient({ apiKey });

  const clubSearch = await client.clubSearch({ text: "Bayern" });
  console.log("clubSearch", clubSearch);
  const nationalTopScorers = await client.nationalTopScorers({  });
  console.log("nationalTopScorers", nationalTopScorers);
