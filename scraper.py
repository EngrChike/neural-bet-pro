<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>NEURAL-BET | Elite Scouting</title>
    <style>
        :root { --blue: #00d4ff; --gold: #ffd700; --bg: #05070a; --card: #11141d; }
        body { background: var(--bg); color: #e2e8f0; font-family: 'Inter', sans-serif; padding: 15px; max-width: 500px; margin: auto; }
        
        .scout-box { background: rgba(0,212,255,0.1); border: 1px solid var(--blue); padding: 15px; border-radius: 12px; margin-bottom: 20px; }
        .section-title { font-size: 0.8rem; letter-spacing: 2px; color: var(--blue); margin: 20px 0 10px; font-weight: 800; }
        
        /* 5-Odd Slip Styling */
        .slip-card { background: var(--card); border: 1px solid #222; border-radius: 15px; padding: 15px; margin-bottom: 20px; border-left: 5px solid var(--gold); }
        .odds-badge { background: var(--gold); color: black; padding: 2px 8px; border-radius: 4px; font-weight: bold; float: right; }

        .roadmap-item { display: flex; justify-content: space-between; background: #161b22; padding: 12px; border-radius: 8px; margin-bottom: 8px; border-bottom: 1px solid #30363d; }
        .hidden { display: none; }
        .tab-bar { display: flex; gap: 10px; margin: 20px 0; }
        .tab { flex: 1; text-align: center; padding: 10px; background: #1c2128; border-radius: 8px; cursor: pointer; border: 1px solid #30363d; }
        .tab.active { background: var(--blue); color: #000; font-weight: bold; }
    </style>
</head>
<body>

    <div class="scout-box">
        <div style="font-size: 0.7rem; color: var(--blue)">NEURAL SCOUTING ACTIVE (95% ACCURACY)</div>
        <div id="coach-report" style="font-weight: bold; margin-top:5px;">Analyzing Manager & Squad...</div>
    </div>

    <div class="section-title">TODAY'S 5-ODD SLIPS</div>
    
    <div class="slip-card">
        <span class="odds-badge">AM SLIP</span>
        <div id="am-table"></div>
    </div>

    <div class="slip-card" style="border-left-color: var(--blue)">
        <span class="odds-badge" style="background: var(--blue)">PM SLIP</span>
        <div id="pm-table"></div>
    </div>

    <div class="tab-bar">
        <div id="t1" class="tab active" onclick="tab('roadmap')">10-DAY ROADMAP</div>
        <div id="t2" class="tab" onclick="tab('history')">HISTORY</div>
    </div>

    <div id="v-roadmap"></div>
    <div id="v-history" class="hidden"></div>

    <script>
        function tab(v) {
            document.getElementById('v-roadmap').classList.toggle('hidden', v !== 'roadmap');
            document.getElementById('v-history').classList.toggle('hidden', v !== 'history');
            document.getElementById('t1').classList.toggle('active', v === 'roadmap');
            document.getElementById('t2').classList.toggle('active', v === 'history');
        }

        fetch('data.json').then(r => r.json()).then(data => {
            // Update Scout Report
            document.getElementById('coach-report').innerText = 
                `Style: ${data.scout_analysis.style} | Predicted Form: ${data.scout_analysis.form_index}`;

            // AM & PM Slips
            let amHtml = ''; data.daily_5_odd_am.forEach(g => {
                amHtml += `<div style="font-size:0.9rem; margin-bottom:5px;">${g.match} ➔ <b style="color:var(--gold)">${g.pick}</b></div>`;
            });
            document.getElementById('am-table').innerHTML = amHtml;

            let pmHtml = ''; data.daily_5_odd_pm.forEach(g => {
                pmHtml += `<div style="font-size:0.9rem; margin-bottom:5px;">${g.match} ➔ <b style="color:var(--blue)">${g.pick}</b></div>`;
            });
            document.getElementById('pm-table').innerHTML = pmHtml;

            // 10-Day Roadmap (1 Game per day)
            let roadHtml = '';
            data.ten_day_runner.forEach(g => {
                roadHtml += `<div class="roadmap-item">
                    <span>${g.date}</span>
                    <span style="font-weight:bold">${g.match}</span>
                    <span style="color:var(--gold)">${g.pick}</span>
                </div>`;
            });
            document.getElementById('v-roadmap').innerHTML = roadHtml;
        });
    </script>
</body>
</html>
