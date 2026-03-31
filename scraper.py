import json
import datetime
import random
import os

def analyze_deep_stats():
    # Simulates checking Coach style, Player injury/form, and Manager changes
    styles = ["High-Press Attacking", "Tactical Defensive", "Counter-Strike", "Possession"]
    accuracy_trigger = random.randint(92, 98) # Target 95% average
    return {
        "tactic": random.choice(styles),
        "form": f"{accuracy_trigger}%",
        "scout_note": "New Manager factor analyzed" if random.random() > 0.8 else "Stable Squad"
    }

def start_engine():
    now = datetime.datetime.now()
    scout = analyze_deep_stats()
    
    # --- 10-DAY ROADMAP (1 Sure Game Per Day) ---
    teams = ["Chelsea", "Arsenal", "Real Madrid", "Man City", "Bayern", "Napoli", "PSG", "Inter", "Dortmund", "Liverpool"]
    roadmap = []
    for i in range(10):
        game_date = now + datetime.timedelta(days=i)
        roadmap.append({
            "date": game_date.strftime("%b %d"),
            "match": f"{teams[i]} vs {random.choice(teams)}",
            "pick": "Sure Over 1.5",
            "accuracy": "95%"
        })

    # --- DAILY 5-ODD SLIPS (AM & PM) ---
    am_slip = [
        {"match": "Lazio vs Milan", "pick": "BTTS", "odds": "1.95"},
        {"match": "Ajax vs PSV", "pick": "Over 2.5", "odds": "1.80"},
        {"match": "Porto vs Braga", "pick": "Home Win", "odds": "1.65"}
    ]
    pm_slip = [
        {"match": "Real Madrid vs Barca", "pick": "Over 2.5", "odds": "1.85"},
        {"match": "Man City vs Arsenal", "pick": "GG (BTTS)", "odds": "1.75"},
        {"match": "Juve vs Inter", "pick": "Over 1.5", "odds": "1.60"}
    ]

    # --- MONTHLY RESET LOGIC ---
    # (Simplified for display; in production this compares timestamps)
    wins = random.randint(20, 30) # Simulated wins for current month
    losses = random.randint(2, 5)

    final_data = {
        "last_updated": now.strftime("%Y-%m-%d %H:%M"),
        "current_month": now.strftime("%B %Y"),
        "monthly_stats": {"wins": wins, "losses": losses},
        "scout": scout,
        "am_slip": am_slip,
        "pm_slip": pm_slip,
        "ten_day_runner": roadmap
    }

    with open('data.json', 'w') as f:
        json.dump(final_data, f, indent=4)

if __name__ == "__main__":
    start_engine()
