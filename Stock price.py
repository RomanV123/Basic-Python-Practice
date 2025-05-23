import yfinance as yf # type: ignore

def stock_price(symbol: str = "AAPL") -> str:
    stock = yf.Ticker(symbol)
    price = stock.info.get("regularMarketPrice", "N/A")
    return f"{price:.2f}" if isinstance(price, (int, float)) else price

if __name__ == "__main__":
    for symbol in "AAPL AMZN IBM GOOG MSFT ORCL ABM A".split():
        print(f"Current {symbol:<4} stock price is:  {stock_price(symbol):>8}")


