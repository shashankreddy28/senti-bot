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
- discord.py (to send automated messages)  
- dotenv (to keep secrets out of code)

---

## 📸 Sample Message in Discord
```
📊 **Stock Market Sentiment** (July 09)

**Overall Sentiment:** 🟡 Neutral (0.07)

📈 **Top 5 Best Performers**
**JPM** - Sentiment: 🟢 Strongly Positive (1.00)
- JP Morgan CEO to Handelsblatt: we want to invest further in Germany
**LLY** - Sentiment: 🟢 Strongly Positive (0.67)
- Eli Lilly: new recommended dosage for Kisunla
**V** - Sentiment: 🟢 Positive (0.50)
- Mar Vista U.S. Quality Q2 2025 Commentary
**PFE** - Sentiment: 🟢 Positive (0.50)
- Companies Like Pfizer Inc (PFE) are Boosting the Cannabis Light Market
**AMZN** - Sentiment: 🟢 Positive (0.43)
- IHerb Welcomes Hyeyoung Moon as Chief Revenue Officer; Former LG, Amazon and Starbucks Exec Joins iHerb to Drive Customer Acquisition and Brand Loyalty in the U.S. and Priority Global Markets

📉 **Top 5 Worst Performers**
**META** - Sentiment: 🔴 Negative (-0.25)
- EssilorLuxottica shares jump after reports that Meta bought 3% stake
**BAC** - Sentiment: 🔴 Negative (-0.25)
- Bank Of America: Structural Compounder, But No Urgency To Buy Today
**TSLA** - Sentiment: 🔴 Negative (-0.33)
- ON Semiconductor: Tesla And Aehr Test Systems Are The Sell Signal After 80% Run
**PG** - Sentiment: 🔴 Strongly Negative (-1.00)
- Why Procter & Gamble (PG) Dipped More Than Broader Market Today
**MA** - Sentiment: 🔴 Strongly Negative (-1.00)
- Mastercard's Vocalink Gets $16.2 Million BOE Fine for Compliance Failures

✨ **Overall Top Headlines**
- Chaos continues at Elon Musk’s X with departure of CEO Linda Yaccarino
- Buy this stock if you want copper exposure, analyst says

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
├── get_stocks.py           # Provides a hardcoded list of 25 popular stock tickers
├── fetch_news.py           # Fetches news headlines for specific stocks
├── analyze_sentiment.py    # Analyzes sentiment using FinBERT
├── send_discord.py         # Sends message to first available Discord channel
├── main.py                 # Entry point
├── .env                    # API keys (excluded from Git)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```