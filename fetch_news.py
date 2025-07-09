import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import finnhub
load_dotenv()
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")

def get_general_news():
    """
    Fetches general news headlines and summaries since the previous market close (4:00 PM ET).
    Returns a list of dictionaries containing headlines and summaries.
    """
    # Initialize Finnhub client
    finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
    # Get current time and previous market close
    now = datetime.now()
    # Market closes at 4:00 PM ET, so we use yesterday's close if before 4:00 PM today
    if now.hour < 16:
        market_close = (now - timedelta(days=1)).replace(hour=16, minute=0, second=0, microsecond=0)
    else:
        market_close = now.replace(hour=16, minute=0, second=0, microsecond=0)
    
    # Format dates for Finnhub API (YYYY-MM-DD)
    from_date = market_close.strftime("%Y-%m-%d")
    to_date = now.strftime("%Y-%m-%d")
    try:
        # Fetch general market news
        news = finnhub_client.general_news('general', min_id=0)
        
        # Filter news by date and extract headlines and summaries
        filtered_news = [
            {
                "headline": article["headline"],
                "summary": article["summary"]
            }
            for article in news
            if datetime.fromtimestamp(article["datetime"]) >= market_close
        ]
        
        return filtered_news
    
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []
    
    finally:
        # Clean up client
        finnhub_client.close()

def get_stock_news(stocks):
    """
    Fetches news headlines and summaries for a list of stocks since the previous market close (4:00 PM ET).
    Returns a dictionary where keys are stock tickers and values are lists of news items.
    """
    # Initialize Finnhub client
    finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
    # Get current time and previous market close
    now = datetime.now()
    # Market closes at 4:00 PM ET, so we use yesterday's close if before 4:00 PM today
    if now.hour < 16:
        market_close = (now - timedelta(days=1)).replace(hour=16, minute=0, second=0, microsecond=0)
    else:
        market_close = now.replace(hour=16, minute=0, second=0, microsecond=0)
    
    # Format dates for Finnhub API (YYYY-MM-DD)
    from_date = market_close.strftime("%Y-%m-%d")
    to_date = now.strftime("%Y-%m-%d")
    
    stock_news = {}
    try:
        for stock in stocks:
            news = finnhub_client.company_news(stock, _from=from_date, to=to_date)
            
            filtered_news = [
                {
                    "headline": article["headline"],
                    "summary": article["summary"]
                }
                for article in news
                if datetime.fromtimestamp(article["datetime"]) >= market_close
            ]
            stock_news[stock] = filtered_news
        
        return stock_news
    
    except Exception as e:
        print(f"Error fetching stock news: {e}")
        return {}
    
    finally:
        # Clean up client
        finnhub_client.close()

if __name__ == "__main__":
    general_news_items = get_general_news()
    print(f'Number of general news items: {len(general_news_items)}')
    print("Latest General News Headlines:")
    for item in general_news_items:
        print(f"Headline: {item['headline']}")
        print(f"Summary: {item['summary']}\n")
        
    stocks_to_fetch = ["AAPL", "GOOGL", "MSFT"]
    stock_news_items = get_stock_news(stocks_to_fetch)
    print(f'\nNumber of stock news items: {sum(len(v) for v in stock_news_items.values())}')
    for stock, news_list in stock_news_items.items():
        print(f"\nLatest News for {stock}:")
        for item in news_list:
            print(f"  Headline: {item['headline']}")
            print(f"  Summary: {item['summary']}\n")