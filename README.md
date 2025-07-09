
# 📊 Stock Market Sentiment Bot (Discord Edition)

A Discord bot that fetches daily financial news for the top 25 S&P 500 stocks, analyzes sentiment using FinBERT, and posts a market update to your server, highlighting the best and worst performers.

---

## 🚀 Features
- Fetches financial news for the top 25 S&P 500 stocks.
- Analyzes overall daily sentiment using FinBERT (a language model specialized for financial text).
- Identifies and highlights the best and worst performing stocks based on sentiment.
- Posts a market summary to your Discord server automatically.

---

## 🛠️ Tech Stack
- Python  
- Finnhub API (for financial news)  
- Transformers & PyTorch (for sentiment analysis with FinBERT)  
- Pandas, BeautifulSoup4, lxml (for scraping S&P 500 tickers)
- discord.py (to send automated messages)  
- dotenv (to keep secrets out of code)

---

## 📸 Sample Message in Discord
```
📊 **Stock Market Sentiment** (July 09)

**Overall Sentiment:** Neutral (0.09)

📈 **Best Performer**
**ADBE** - Sentiment: Strongly Positive (1.00)
- **Headline:** Adobe (NASDAQ:ADBE) Is Investing Its Capital With Increasing Efficiency
  **Summary:** What trends should we look for it we want to identify stocks that can multiply in value over the long term? In a...
- **Headline:** 2 Phenomenal Stock Bargains to Buy With the Market at All-Time Highs
  **Summary:** The market assumes that generative AI will replace the Google Search engine.  Adobe's generative AI-powered image and video creation tools are industry-leading.  With the stock market at new all-time highs, investors may be a bit wary of buying stocks right now.

📉 **Worst Performer**
**AES** - Sentiment: Negative (-0.29)
- **Headline:** Traders Eye Fed Minutes as US Equity Futures Post Narrow Gains Pre-Bell
  **Summary:** US equity futures posted narrow gains before Wednesday's opening bell as traders looked ahead to the
- **Headline:** AES Stock Jumps on Report That Renewable Energy Firm Is Exploring Sale
  **Summary:** Shares in AES Corp. are jumping in premarket trading Wednesday as the renewable energy firm reportedly explores selling itself, among other options, as it faces takeover interest.

#StockMarket #FinanceBot
```

---

## 🧪 Quick Setup Guide

### 1. Clone the Repo & Install Requirements
```bash
git clone https://github.com/your-username/stock-sentiment-bot.git
cd stock-sentiment-bot
pip install -r requirements.txt
```

### 2. Create `.env` with Your API Keys
```dotenv
FINNHUB_API_KEY=your_finnhub_api_key
DISCORD_TOKEN=your_discord_bot_token
```

---

## 🤖 Set Up Your Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new app → Add a bot → Copy its token (add to `.env`)
3. Go to **OAuth2 → URL Generator**  
   - Scopes: `bot`  
   - Bot permissions: ✅ `Send Messages`
4. Copy the URL → Paste in browser → Invite the bot to your server
5. That’s it! The bot will post to the **first available text channel**.

---

## ▶️ Run the Bot
```bash
python main.py
```

---

## 🔄 Automate It (Optional)
Set up a daily message using:
- **cron** (local or server)
- **Replit + schedule**
- **GitHub Actions**

---

## 📄 License
MIT License – feel free to fork, modify, and deploy your own version.


---

## 📁 File Structure

```
stock-sentiment-bot/
├── get_stocks.py           # Scrapes S&P 500 tickers from Wikipedia
├── fetch_news.py           # Fetches news headlines for specific stocks
├── analyze_sentiment.py    # Analyzes sentiment using FinBERT
├── send_discord.py         # Sends message to first available Discord channel
├── main.py                 # Entry point
├── .env                    # API keys (excluded from Git)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```
