# Senti-Bot
Bot that can analyse daily sentiment of the stop market and summerize news in short.
📊 Stock Market Sentiment Bot
A simple Twitter/X bot that fetches the top stock market news of the day, analyzes the sentiment using natural language processing, and posts a concise summary.

✅ Built with Python, Finnhub API, TextBlob, and Tweepy.
# 🚀 Features
Fetches the latest financial news headlines
Performs sentiment analysis on headlines
Posts a daily sentiment summary on Twitter/X
Modular codebase: fetch_news, analyze_sentiment, post_tweet

# 📸 Sample Output (Tweet)

📊 Stock Market Sentiment (July 8)

Sentiment: 🔴 Negative

Top News:

- Markets fall after Fed signals higher-for-longer rates
- Apple and Tesla lead tech pullback

# 🛠️ Tech Stack
Python

Finnhub API – For financial news

TextBlob – Sentiment analysis

Tweepy – Twitter API wrapper

.env – Secure storage of API keys


# 🧪 Quick Setup

1. Clone the Repository

git clone https://github.com/shashankreddy28/stock-sentiment-bot.git

cd stock-sentiment-bot

3. Install Dependencies

pip install -r requirements.txt

OR manually:

pip install requests tweepy nltk textblob python-dotenv

3. Create a .env File
   
Add the following to a .env file in the root directory:

FINNHUB_API_KEY=your_finnhub_key

TWITTER_API_KEY=your_twitter_api_key

TWITTER_API_SECRET=your_twitter_api_secret

TWITTER_ACCESS_TOKEN=your_access_token

TWITTER_ACCESS_SECRET=your_access_secret

4. Run the Bot

python main.py or python3 main.py

🧰 File Structure
stock-sentiment-bot/
├── fetch_news.py           # Fetches top news headlines

├── analyze_sentiment.py    # Analyzes overall sentiment

├── post_tweet.py           # Posts tweet via Twitter API

├── main.py                 # Entry point

├── .env                    # API keys (not committed to Git)

└── README.md
