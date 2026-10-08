import pandas as pd
import numpy as np
import yfinance as yf
import statsmodels.api as sm
import matplotlib.pyplot as plt

def attribution_analysis(betas, alphas, return_df):

    factors = ["Mkt-RF", "SMB", "HML", "RMW", "CMA", "MOM"]
    lookback = 252 * 1
    end_date = return_df.index[-1]
    start_date = return_df.index[-lookback]

    # set years to whatever period desired
    
    betas_atr = betas.loc[start_date:end_date]
    alphas_atr = alphas.loc[start_date:end_date]
    factors_atr = return_df.loc[start_date:end_date, factors]
    excess_atr = return_df.loc[start_date: end_date, "Excess"]

    factor_contribution = betas_atr.mul(factors_atr).sum()
    alpha_contribution = alphas_atr.sum()
    residual_contribution = (excess_atr.sum() - factor_contribution.sum() - alpha_contribution)

    attribution = factor_contribution.copy()
    attribution["Alpha"] = alpha_contribution
    attribution["Residual"] = residual_contribution

    attribution = attribution.astype(float)
    return attribution
def composition_analysis(betas,return_df):

    lookback = 252
    factors = ["Mkt-RF", "SMB", "HML", "RMW", "CMA", "MOM"]
    end_date = return_df.index[-1]
    start_date = return_df.index[-lookback]
    betas_lookback = betas.loc[start_date:end_date]
    avg_betas = betas_lookback.mean()
    return avg_betas