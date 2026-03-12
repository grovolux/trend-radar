import requests
import pandas as pd

url = "https://hacker-news.firebaseio.com/v0/topstories.json"

response = requests.get(url)
story_ids = response.json()[:20]

posts = []

for story_id in story_ids:
    item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    item = requests.get(item_url).json()

    posts.append({
        "title": item.get("title"),
        "score": item.get("score"),
        "comments": item.get("descendants"),
        "url": item.get("url")
    })

df = pd.DataFrame(posts)

print(df.to_string())
