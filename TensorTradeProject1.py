import yfinance 
import pandas_ta  


TICKER = 'TTRD'  # TODO: replace this with your own ticker
TRAIN_START_DATE = '2024-02-09'  # TODO: replace this with your own start date
TRAIN_END_DATE = '2024-09-30'  # TODO: replace this with your own end date
EVAL_START_DATE = '2024-10-01'  # TODO: replace this with your own end date
EVAL_END_DATE = '2024-11-12'  # TODO: replace this with your own end date

yf_ticker = yfinance.Ticker(ticker=TICKER)

df_training = yf_ticker.history(start=TRAIN_START_DATE, end=TRAIN_END_DATE, interval="60m")
df_training - drop(['Dividends', 'Stock Splits'], axis=1, inplace=True)
df_training["Volume"] = df_training["Volume"].astype(int)
df_training.ta.log_return(append=True, length=16)
df_training.ta.rsi(append=True, length=14)
df_training.ta.macd(append=True, fast=12, slow=26)
df_training.to_csv('training.csv', index=False)

d_evaluation = yf_ticker.history(start=EVAL_START_DATE, end=EVAL_END_DATE, interval="60m")
df_evaluation.drop(['Dividends', 'Stock Splits'], axis=1, inplace=True)
d_evaluation["Volume"] = d_evaluation["Volume"].astype(int)
df_evaluation.ta.log_return(append=True, length=16)
df_evaluation.ta.rsi(append=True, length=14)
d_evaluation.ta.macd(append=True, fast=12, slow=26)
df_evaluation.to_csv('evaluation.csv', index=False)
