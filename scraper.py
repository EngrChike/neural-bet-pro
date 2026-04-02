import json
import datetime
import random

# Generate timestamps
now = datetime.datetime.now()
current_month = now.strftime("%B %Y")

# Three separate pools for unique games
morning_teams = ["Inter Milan", "Dortmund", "Porto", "Ajax", "Napoli", "Benfica", "Sporting CP", "AZ Alkmaar"]
evening_teams = ["Real Madrid", "Man City", "Arsenal", "Barcelona", "Liverpool", "Juventus", "Bayern Munich", "PSG"]
roadmap_teams = ["Aston Villa", "Newcastle", "Leverkusen", "Roma", "Monaco", "Lille", "Tottenham", "RB Leipzig"]

# 1. MORNING SLIP (3 Games)
am_slip = []
random.shuffle(morning_teams)
for i in range(3):
    am_slip.append({"match": f"{morning_teams[i]} vs Opponent", "pick": "O2.5"})

# 2. EVENING SLIP (3 Games)
pm_slip = []
random.shuffle(evening_teams)
for i in range(3):
    pm_slip.append({"match": f"{evening_teams[i]} vs Opponent", "pick": "O2.5"})

# 3. 10-DAY ROADMAP (10 Games)
roadmap = []
random.shuffle(roadmap_teams)
for i in range(10):
    game_date = now + datetime.timedelta(days=i)
    roadmap.append({
        "date": game_date.strftime("%b %d"),
        "match": f"{roadmap_teams[i % 8]} vs Opponent"
    })

# Final Dictionary
data = {
    "last_updated": now.strftime("%Y-%m-%d %H:%M"),
    "current_month": current_month,
    "monthly_stats": {"wins": 18, "losses": 3},
    "am_slip": am_slip,
    "pm_slip": pm_slip,
    "ten_day_runner": roadmap
}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

print("SUCCESS: Data generated and saved to data.json")
