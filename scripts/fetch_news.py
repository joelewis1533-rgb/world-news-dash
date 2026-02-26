import requests
import json
import os

# 1. Pull the key from your GitHub Secrets
API_KEY = os.getenv("NEWS_API_KEY")

def fetch_and_save(url, filename):
    print(f"Attempting to fetch data for {filename}...")
    try:
        response = requests.get(url)
        data = response.json()
        
        # 2. Check if the API returned an error
        if data.get("status") == "error":
            print(f"❌ API Error for {filename}: {data.get('message')}")
            return

        # 3. Check if we actually got articles
        if "articles" in data and len(data["articles"]) > 0:
            # We save it to the current directory (root)
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"✅ Successfully saved {len(data['articles'])} articles to {filename}")
        else:
            print(f"⚠️ No articles found for {filename}. API status: {data.get('status')}")
            
    except Exception as e:
        print(f"❌ Connection Error for {filename}: {e}")

if __name__ == "__main__":
    if not API_KEY:
        print("❌ CRITICAL ERROR: NEWS_API_KEY is missing from GitHub Secrets!")
    else:
        # World News
        world_url = f"https://newsapi.org{API_KEY}"
        fetch_and_save(world_url, "news-data.json")
        
        # NBA Sports News
        sports_url = f"https://newsapi.org{API_KEY}"
        fetch_and_save(sports_url, "sports-data.json")
