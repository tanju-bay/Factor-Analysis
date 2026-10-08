import pandas as pd
import numpy as np
import yfinance as yf
import statsmodels.api as sm
import matplotlib.pyplot as plt


def rolling_attribution(contribution_rolling,ticker):
    # Plots the rolling attributions
    contribution_rolling[["Mkt-RF", "SMB", "HML", "RMW", "CMA", "MOM"]].dropna().plot(kind='line', figsize=(12,6))
    plt.title(f'Rolling 252-Day Factor Contributions to {ticker} Excess Return')
    plt.ylabel("Cumulative Contribution (decimal return)")
    plt.show()
def rolling_alpha(contrib_rolling,ticker):
    contrib_rolling["Alpha"].dropna().plot(kind="line", figsize=(12,6))
    plt.title(f"Rolling {window}-Day Alpha for {ticker}")
    plt.ylabel("Alpha (decimal Return)")
    plt.show()
def rolling_residuals(contrib_rolling, ticker):
    contrib_rolling["Residual"].dropna().plot(kind="line", figsize=(12,6))
    plt.title(f'Rolling Residuals for {ticker}')
    plt.ylabel("Residuals")
    plt.show()
def cross_sectional_attribution(attribution,ticker):
    # Plot cumulative attribution
    colors = [
        "tab:blue",    # Mkt-RF
        "tab:orange",  # SMB
        "tab:green",   # HML
        "tab:pink",     # RMW
        "tab:purple",  # CMA
        "tab:brown",   # MOM
        "tab:red",    # Alpha
        "tab:gray"     # Residual
    ]
    fig, ax = plt.subplots(figsize=(12,6))
    ax.axhline(0)
    ax.bar(attribution.index, attribution.values, color=colors)

    ax.set_title(f"Factor Return Attribution for {ticker}")
    ax.set_ylabel("1Y Cumulative Excess Return)")
    plt.show()
def composition(composition, ticker):
    # Plot factor composition
    colors = [
        "tab:blue",    # Mkt-RF
        "tab:orange",  # SMB
        "tab:green",   # HML
        "tab:pink",     # RMW
        "tab:purple",  # CMA
        "tab:brown",   # MOM
        "tab:red",    # Alpha
        "tab:gray"     # Residual
    ]
    fig, ax = plt.subplots(figsize=(12,6))
    ax.bar(composition.index, composition.values, color=colors)
    ax.axhline(0)
    ax.set_title(f"Factor Composition {ticker}")
    ax.set_ylabel("Beta Exposure by Factor")
    plt.show()
