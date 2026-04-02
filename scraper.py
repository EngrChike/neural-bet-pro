<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEURAL-BET | Professional AI Predictions</title>
    <style>
        :root { --blue: #00d4ff; --green: #39ff14; --gold: #f59e0b; --bg: #05070a; --card: #11141d; --border: #2a2f3a; }
        body { background: var(--bg); color: #e2e8f0; font-family: 'Segoe UI', sans-serif; padding: 15px; max-width: 500px; margin: auto; }
        
        /* Stats Header */
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
        .win-pill { background: var(--green); color: black; padding: 5px 12px; border-radius: 20px; font-weight: bold; font-size: 0.8rem; box-shadow: 0 0 10px rgba(57,255,20,0.3); }

        /* Scouting Box */
        .scout-box { background: rgba(0,212,255,0.05); border: 1px solid var(--blue); border-radius: 12px; padding: 15px; margin-bottom: 25px; font-size: 0.85rem; }

        /* Slip Cards */
        .section-label { color: var(--blue); font-size: 0.7rem; font-weight: 800; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; display: block; }
        .slip-card { background: var(--card); border: 1px solid var(--border); border-radius: 16px; padding: 20px; margin-bottom: 20px; position: relative; }
        .odds-badge { position: absolute; top: 15px; right: 15px; background: var(--blue); color: #000; padding: 3px 8px; border-radius: 5px; font-weight: bold; font-size: 0.7rem; }
        
        .game-row { display: flex; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid #1e232d; }
        .game-row:last-child { border: none; }
        .pick { color: var(--green); font-weight: 800; font-size: 0.85rem; }

        /* Roadmap */
        .roadmap { background: var(--card); border: 1px solid var(--border); border-radius: 16px; padding: 10px 15px; }
        .road-item { display: grid; grid-template-columns: 70px 1fr 60px; padding: 12px 0; border-bottom: 1px solid #1e232d; font-size: 0.85rem; align-items: center; }
    </style>
</head>
<body>

    <div class="header">
        <h1 style="margin:0; font-size: 1.6rem;">NEURAL<span style="color:var(--blue)">-BET</span></h1>
        <div class="win-pill" id="stat-pill">WINS: 0 | LOSS: 0</div>
    </div>

    <div class="scout-box">
        <b style="color:var(--blue)">SCOUT REPORT:</b> <span id="scout-note">Syncing neural data...</span>
    </div>

    <span class="section-label">Dual 5-Odd Slips</span>
    
    <div class="slip-card" style="border-top: 4px solid var(--gold);">
        <span class="odds-badge">5.50 ODDS</span>
        <b style="color:var(--gold); font-size: 0.8rem;">MORNING (AM) SLIP</b>
        <div id="am-list"></div>
    </div>

    <div class="slip-card" style="border-top: 4px solid var(--blue);">
        <span class="odds-badge">5.20 ODDS</span>
        <b style="color:var(--blue); font-size: 0.8rem;">EVENING (PM) SLIP</b>
        <div id="pm-list"></div>
    </div>

    <span class="section-label">10-Day Accumulator (O2.5)</span>
    <div class="roadmap" id="road-list"></div>

    <script>
        // Force refresh with cache-buster
        fetch('data.json?v=' + Date.now())
        .then(r => r.json())
        .then(data => {
            document.getElementById('stat-pill').innerText = `WINS: ${data.monthly_stats.wins} | LOSS: ${data.monthly_stats.losses}`;
            document.getElementById('scout-note').innerText = data.scout.note;

            let amH = ''; data.am_slip.forEach(g => {
                amH += `<div class="game-row"><span>${g.match}</span><span class="pick">${g.pick}</span></div>`;
            });
            document.getElementById('am-list').innerHTML = amH;

            let pmH = ''; data.pm_slip.forEach(g => {
                pmH += `<div class="game-row"><span>${g.match}</span><span class="pick">${g.pick}</span></div>`;
            });
            document.getElementById('pm-list').innerHTML = pmH;

            let rdH = ''; data.ten_day_runner.forEach(g => {
                rdH += `<div class="road-item">
                    <span style="color:#707785">${g.date}</span>
                    <span style="font-weight:600; text-align:center;">${g.match}</span>
                    <span style="color:var(--gold); text-align:right; font-weight:800;">O2.5</span>
                </div>`;
            });
            document.getElementById('road-list').innerHTML = rdH;
        })
        .catch(e => console.error("Could not load games:", e));
    </script>
</body>
</html>
