

# 📊 Stock Market Sentiment Bot (Discord Edition)

A Discord bot that fetches daily financial news for the top 25 S&P 500 stocks, analyzes sentiment using FinBERT, and posts a market update to your server, highlighting the best and worst performers.

---

## 🚀 Features
- Fetches financial news for the top 25 S&P 500 stocks.
- Analyzes overall daily sentiment using FinBERT (a language model specialized for financial text).
- Identifies and highlights the top 5 best and worst performing stocks based on sentiment, including their top headlines.
- Provides overall top headlines from general news.
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

**Overall Sentiment:** 🟡 Neutral (0.09)

📈 **Top 5 Best Performers**
**ADBE** - Sentiment: 🟢 Strongly Positive (1.00)
- Adobe (NASDAQ:ADBE) Is Investing Its Capital With Increasing Efficiency
**AMCR** - Sentiment: 🟢 Strongly Positive (1.00)
- Jefferies Initiates “Buy” on Amcor (AMCR), Sets Price Target at $12 on Strong Market Position
**ABT** - Sentiment: 🟢 Positive (0.50)
- Biomarkers Market Research Report 2025-2030 | Assay Kit Demand Surges as Advancements in Omics Technologies Elevate Biomarker Discovery and Diagnostic Precision
**AMZN** - Sentiment: 🟢 Positive (0.43)
- IHerb Welcomes Hyeyoung Moon as Chief Revenue Officer; Former LG, Amazon and Starbucks Exec Joins iHerb to Drive Customer Acquisition and Brand Loyalty in the U.S. and Priority Global Markets
**ACN** - Sentiment: 🟡 Neutral (0.00)
- Accenture (ACN) Buy SYSTEMA to Support Manufacturing Automation for Semiconductor Clients

📉 **Top 5 Worst Performers**
**MO** - Sentiment: 🟡 Neutral (0.00)
- Altria: Jefferies initiates coverage says 'sell'
**AEE** - Sentiment: 🟡 Neutral (0.00)
- Ameren Corporation Second Quarter 2025 Earnings Webcast Aug. 1, 2025
**GOOGL** - Sentiment: 🟡 Neutral (-0.03)
- Meta Has Surged on the Back of AI Software. Why Hardware Is the Next Play.
**GOOG** - Sentiment: 🔴 Negative (-0.14)
- Inside Tesla's Robotaxi Revolution
**AES** - Sentiment: 🔴 Negative (-0.29)
- Traders Eye Fed Minutes as US Equity Futures Post Narrow Gains Pre-Bell

✨ **Overall Top Headlines**
- Buy this stock if you want copper exposure, analyst says
- TikTok is reportedly readying a standalone U.S. app. It could set the stage for a long-awaited spinoff.

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

