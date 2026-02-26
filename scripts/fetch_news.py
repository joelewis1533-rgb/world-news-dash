import requests
import json
import os

# Get API Key from GitHub Secrets
API_KEY = os.getenv("NEWS_API_KEY")

def fetch_and_save(url, filename):
    try:
        response = requests.get(url)
        data = response.json()
        
        # We use ../ to go UP one folder out of 'scripts' into the main area
        # OR we just use the filename if the Action runs from the root
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Successfully saved {filename}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if not API_KEY:
        print("ERROR: NEWS_API_KEY is missing!")
    else:
        # World News
        fetch_and_save(f"https://newsapi.org{API_KEY}", "news-data.json")
        # NBA News
        fetch_and_save(f"https://newsapi.org{API_KEY}", "sports-data.json")
