from fetch_news import get_stock_news, get_general_news
from analyse_sentiment import analyze_sentiment, get_average_sentiment, get_expected_change
from get_stocks import get_sp500_tickers
import asyncio
from send_discord import send_discord_message
from datetime import datetime

def run_bot():
    stocks_to_analyze = get_sp500_tickers()
    stock_news = get_stock_news(stocks_to_analyze)
    general_news_items = get_general_news()

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
                "headlines": [item["headline"] for item in news_items[:1]], # Only 1 headline
            })

    overall_sentiment = get_average_sentiment(all_sentiments)
    overall_expected_change = get_expected_change(overall_sentiment)

    message = f"""📊 **Stock Market Sentiment** ({date})\n\n**Overall Sentiment:** {overall_expected_change} ({overall_sentiment:.2f})\n"""

    if stock_sentiments:
        # Sort stocks by sentiment to get best and worst performers
        sorted_stocks = sorted(stock_sentiments, key=lambda x: x['sentiment'], reverse=True)
        best_performers = sorted_stocks[:5]
        worst_performers = sorted_stocks[-5:]

        message += "\n📈 **Top 5 Best Performers**\n"
        for performer in best_performers:
            message += f"**{performer['stock']}** - Sentiment: {get_expected_change(performer['sentiment'])} ({performer['sentiment']:.2f})\n"
            for headline in performer['headlines']:
                message += f"- {headline}\n"

        message += "\n📉 **Top 5 Worst Performers**\n"
        for performer in worst_performers:
            message += f"**{performer['stock']}** - Sentiment: {get_expected_change(performer['sentiment'])} ({performer['sentiment']:.2f})\n"
            for headline in performer['headlines']:
                message += f"- {headline}\n"

        # Overall Top Headlines (from general news)
        if general_news_items:
            message += "\n✨ **Overall Top Headlines**\n"
            for item in general_news_items[:2]: # Top 2 general headlines
                message += f"- {item['headline']}\n"

    message += "\n#StockMarket #FinanceBot"

    print(message)  # For testing purposes
    if len(message) > 2000:
        print("Message too long, truncating...", "length:", len(message))
        message = message[:1997] + "..."
    asyncio.run(send_discord_message(message))

if __name__ == "__main__":
    run_bot()
