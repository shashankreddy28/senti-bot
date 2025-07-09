from fetch_news import get_news
from analyze_sentiment import analyze_sentiment
import asyncio
from send_discord import send_discord_message
from datetime import datetime

def run_bot():
    headlines = get_news()
    sentiment = analyze_sentiment(headlines)
    date = datetime.today().strftime('%B %d')
    message = f"""📊 Stock Market Sentiment ({date})
Sentiment: {sentiment}
Top News:
- {headlines[0]}
- {headlines[1]}
#StockMarket #FinanceBot"""
    # post_to_twitter(message)
    print(message)  # For testing purposes
    asyncio.run(send_discord_message(message))
if __name__ == "__main__":
    run_bot()
