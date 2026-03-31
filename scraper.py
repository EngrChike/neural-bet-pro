import json
import datetime
import random

def start_engine():
    now = datetime.datetime.now()
    current_month_name = now.strftime("%B %Y")
    
    teams = ["Real Madrid", "Man City", "Bayern", "Arsenal", "PSG", "Liverpool", "Napoli", "Dortmund", "Barcelona", "Inter"]
    
    # Generate 10-Day Roadmap (Future)
    roadmap = []
    for i in range(10):
        day_date = now + datetime.timedelta(days=i)
        roadmap.append({
            "date": day_date.strftime("%b %d"),
            "match": f"{teams[i]} vs {random.choice(teams)}",
            "pick": "Over 2.5",
            "status": "UPCOMING"
        })

    # Generate Past Results (History)
    history = []
    win_count = 0
    loss_count = 0
    
    # We simulate the last 15 days of results
    for i in range(1, 16):
        past_date = now - datetime.timedelta(days=i)
        # Only count if the result happened in the CURRENT month
        is_this_month = past_date.month == now.month
        
        res = random.choice(["WIN", "LOSS"])
        if is_this_month:
            if res == "WIN": win_count += 1
            else: loss_count += 1
            
        history.append({
            "date": past_date.strftime("%b %d"),
            "match": f"{random.choice(teams)} vs {random.choice(teams)}",
            "result": res,
            "score": f"{random.randint(0,4)}-{random.randint(0,4)}"
        })

    final_data = {
        "last_updated": now.strftime("%Y-%m-%d %H:%M"),
        "current_month": current_month_name,
        "monthly_stats": {
            "wins": win_count,
            "losses": loss_count,
            "total": win_count + loss_count
        },
        "ten_day_runner": roadmap,
        "history": history
    }

    with open('data.json', 'w') as f:
        json.dump(final_data, f, indent=4)
    print(f"Stats Updated for {current_month_name}")

if __name__ == "__main__":
    start_engine()
