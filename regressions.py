import pandas as pd
import numpy as np
import yfinance as yf
import statsmodels.api as sm
import matplotlib.pyplot as plt

def regression(combined_df, ticker_name):
    # Create a new df that splits the x components & y components
    x = combined_df[["Mkt-RF", "SMB", "HML", "RMW", "CMA", "MOM"]]
    y = combined_df[["daily return"]]

    # Make sure to add the constant -- this is essentially the residuals + alpha
    x = sm.add_constant(x)
    model = sm.OLS(y,x).fit()

    # send results to a seperate file
    with open("simple_regression_results.txt", "w") as f:
        print(f"Ticker: {ticker_name} \n", file=f)
        print(f"{model.summary()}", file=f)

        
def rolling_regression(df):
    # Need to calculate the excess return
    df["Excess"] = df["daily return"] - df["RF"]
    window = 252 #~252 trading days in  a year

    factors = ["Mkt-RF", "SMB", "HML", "RMW", "CMA", "MOM"]

    # making two empty containers to store data
    betas = pd.DataFrame(index=df.index, columns=factors, dtype=float)
    alphas = pd.Series(index=df.index, dtype=float)
    # need to take the rolling average of the associated betas
    for end in range(window, len(df)+1):
        window_df = df.iloc[end-window: end]

        y = window_df["Excess"]
        X = sm.add_constant(window_df[factors])

        res = sm.OLS(y,X).fit()

        betas.iloc[end-1] = res.params[factors]
        alphas.iloc[end-1] = res.params["const"]
    # multiply the betas times their factor return contribution
    contrib_daily = betas.mul(df[factors], axis =0)
    # Add on the alpha series to new dataframe
    contrib_daily["Alpha"] = alphas
    # We are calculating the residuals by removing the factor returns from ticker
    contrib_daily["Residual"] = df["Excess"] - contrib_daily[factors].sum(axis=1) - contrib_daily["Alpha"]
    # Calculate the 1Y cumulative contribution
    contrib_rolling = contrib_daily[factors + ['Alpha', 'Residual']].rolling(window).sum()
    # Dataframe with contribution to rolling averages
    return betas, alphas, contrib_rolling