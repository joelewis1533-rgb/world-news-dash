import requests
import json
import os

# Pulls from GitHub Secrets
API_KEY = os.getenv("NEWS_API_KEY")

def fetch_and_save(url, filename):
    try:
        response = requests.get(url)
        data = response.json()
        
        if "articles" in data:
            # Saves directly to the main folder so the website can see it
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Successfully created {filename}")
        else:
            print(f"Error: API returned no articles. Check your API Key.")
    except Exception as e:
        print(f"Failed to fetch {filename}: {e}")

if __name__ == "__main__":
    if not API_KEY:
        print("CRITICAL ERROR: NEWS_API_KEY is missing from GitHub Secrets!")
    else:
        # World News
        fetch_and_save(f"https://newsapi.org{API_KEY}", "news-data.json")
        # NBA Sports News
        fetch_and_save(f"https://newsapi.org{API_KEY}", "sports-data.json")
