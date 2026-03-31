import json
import datetime
import random

# --- START OF LOGIC (NO INDENTATION NEEDED) ---
start_date = datetime.datetime.now()
teams = ["Bayern", "Real Madrid", "Man City", "Liverpool", "Napoli", "Dortmund", "Barcelona", "Inter", "PSG", "Ajax"]

# 1. Generate the 10-Day Roadmap
roadmap = []
for i in range(10):
    day_date = start_date + datetime.timedelta(days=i)
    roadmap.append({
        "day_number": i + 1,
        "date": day_date.strftime("%A, %b %d"),
        "match": f"{teams[i]} vs {random.choice(teams)}",
        "pick": "Over 2.5 Goals",
        "status": "LOCKED"
    })

# 2. Generate Daily Slips
slips = [
    {"match": "Arsenal vs Chelsea", "pick": "GG + Over 2.5", "odds": "2.40"},
    {"match": "Juventus vs Milan", "pick": "Home Win + Over 1.5", "odds": "2.10"}
]

# 3. Save to data.json
final_data = {
    "last_updated": start_date.strftime("%Y-%m-%d %H:%M"),
    "ten_day_runner": roadmap,
    "daily_slips": slips
}

with open('data.json', 'w') as f:
    json.dump(final_data, f, indent=4)

print("Success: data.json created!")
# --- END OF LOGIC ---
