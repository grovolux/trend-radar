import requests
import pandas as pd

url = "https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=100"

data = requests.get(url).json()

results = []
for item in data["hits"]:
    results.append({
        "title": item.get("title", ""),
        "score": item.get("points", 0)
    })

pd.DataFrame(results).to_csv("hackernews_trends.csv", index=False)
