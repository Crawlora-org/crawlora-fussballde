import os

from crawlora_fussballde import FussballdeClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with FussballdeClient(api_key=api_key) as client:
    club_search = client.club_search(text='Bayern')
    print('club_search', club_search)
    national_top_scorers = client.national_top_scorers()
    print('national_top_scorers', national_top_scorers)
