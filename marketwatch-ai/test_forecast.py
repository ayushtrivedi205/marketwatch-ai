import pandas as pd

from analysis.forecast import (
    forecast_prices
)

df = pd.read_csv(
    "data/processed/prices.csv"
)

btc = df[
    df["symbol"] == "BTCUSDT"
]["price"]

result = forecast_prices(btc)

print(result)