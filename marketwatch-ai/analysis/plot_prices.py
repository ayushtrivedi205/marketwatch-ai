import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/prices.csv"
)

df["timestamp"] = pd.to_datetime(
    df["timestamp"]
)

btc = df[df["symbol"] == "BTCUSDT"]

plt.plot(
    btc["timestamp"],
    btc["price"]
)

plt.title("BTC Price History")

plt.show()