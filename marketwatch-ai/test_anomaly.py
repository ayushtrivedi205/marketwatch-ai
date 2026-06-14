import pandas as pd

from analysis.anomaly_detector import (
    detect_anomalies
)

df = pd.read_csv(
    "data/processed/prices.csv"
)

alerts = detect_anomalies(df)

print("\nANOMALY ALERTS\n")

for alert in alerts:
    print(alert)