import requests
import json
import os

# 1. Setup (Using a free news API)
API_KEY = "YOUR_NEWSAPI_KEY_HERE"  # Get one free at newsapi.org
URL = f"https://newsapi.org{API_KEY}"

def fetch_and_save_news():
    try:
        # 2. Get the news data
        response = requests.get(URL)
        data = response.json()

        # 3. Save it to a file your website uses (e.g., news-data.json)
        with open('news-data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
        print("Successfully updated news-data.json")
    except Exception as e:
        print(f"Error fetching news: {e}")

if __name__ == "__main__":
    fetch_and_save_news()
