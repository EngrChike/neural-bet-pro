import json
import datetime
import requests
import os

def start_engine():
    # Pull the secret key from GitHub's vault
    api_key = os.getenv('FOOTBALL_API_KEY')
    headers = {'X-Auth-Token': api_key}
    
    # URL for upcoming matches in top leagues
    # Change the URL line to this:
url = 'https://api.football-data.org/v4/matches?dateFrom=' + datetime.datetime.now().strftime('%Y-%m-%d') + '&dateTo=' + (datetime.datetime.now() + datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        all_matches = data.get('matches', [])
    except Exception as e:
        print(f"Error fetching data: {e}")
        all_matches = []

    roadmap = []
    # Filter for the first 10 matches found
    for i, match in enumerate(all_matches[:10]):
        utc_date = datetime.datetime.strptime(match['utcDate'], "%Y-%m-%dT%H:%M:%SZ")
        roadmap.append({
            "day_number": i + 1,
            "date": utc_date.strftime("%A, %b %d"),
            "match": f"{match['homeTeam']['name']} vs {match['awayTeam']['name']}",
            "pick": "Over 2.5 Goals",
            "status": "LOCKED"
        })

    # If API fails or is empty, we use a fallback
    if not roadmap:
        roadmap = [{"day_number": 1, "date": "Check back soon", "match": "No live games found", "pick": "-", "status": "WAITING"}]

    final_data = {
        "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "ten_day_runner": roadmap,
        "daily_slips": roadmap[:2] # Using real matches for daily slips too
    }

    with open('data.json', 'w') as f:
        json.dump(final_data, f, indent=4)
    print("Success: Live data synced!")

if __name__ == "__main__":
    start_engine()
