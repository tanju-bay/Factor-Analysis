# Factor-Analysis
This project is a Factor Exposure Analyzer designed to evaluate the risk and return characteristics of ETFs and other publicly traded securities using a multi-factor asset pricing framework. The model pulls historical market data and applies the Fama-French Five-Factor Model plus Momentum to estimate each security’s exposure to key systematic risk factors, including market, size, value, profitability, investment, and momentum.

The project also provides tools for analyzing how these factor exposures change over time through rolling regressions, factor contribution analysis, and performance attribution. By separating returns into factor-driven performance, alpha, and residual components, the analyzer helps users better understand what is driving an investment’s returns and the underlying factor risks embedded within a portfolio or ETF.

To use the model input your desired ETF or Equity ticker as the argument for the main function under file "main.py"

Important Notes:

The current factor dataset is static, and is currently only updated to August, 31st 2026. This dataset was pulled from the Dartmouth Fama French data library, link here: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html and is updated approximately monthly. I recommend downloading the most recent factor returns and locally running this script, making sure to change the dates in the datapull for the most up to date results. Other factor datasets are provided by large data brokers such as S&P, Fitch, etc. but normally require a paid subscription

The rolling attribution function is still underprogress
