import pandas as pd

df = pd.read_csv("data/processed/prices.csv")

print(
    df[df["symbol"] == "BTCUSDT"]
    [["timestamp", "price"]]
    .tail(10)
)