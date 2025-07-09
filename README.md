
# 📊 Stock Market Sentiment Bot (Discord Edition)

A Discord bot that fetches daily financial news, analyzes sentiment using FinBERT, and posts a market update to your server.

---

## 🚀 Features
- Fetches financial news for specific stocks (AAPL, GOOGL, MSFT) from Finnhub
- Analyzes overall daily sentiment using FinBERT (a language model specialized for financial text)
- Posts a market summary to your Discord server automatically

---

## 🛠️ Tech Stack
- Python  
- Finnhub API (for financial news)  
- Transformers & PyTorch (for sentiment analysis with FinBERT)  
- discord.py (to send automated messages)  
- dotenv (to keep secrets out of code)

---

## 📸 Sample Message in Discord
```
📊 Stock Market Sentiment (July 9)
Overall Sentiment: 0.03

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
├── fetch_news.py           # Fetches news headlines for specific stocks
├── analyze_sentiment.py    # Analyzes sentiment using FinBERT
├── send_discord.py         # Sends message to first available Discord channel
├── main.py                 # Entry point
├── .env                    # API keys (excluded from Git)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```
