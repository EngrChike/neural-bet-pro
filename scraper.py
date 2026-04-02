import json
import datetime
import random

# Generate current date
now = datetime.datetime.now()
current_month = now.strftime("%B %Y")

# Create 3 totally different game lists
am_games = ["Napoli vs Lazio", "Milan vs Monza", "Ajax vs Vitesse"]
pm_games = ["Real Madrid vs Betis", "Man City vs Everton", "Arsenal vs Fulham"]
road_teams = ["Liverpool", "PSG", "Inter", "Bayern", "Dortmund", "Porto", "Chelsea", "Spurs", "Benfica", "Roma"]

# 1. Build Morning Slip
am_slip = []
for g in am_games:
    am_slip.append({"match": g, "pick": "O2.5"})

# 2. Build Evening Slip
pm_slip = []
for g in pm_games:
    pm_slip.append({"match": g, "pick": "O2.5"})

# 3. Build 10-Day Roadmap (Over 2.5 Odd Accumulation)
ten_day = []
for i in range(10):
    game_date = now + datetime.timedelta(days=i)
    ten_day.append({
        "date": game_date.strftime("%b %d"),
        "match": f"{road_teams[i % 10]} vs Opponent",
        "pick": "O2.5"
    })

# The Master Dictionary - This MUST match the HTML keys
data_to_save = {
    "last_updated": now.strftime("%Y-%m-%d %H:%M"),
    "current_month": current_month,
    "monthly_stats": {"wins": 15, "losses": 2},
    "am_slip": am_slip,
    "pm_slip": pm_slip,
    "ten_day_runner": ten_day
}

# Write the file
with open('data.json', 'w') as f:
    json.dump(data_to_save, f, indent=4)

print("SUCCESS: data.json has been created with fresh games.")
