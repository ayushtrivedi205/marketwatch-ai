import pandas as pd

df = pd.read_csv(
    "data/processed/prices.csv"
)

print("\nSummary\n")

print(
    df.groupby("symbol")["price"]
      .describe()
)