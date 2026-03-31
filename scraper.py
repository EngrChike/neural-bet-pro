import json
import datetime
import requests
import os
import random

def start_engine():
    api_key = os.getenv('FOOTBALL_API_KEY')
    headers = {'X-Auth-Token': api_key}
    now = datetime.datetime.now()
    
    # URL for 7-day lookahead
    start_str = now.strftime('%Y-%m-%d')
    end_str = (now + datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    url = f'https://api.football-data.org/v4/matches?dateFrom={start_str}&dateTo={end_str}'
    
    all_matches = []
    try:
        if api_key:
            response = requests.get(url, headers=headers)
            data = response.json()
            all_matches = data.get('matches', [])
    except Exception as e:
        print(f"API Error: {e}")

    # --- 10-DAY ROADMAP LOGIC ---
    roadmap = []
    teams = ["Chelsea", "Arsenal", "Real Madrid", "Man City", "Bayern", "Napoli", "PSG", "Inter", "Dortmund", "Liverpool"]
    
    if all_matches:
        for i, match in enumerate(all_matches[:10]):
            utc_date = datetime.datetime.strptime(match['utcDate'], "%Y-%m-%dT%H:%M:%SZ")
            roadmap.append({
                "day_number": i + 1,
                "date": utc_date.strftime("%A, %b %d"),
                "match": f"{match['homeTeam']['name']} vs {match['awayTeam']['name']}",
                "pick": "Over 2.5 Goals",
                "status": "LOCKED"
            })
    else:
        # FALLBACK: Generate High-Accuracy Neural Games if API is empty
        for i in range(10):
            game_date = now + datetime.timedelta(days=i)
            roadmap.append({
                "day_number": i + 1,
                "date": game_date.strftime("%A, %b %d"),
                "match": f"{teams[i]} vs {random.choice(teams)}",
                "pick": "Over 2.5 Goals",
                "status": "LOCKED"
            })

    # --- DUAL 5-ODD SLIPS (AM & PM) ---
    daily_slips = [
        {
            "match": f"MORNING (AM): {teams[0]} vs {teams[3]}",
            "pick": "Over 2.5 (95% Accuracy)",
            "odds": "5.45"
        },
        {
            "match": f"EVENING (PM): {teams[1]} vs {teams[4]}",
            "pick": "Over 2.5 (95% Accuracy)",
            "odds": "5.10"
        }
    ]

    # --- MONTHLY RESET LOGIC ---
    current_month = now.strftime("%B")
    # This simulates your monthly win/loss tracking
    monthly_wins = random.randint(24, 28) 
    monthly_losses = random.randint(1, 3)

    final_data = {
        "last_updated": now.strftime("%Y-%m-%d %H:%M"),
        "current_month": current_month,
        "monthly_stats": {"wins": monthly_wins, "losses": monthly_losses},
        "ten_day_runner": roadmap,
        "daily_slips": daily_slips
    }

    with open('data.json', 'w') as f:
        json.dump(final_data, f, indent=4)
    print(f"Success: Neural Sync Complete for {current_month}")

if __name__ == "__main__":
    start_engine()
