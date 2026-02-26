import requests
import json
import os

API_KEY = os.getenv("NEWS_API_KEY")

def save_news(url, filename):
    try:
        r = requests.get(url)
        data = r.json()
        if data.get("status") == "ok":
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Saved {filename}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if API_KEY:
        # World News
        save_news(f"https://newsapi.org{API_KEY}", "news-data.json")
        # NBA Sports
        save_news(f"https://newsapi.org{API_KEY}", "sports-data.json")
