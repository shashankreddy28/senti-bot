from fetch_news import get_stock_news
from analyse_sentiment import analyze_sentiment, get_average_sentiment, get_expected_change
from get_stocks import get_sp500_tickers
import asyncio
from send_discord import send_discord_message
from datetime import datetime

def run_bot():
    stocks_to_analyze = get_sp500_tickers()
    stock_news = get_stock_news(stocks_to_analyze)

    date = datetime.today().strftime('%B %d')
    
    all_sentiments = []
    significant_movers = []

    for stock, news_items in stock_news.items():
        if news_items:
            sentiment_scores = analyze_sentiment(news_items)
            average_sentiment = get_average_sentiment(sentiment_scores)
            all_sentiments.extend(sentiment_scores)

            if abs(average_sentiment) > 0.65:
                expected_change = get_expected_change(average_sentiment)
                significant_movers.append({
                    "stock": stock,
                    "sentiment": average_sentiment,
                    "expected_change": expected_change,
                    "headlines": [item["headline"] for item in news_items[:3]],
                    "summaries": [item["summary"] for item in news_items[:3]]
                })

    overall_sentiment = get_average_sentiment(all_sentiments)
    overall_expected_change = get_expected_change(overall_sentiment)

    message = f"""📊 **Stock Market Sentiment** ({date})

**Overall Sentiment:** {overall_expected_change} ({overall_sentiment:.2f})\n"""

    if significant_movers:
        message += "\n**Top Movers:**\n"
        for mover in significant_movers:
            message += f"- **{mover['stock']}**: {mover['expected_change']} ({mover['sentiment']:.2f})\n"

        message += "\n**Top Headlines & Summaries:**\n"
        for mover in significant_movers:
            message += f"\n**{mover['stock']}**\n"
            for i in range(len(mover['headlines'])):
                message += f"- **Headline:** {mover['headlines'][i]}\n"
                message += f"  **Summary:** {mover['summaries'][i]}\n"


    message += "\n#StockMarket #FinanceBot"

    print(message)  # For testing purposes
    if len(message) > 2000:
        print("Message too long, truncating...", "length:", len(message))
        message = message[:1997] + "..."
    asyncio.run(send_discord_message(message))

if __name__ == "__main__":
    run_bot()
