import yfinance as yf

tsla = yf.Ticker("TSLA")

hist = tsla.history(period="1y")

hist.to_csv('./data/yfinance-tsla-1y.csv', index=False)