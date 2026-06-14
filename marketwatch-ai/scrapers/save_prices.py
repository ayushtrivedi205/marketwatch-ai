import pandas as pd
import os
from datetime import datetime


def save_prices(data):

    df = pd.DataFrame(data)

    coins = [
        "BTCUSDT",
        "ETHUSDT",
        "SOLUSDT"
    ]

    df = df[df["symbol"].isin(coins)]

    df["price"] = df["price"].astype(float)

    df["timestamp"] = datetime.now()

    os.makedirs("data/processed", exist_ok=True)

    file_path = "data/processed/prices.csv"

    if os.path.exists(file_path):
        df.to_csv(
            file_path,
            mode="a",
            header=False,
            index=False
        )
    else:
        df.to_csv(
            file_path,
            index=False
        )

    return df