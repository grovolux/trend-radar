import requests
import pandas as pd

url = "https://www.reddit.com/r/startups/top.json?t=day&limit=25"

headers = {
    "User-Agent": "trend-radar-bot"
}

response = requests.get(url, headers=headers)
data = response.json()

posts = []

for post in data["data"]["children"]:
    posts.append({
        "title": post["data"]["title"],
        "score": post["data"]["score"],
        "comments": post["data"]["num_comments"],
        "url": post["data"]["url"]
    })

df = pd.DataFrame(posts)

print(df)
