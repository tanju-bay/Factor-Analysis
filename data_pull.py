import pandas as pd
import numpy as np
import yfinance as yf
import statsmodels.api as sm
import matplotlib.pyplot as plt

def data_pull(ticker):
    # pulls the data from the csvs
    df_fama_factors = pd.read_csv("Fama_French_Factor_Returns.csv")
    df_momentum = pd.read_csv("Momentum_Factor_Returns.csv")
    # Light cleaning
    df_fama_factors = df_fama_factors.set_index("Date")
    df_momentum = df_momentum.set_index("Date")

    df_factors = pd.merge(df_fama_factors, df_momentum, on="Date", how="inner")
    df_factors.index = df_factors.index.astype(str)
    # have to convert date column into datetime str to properly merge with other dfs later
    df_factors.index = pd.to_datetime(df_factors.index)
    df_factors.index = df_factors.index.strftime("%Y%m%d")
    df_factors = df_factors / 100

    # pull the ticker data from yf
    df_ticker = yf.download(ticker, start="2020-01-01", end="2025-10-31")
    # calculate daily return
    df_ticker["daily return"] = df_ticker["Close"].pct_change()
    
    #clean up dataframe so just returns and date and format index
    df_ticker = df_ticker.drop(columns=["Open", "High", "Low", "Volume", "Close"])
    df_ticker = df_ticker.dropna()
    df_ticker.index = df_ticker.index.strftime("%Y%m%d")
    
    # Fixing some of the problems with yf when it returns a df
    # making the df no longer multi-index --> honestly don't fully understand this part
    
    df_ticker.columns = df_ticker.columns.get_level_values(0)
    df_ticker = df_ticker.reset_index()
    df_ticker.columns.name = None
    df_ticker = df_ticker.set_index("Date")
    combined_df = pd.merge(df_factors, df_ticker, on="Date", how="inner")
    combined_df["Excess"] = combined_df["daily return"] - combined_df["RF"]
    return combined_df




