import requests
import os
from dotenv import load_dotenv

load_dotenv()
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")

def get_news():
    url = f"https://finnhub.io/api/v1/news?category=general&token={FINNHUB_API_KEY}"
    res = requests.get(url)
    news = res.json()
    return [item['headline'] for item in news[:5]]  # Top 5 headlines
