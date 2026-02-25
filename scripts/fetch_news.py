import requests
import json
import os

# Use your actual NewsAPI key here
API_KEY = os.getenv("NEWS_API_KEY") or "YOUR_API_KEY_HERE"

def fetch_and_save(url, filename):
    try:
        response = requests.get(url)
        data = response.json()
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Successfully saved {filename}")
    except Exception as e:
        print(f"Error fetching {filename}: {e}")

if __name__ == "__main__":
    # World News URL
    world_url = f"https://newsapi.org{API_KEY}"
    # NBA Sports News URL
    sports_url = f"https://newsapi.org{API_KEY}"

    fetch_and_save(world_url, 'news-data.json')
    fetch_and_save(sports_url, 'sports-data.json')
