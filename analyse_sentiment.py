from fetch_news import get_stock_news
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

def analyze_sentiment(news_items):
    """
    Analyzes the sentiment of news articles using FinBERT.
    Returns a list of sentiment scores.
    """
    tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
    model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

    sentiments = []
    for item in news_items:
        inputs = tokenizer(item["headline"], return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            logits = model(**inputs).logits
        
        scores = {
            'positive': torch.nn.functional.softmax(logits, dim=-1)[0][0].item(),
            'negative': torch.nn.functional.softmax(logits, dim=-1)[0][1].item(),
            'neutral': torch.nn.functional.softmax(logits, dim=-1)[0][2].item()
        }
        
        # Determine sentiment label
        sentiment_label = max(scores, key=scores.get)
        
        # Convert sentiment to numerical score
        if sentiment_label == 'positive':
            sentiments.append(1)
        elif sentiment_label == 'negative':
            sentiments.append(-1)
        else:
            sentiments.append(0)
            
    return sentiments

def get_average_sentiment(sentiments):
    """
    Calculates the average sentiment score.
    """
    if not sentiments:
        return 0
    return sum(sentiments) / len(sentiments)

if __name__ == "__main__":
    stocks_to_analyze = ["AAPL", "GOOGL", "MSFT"]
    stock_news = get_stock_news(stocks_to_analyze)

    for stock, news_items in stock_news.items():
        if news_items:
            sentiment_scores = analyze_sentiment(news_items)
            average_sentiment = get_average_sentiment(sentiment_scores)
            print(f"Average sentiment for {stock}: {average_sentiment}")
        else:
            print(f"No news found for {stock}.")
