import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Collect data for a stock
ticker = input("Enter the Stock Symbol: ").upper()
df = yf.download(ticker, start="2010-01-01", end="2022-12-31")

# Calculate the daily returns of the stock
returns = df["Close"].pct_change().dropna()

# Group the daily returns into yearly returns
returns_per_year = returns.resample("A").sum()

# Calculate the average yearly return
mean_return_per_year = returns_per_year.mean()

# Calculate the standard deviation of the yearly returns
std_dev_per_year = returns_per_year.std()

risk_free_rate = 0.0 # assume a risk-free rate of 0%
sharpe_ratio = (mean_return_per_year - risk_free_rate) / std_dev_per_year

print(f"The average yearly return of {ticker} is {mean_return_per_year:.2%}")
print(f"The standard deviation of the yearly returns of {ticker} is {std_dev_per_year:.2%}")

print(f"The Sharpe ratio of {ticker} is {sharpe_ratio:.2f}")

if sharpe_ratio < 1:
    print(ticker, "is a safe stock to invest." )
    
elif sharpe_ratio > 1:
    print( ticker, " is a risky stock to invest.")

plt.plot(df["Close"])
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.title(f"{ticker} Stock Price")
plt.show()