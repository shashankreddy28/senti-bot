# 📊 Stock Market Sentiment Bot (Discord Edition)

A Discord bot that fetches daily financial news for the top 25 S&P 500 stocks, analyzes sentiment using FinBERT, and posts a market update to your server, highlighting the best and worst performers.

---

## 🚀 Features
- Fetches financial news for the top 25 S&P 500 stocks.
- Analyzes overall daily sentiment using FinBERT (a language model specialized for financial text).
- Identifies and highlights the top 5 best and worst performing stocks based on sentiment, including their top headlines.
- Provides overall top headlines from general news with embedded links.
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
**AMZN** - Sentiment: 🟢 Positive (0.40)
- VideoAmp Empowers Advertisers with Cloud-Native Measurement Using Privacy- Enhanceancing Controls with AWS Clean Rooms

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
- [Here are five charts investors should be watching right now](https://www.marketwatch.com/story/here-are-five-charts-investors-should-be-watching-right-now-50723187)
- [Should Apple replace Tim Cook as CEO? These analysts want a dramatic change.](https://www.marketwatch.com/story/should-apple-replace-tim-cook-as-ceo-these-analysts-want-a-dramatic-change-d1e067dd)
- [Chaos continues at Elon Musk’s X with departure of CEO Linda Yaccarino](https://www.marketwatch.com/story/chaos-continues-at-elon-musks-x-with-departure-of-ceo-linda-yaccarino-af99c2ea)
- [Buy this stock if you want copper exposure, analyst says](https://www.marketwatch.com/story/buy-this-stock-if-you-want-copper-exposure-analyst-says-bffc660a)
- [TikTok is reportedly readying a standalone U.S. app. It could set the stage for a long-awaited spinoff.](https://www.marketwatch.com/story/tiktok-is-reportedly-readying-a-standalone-u-s-app-it-could-set-the-stage-for-a-long-awaited-spinoff.](https://www.marketwatch.com/story/tiktok-is-reportedly-readying-a-standalone-u-s-app-it-could-set-the-stage-for-a-long-awaited-spinoff-50723187)
- [Millennials say they need $847,000 to feel ‘comfortable’ financially. Here’s how much Gen Z, Gen X and boomers want.](https://www.marketwatch.com/story/millennials-say-they-need-847-000-to-feel-comfortable-financially-heres-how-much-gen-z-gen-x-and-boomers-want.](https://www.marketwatch.com/story/millennials-say-they-need-847-000-to-feel-comfortable-financially-heres-how-much-gen-z-gen-x-and-boomers-want-50723187)
- [Tesla investors ask: When’s the shareholder meeting?](https://www.marketwatch.com/story/tesla-investors-ask-whens-the-shareholder-meeting.](https://www.marketwatch.com/story/tesla-investors-ask-whens-the-shareholder-meeting-50723187)
- [Big Tech rallies — plus, where we stand on Starbucks after China stake offers](https://www.marketwatch.com/story/big-tech-rallies-plus-where-we-stand-on-starbucks-after-china-stake-offers.](https://www.marketwatch.com/story/big-tech-rallies-plus-where-we-stand-on-starbucks-after-china-stake-offers-50723187)
```

---

## 🧪 Quick Setup Guide

### 1. Clone the Repo & Install Requirements
```bash
git clone https://github.com/shashankreddy28/senti-bot.git
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
5. **Invite the bot to your server:** Copy the generated URL and paste it into your browser. This will allow you to select a server to add the bot to.
6. That’s it! The bot will post to the **first available text channel**.

**Note on Channel Selection:** By default, the bot will attempt to send messages to a channel named `stock-sentiment`. If this channel does not exist in any server the bot is a member of, it will send the message to the first available text channel it finds. You can change the target channel name by modifying the `channel_name` argument in the `send_discord_message` function call within `main.py`.

---

## ▶️ Run the Bot
```bash
python main.py
```
To run the bot immediately for testing purposes:
```bash
python main.py --test
```

---

## 🔄 Automate It (Optional)
To automate the bot to run daily 1 hour before market open (8:30 AM ET, Monday-Friday):

### 1. Create a Shell Script (e.g., `run_bot.sh`)
Create a file named `run_bot.sh` in the root directory of your project with the following content:
```bash
#!/bin/bash

# Navigate to the bot's directory
cd /path/to/your/senti-bot

# Activate the virtual environment
source venv/bin/activate

# Run the Python script
python main.py

# Deactivate the virtual environment (optional)
deactivate
```
**Remember to replace `/path/to/your/senti-bot` with the actual absolute path to your project directory.**

### 2. Make the Shell Script Executable
```bash
chmod +x run_bot.sh
```

### 3. Schedule with Cron
Open your crontab for editing:
```bash
crontab -e
```
Add the following line to schedule the script to run at 8:00 AM ET, Monday through Friday:
```cron
0 8 * * 1-5 /path/to/your/senti-bot/run_bot.sh >> /path/to/your/senti-bot/cron.log 2>&1
```
**Again, replace `/path/to/your/senti-bot` with the actual absolute path to your project directory.**

This cron job will:
- Run at 8:30 AM (30 minutes past 8 AM).
- Every day of the month (`*`).
- Every month (`*`).
- On weekdays (1-5, where 1 is Monday and 5 is Friday).
- Execute your `run_bot.sh` script.
- Redirect all standard output and standard error to `cron.log` for logging purposes.

---

## ☁️ Free Hosting Options

Here are a few options for hosting your bot for free:

### 2. Replit
- **Pros:** Easy to use online IDE, supports many languages, can keep bots running 24/7 (though free tier might require some workarounds to prevent sleeping).
- **Cons:** Free tier projects might go to sleep after inactivity, requiring external pings or paid plans for continuous uptime.
- **Setup:** Import your GitHub repository, install dependencies, and configure a "Uptime Robot" or similar service to ping your Replit app regularly to keep it awake.

### 3. Heroku (with caveats)
- **Pros:** Popular platform for deploying web apps and bots, good documentation.
- **Cons:** Free tier has been significantly reduced or removed for many features. You might incur costs for continuous operation.
- **Setup:** Requires a `Procfile` to specify how your bot runs. You'll need to link your GitHub repo and deploy. Be mindful of their current free tier policies.

### 4. Google Cloud Platform / Amazon Web Services (Free Tiers)
- **Pros:** Powerful, scalable, and highly customizable. Generous free tiers for new users.
- **Cons:** Can be complex to set up for beginners, requires more technical knowledge.
- **Setup:** Explore services like Google Cloud Run, AWS Lambda, or EC2 (for a small virtual machine) within their free tier limits. You'll need to configure triggers (e.g., Cloud Scheduler for GCP, CloudWatch Events for AWS) to run your script.

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
