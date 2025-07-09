import pandas as pd

def get_sp500_tickers():
    """
    Scrapes the Wikipedia page for the list of S&P 500 companies and returns a list of their tickers.
    """
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    # The read_html function returns a list of all tables found on the page
    tables = pd.read_html(url)
    # The first table on the page is the one we want
    sp500_table = tables[0]
    # The 'Symbol' column contains the tickers
    tickers = sp500_table['Symbol'].tolist()
    return tickers[:25]

if __name__ == '__main__':
    sp500_tickers = get_sp500_tickers()
    print("S&P 500 Tickers (Top 25):")
    print(sp500_tickers)
    print(f"\nTotal number of tickers: {len(sp500_tickers)}")
