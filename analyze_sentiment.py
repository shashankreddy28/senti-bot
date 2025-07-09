from textblob import TextBlob

def analyze_sentiment(headlines):
    polarity = 0
    for headline in headlines:
        blob = TextBlob(headline)
        polarity += blob.sentiment.polarity
    avg_polarity = polarity / len(headlines)
    
    if avg_polarity > 0.1:
        return "🟢 Positive"
    elif avg_polarity < -0.1:
        return "🔴 Negative"
    else:
        return "🟡 Neutral"
