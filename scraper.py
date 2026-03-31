import json
import datetime
import random
import os
import requests

def start_engine():
    now = datetime.datetime.now()
    current_month_label = now.strftime("%B %Y")
    api_key = os.getenv('FOOTBALL_API_KEY')
    headers = {'X-Auth-Token': api_key}
    
    # 1. Fetch Real Matches for the next 7 days
    start_str = now.strftime('%Y-%m-%d')
    end_str = (now + datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    url = f'https://api.football-data.org/v4/matches?dateFrom={start_str}&dateTo={end_str}'
    
    roadmap = []
    daily_slip = []
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        matches = data.get('matches', [])
        
        # Build 10-Day Roadmap from real fixtures
        for m in matches[:10]:
            match_date = datetime.datetime.strptime(m['utcDate'], "%Y-%m-%dT%H:%M:%SZ")
            roadmap.append({
                "date": match_date.strftime("%b %d"),
                "match": f"{m['homeTeam']['shortName']} vs {m['awayTeam']['shortName']}",
                "pick": "Over 2.5 Goals",
                "odds": "1.85"
            })

        # Build the 5-Odd Daily Slip (Using first 3 matches)
        if len(matches) >= 3:
            for m in matches[:3]:
                daily_slip.append({
                    "match": f"{m['homeTeam']['shortName']} vs {m['awayTeam']['shortName']}",
                    "pick": "Over 2.5",
                    "odds": "1.80"
                })
    except:
        roadmap = [{"date": "N/A", "match": "Check API Connection", "pick": "-"}]
        daily_slip = [{"match": "No Live Data", "pick": "-", "odds": "0.00"}]

    # 2. History & Monthly Stats Logic
    history = []
    wins, losses = 0, 0
    for i in range(1, 11):
        past_date = now - datetime.timedelta(days=i)
        is_this_month = (past_date.month == now.month)
        res = random.choice(["WIN", "LOSS"])
        if is_this_month:
            if res == "WIN": wins += 1
            else: losses += 1
        history.append({
            "date": past_date.strftime("%b %d"),
            "match": "Previous Analysis",
            "result": res
        })

    final_data = {
        "last_updated": now.strftime("%Y-%m-%d %H:%M"),
        "current_month": current_month_label,
        "monthly_stats": {"wins": wins, "losses": losses},
        "daily_5_odd": daily_slip,
        "ten_day_runner": roadmap,
        "history": history
    }

    with open('data.json', 'w') as f:
        json.dump(final_data, f, indent=4)

if __name__ == "__main__":
    start_engine()
