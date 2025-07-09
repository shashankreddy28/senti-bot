def get_sp500_tickers():
    """
    Returns a hardcoded list of 25 popular stock tickers.
    """
    return [
        "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "TSLA", "META", "BRK.B", "JPM", "JNJ",
        "V", "PG", "UNH", "HD", "MA", "LLY", "XOM", "CVX", "KO", "PEP",
        "WMT", "BAC", "PFE", "DIS", "CMCSA"
    ]

if __name__ == '__main__':
    sp500_tickers = get_sp500_tickers()
    print("Popular Tickers (Top 25):")
    print(sp500_tickers)
    print(f"\nTotal number of tickers: {len(sp500_tickers)}")
