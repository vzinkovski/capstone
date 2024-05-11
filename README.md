Please follow this **[link](https://github.com/vzinkovski/umich_siads_capstone/blob/main/FORECASTING%20DAILY%20RETURNS%20FOR%20S%26P%20500%20CONSTITUENTS%20%26%20IMPLEMENTING%20A%20TRADING%20STRATEGY.pdf)** to view the full project.

---

## FORECASTING DAILY RETURNS FOR S&P 500 CONSTITUENTS & IMPLEMENTING A TRADING STRATEGY
*Authors: Takehisa Kanayama & Vladimir Zinkovski*
 
*Publication date: April 2024*

### Introduction

This project seeks to forecast daily returns for S&P 500 constituent companies. The forecast period is one-day ahead and approached as a binary classification task where we label positive returns as the positive class, and negative or zero returns as the negative class. We use two datasets to extract features that may be predictive of future returns. First, the open, high, low and closing prices, and trading volume data from Yahoo! Finance. Second, various macroeconomic indicators pertaining to the US economy from the Federal Reserve Economic Data (FRED). We use data from 2000 until 2023, which is split 18/3/3 years (i.e. 75%/12.5%/12.5%) for training/validation/testing. Using a long time horizon allows us to cover multiple black swan events, such as, for example, the dotcom bubble in 2000-2002, GFC in 2008-9, and COVID-related crash in 2020 and subsequent V-shaped recovery in 2021-22. Our intention is that incorporating outlier events into our data will result in more robust machine learning models. We train and tune three individual models using different underlying algorithms, which are then combined into two different ensemble models. Finally, we employ the best performing model into a simple trading strategy where if we predict the next day’s returns as positive, we buy for a holding period of one day.

### Results

The following table summarizes individual and ensemble model performance versus a benchmark DummyClassifier. The average highest precision score over the validation set is achieved by the VotingClassifier at 0.556 (lower bound at 0.507). However, when accounting for standard deviation, the absolute highest lower bound is achieved by the RandomForest at 0.512. We select the RandomForest, further optimize its decision threshold such that gross cumulative percentage equity returns are maximized, then use this best model upon which to build our trading strategy. Lastly, our best model also managed to achieve a higher precision score than the DummyClassifier on the out-of-sample test set.


![Precision Scores](https://raw.githubusercontent.com/vzinkovski/umich_siads_capstone/main/precision_scores.png)


The below chart shows the performance of our trading strategy versus a naive buy-and-hold trading strategy. Our strategy failed to outperform its benchmark, the S&P 500, particularly underperforming during bull market years. However, our simple trading model was nevertheless able to break-even over the 3-year test period from 2021-2023 and present a plausible starting point for further work.


![Trading Performance](https://raw.githubusercontent.com/vzinkovski/umich_siads_capstone/main/trading_performance.png)


### Conclusion

Despite deriving our model features from just two – exhaustively mined – data sources, we were nevertheless able to build a machine learning model which outperformed the benchmark DummyClassifier in both the validation and test sets. Although more complex ensemble models did indeed result in higher precision scores, these were, somewhat counterintuitively, coupled with a higher standard deviation. As a result, the RandomForest was our best performing model.

However, our subsequent trading strategy was not able to outperform a simple buy-and-hold trading strategy, underperforming specifically during bull market years. Even though our trading strategy trailed its benchmark, it did manage to break even. As such, this can be considered a reasonable initial prototype trading model which may benefit from further refinements such as weighted capital allocation, scaling in and out of positions, and variable holding periods, among others.

Finally, ingesting data from additional sources, particularly non-traditional sources (e.g. satellite imagery, text, etc.), applying further feature engineering, and more nuanced feature selection, may all lead to additional performance gains and are potential areas for further work.

### How to run the code?

Our work has been fully produced in the Jupyter Notebook format using the Python language. This format encourages reproducibility of results and we encourage the reader to download a copy and experiment with the code. Please follow this **[link](https://nbviewer.org/github/vzinkovski/umich_siads_capstone/blob/main/forecast_sp500_returns.ipynb)** to view the complete project.

### Data access statement

All data used in this project can be freely accessed from the below two sources in order to allow for reproducibility of results.

**yfinance**: An open-source tool that uses Yahoo's publicly available APIs and is intended for research and educational purposes. Please refer to Yahoo!'s terms of use ([here](https://legal.yahoo.com/us/en/yahoo/terms/product-atos/apiforydn/index.html), [here](https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html), and [here](https://policies.yahoo.com/us/en/yahoo/terms/index.htm)) for details on your rights to use the actual data downloaded. Note that the Yahoo! Finance API is intended for personal use only. Links to [PyPi](https://pypi.org/project/yfinance/) and [GitHub](https://github.com/ranaroussi/yfinance).

**fredapi**: A Python API for the [FRED](https://fred.stlouisfed.org/) data provided by the Federal Reserve Bank of St. Louis. In order to use the API you can use the following, freely available & non-personal, API key: *a74d505e6731a2b5b06fdcf6ca20f6f5*, or [apply for one](https://fred.stlouisfed.org/docs/api/api_key.html) for free on the FRED website. This API is made available under a permissive, open-source Apache-2.0 license. Links to [PyPi](https://pypi.org/project/fredapi/) and [GitHub](https://github.com/mortada/fredapi).

### Libraries

What follows are the main libraries used in this project. For a complete list, including dependencies, please refer to the requirements.txt file.

- seaborn   : 0.13.1
- torch     : 2.2.1+cu121
- yfinance  : 0.2.37
- numpy     : 1.25.2
- lightgbm  : 4.1.0
- talib     : 0.4.28
- requests  : 2.31.0
- matplotlib: 3.7.1
- fredapi   : 0.5.1
- pandas    : 2.0.3
- sklearn   : 1.2.2
- skorch    : 0.15.0
- optuna    : 3.6.1
