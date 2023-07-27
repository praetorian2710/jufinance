from jufinance import Quote

tickers = ["INFY", "RELIANCE", "HDFCBANK", "HDFC"]
quote = Quote(tickers[1])


# quote.get_stock_info() : Retrieves general information about the stock, such as its name, sector, industry, and more.

# quote.get_current_price(): Fetches the current price of the stock.

# quote.get_pros_and_cons(): Retrieves the pros and cons of the stock based on analyst opinions.

# quote.get_basic_info(): Fetches basic information about the stock, including its ISIN, BSE code, NSE symbol, and more.

# quote.get_financials(): Retrieves financial information for the stock, such as balance sheet, income statement, and cash flow.

# quote.get_annual_reports(): Fetches links to the stock's annual reports.

# quote.get_market_depth(): Retrieves market depth data, including bids and asks.

# quote.get_stock_price_change(): Fetches information about stock price changes and percentage changes.

# quote.get_broker_research(): Retrieves broker research reports related to the stock.

# quote.get_top_news(): Fetches top news related to the stock.

# quote.get_stock_historical_data(): Retrieves historical price data for the stock.
print(quote.get_stock_historical_data())
