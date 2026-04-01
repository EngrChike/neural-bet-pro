import json
import datetime
import random

# 1. Basic Setup
now = datetime.datetime.now()
current_month = now.strftime("%B %Y")

# 2. Generate 10-Day Roadmap (1 Game Per Day)
teams = ["Chelsea", "Arsenal", "Real Madrid", "Man City", "Bayern", "Napoli", "PSG", "Inter", "Dortmund", "Liverpool"]
roadmap = []
for i in range(10):
    game_date = now + datetime.timedelta(days=i)
    roadmap.append({
        "date": game_date.strftime("%b %d"),
        "match": f"{teams[i]} vs {random.choice(teams)}",
        "pick": "Sure Over 1.5",
        "status": "95% ACCURACY"
    })

# 3. Generate 5-Odd Slips (Morning & Evening)
am_slip = [
    {"match": "Lazio vs Milan", "pick": "BTTS", "odds": "1.95"},
    {"match": "Ajax vs PSV", "pick": "Over 2.5", "odds": "1.80"},
    {"match": "Porto vs Braga", "pick": "Home Win", "odds": "1.65"}
]
pm_slip = [
    {"match": "Real Madrid vs Barca", "pick": "Over 2.5", "odds": "1.85"},
    {"match": "Man City vs Arsenal", "pick": "GG", "odds": "1.75"},
    {"match": "Juve vs Inter", "pick": "Over 1.5", "odds": "1.60"}
]

# 4. Save to File
final_data = {
    "last_updated": now.strftime("%Y-%m-%d %H:%M"),
    "current_month": current_month,
    "monthly_stats": {"wins": 12, "losses": 2},
    "scout": {"tactic": "Attacking High-Press", "form": "95%", "note": "Squad depth analyzed"},
    "am_slip": am_slip,
    "pm_slip": pm_slip,
    "ten_day_runner": roadmap
}

with open('data.json', 'w') as f:
    json.dump(final_data, f, indent=4)

print("Data saved successfully!")


