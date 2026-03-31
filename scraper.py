import json
import datetime
import random
def start_engine():
# Everything below this must have 4 spaces on the left!
start_date = datetime.datetime.now()
teams = [&quot;Bayern&quot;, &quot;Real Madrid&quot;, &quot;Man City&quot;, &quot;Liverpool&quot;, &quot;Napoli&quot;, &quot;Dortmund&quot;, &quot;Barcelona&quot;,
&quot;Inter&quot;, &quot;PSG&quot;, &quot;Ajax&quot;]
# 1. Generate the 10-Day Roadmap
roadmap = []
for i in range(10):
day_date = start_date + datetime.timedelta(days=i)
roadmap.append({
&quot;day_number&quot;: i + 1,
&quot;date&quot;: day_date.strftime(&quot;%A, %b %d&quot;),
&quot;match&quot;: f&quot;{teams[i]} vs {random.choice(teams)}&quot;,
&quot;pick&quot;: &quot;Over 2.5 Goals&quot;,
&quot;status&quot;: &quot;LOCKED&quot;
})
# 2. Generate Daily Slips
slips = [
{&quot;match&quot;: &quot;Arsenal vs Chelsea&quot;, &quot;pick&quot;: &quot;GG + Over 2.5&quot;, &quot;odds&quot;: &quot;2.40&quot;},
{&quot;match&quot;: &quot;Juventus vs Milan&quot;, &quot;pick&quot;: &quot;Home Win + Over 1.5&quot;, &quot;odds&quot;: &quot;2.10&quot;}
]
final_data = {
&quot;last_updated&quot;: start_date.strftime(&quot;%Y-%m-%d %H:%M&quot;),
&quot;ten_day_runner&quot;: roadmap,
&quot;daily_slips&quot;: slips
}
with open(&#39;data.json&#39;, &#39;w&#39;) as f:
json.dump(final_data, f, indent=4)
print(&quot;Success: data.json created!&quot;)
if __name__ == &quot;__main__&quot;:
start_engine()
