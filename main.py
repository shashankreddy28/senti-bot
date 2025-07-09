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
    stock_sentiments = []

    for stock, news_items in stock_news.items():
        if news_items:
            sentiment_scores = analyze_sentiment(news_items)
            average_sentiment = get_average_sentiment(sentiment_scores)
            all_sentiments.extend(sentiment_scores)
            stock_sentiments.append({
                "stock": stock,
                "sentiment": average_sentiment,
                "headlines": [item["headline"] for item in news_items[:2]],
                "summaries": [item["summary"] for item in news_items[:2]]
            })

    overall_sentiment = get_average_sentiment(all_sentiments)
    overall_expected_change = get_expected_change(overall_sentiment)

    message = f"""📊 **Stock Market Sentiment** ({date})

**Overall Sentiment:** {overall_expected_change} ({overall_sentiment:.2f})
"""

    if stock_sentiments:
        best_performer = max(stock_sentiments, key=lambda x: x['sentiment'])
        worst_performer = min(stock_sentiments, key=lambda x: x['sentiment'])

        message += "\n📈 **Best Performer**\n"
        message += f"**{best_performer['stock']}** - Sentiment: {get_expected_change(best_performer['sentiment'])} ({best_performer['sentiment']:.2f})\n"
        for i in range(len(best_performer['headlines'])):
            message += f"- **Headline:** {best_performer['headlines'][i]}\n"
            message += f"  **Summary:** {best_performer['summaries'][i]}\n"

        message += "\n📉 **Worst Performer**\n"
        message += f"**{worst_performer['stock']}** - Sentiment: {get_expected_change(worst_performer['sentiment'])} ({worst_performer['sentiment']:.2f})\n"
        for i in range(len(worst_performer['headlines'])):
            message += f"- **Headline:** {worst_performer['headlines'][i]}\n"
            message += f"  **Summary:** {worst_performer['summaries'][i]}\n"

    message += "\n#StockMarket #FinanceBot"

    print(message)  # For testing purposes
    if len(message) > 2000:
        print("Message too long, truncating...", "length:", len(message))
        message = message[:1997] + "..."
    asyncio.run(send_discord_message(message))

if __name__ == "__main__":
    run_bot()
