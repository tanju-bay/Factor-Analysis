import pandas as pd
import numpy as np
import yfinance as yf
import statsmodels.api as sm
import matplotlib.pyplot as plt
import plots as p
import regressions as r
import data_pull as dp
import attribution_analysis as a
def main(ticker):
    combined_df = dp.data_pull(ticker)
    r.regression(combined_df, ticker) # This writes regression results to txt file
    betas, alphas, contrib_rolling = r.rolling_regression(combined_df)
    attribution = a.attribution_analysis(betas, alphas, combined_df)
    composition = a.composition_analysis(betas, combined_df)
    p.composition(composition, ticker)
    #p.rolling_attribution(contrib_rolling, ticker)
    p.cross_sectional_attribution(attribution, ticker)
main(ticker="SPY")