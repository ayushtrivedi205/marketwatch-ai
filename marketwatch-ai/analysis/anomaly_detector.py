import pandas as pd


def detect_anomalies(df):

    alerts = []

    # Ensure chronological order
    df = df.sort_values("timestamp")

    for symbol in df["symbol"].unique():

        coin_df = (
            df[df["symbol"] == symbol]
            .sort_values("timestamp")
            .copy()
        )

        # Need enough observations
        if len(coin_df) < 10:
            continue

        # Use only recent data
        recent_prices = coin_df["price"].tail(20)

        mean_price = recent_prices.mean()
        std_price = recent_prices.std()

        latest_price = recent_prices.iloc[-1]

        if std_price == 0 or pd.isna(std_price):
            continue

        z_score = (
            latest_price - mean_price
        ) / std_price

        # Trigger alert if abnormal
        if abs(z_score) > 2:

            alert_type = (
                "Price Spike"
                if z_score > 0
                else "Price Drop"
            )

            alerts.append({
                "symbol": symbol,
                "current_price": round(float(latest_price), 2),
                "rolling_mean": round(float(mean_price), 2),
                "z_score": round(float(z_score), 2),
                "alert_type": alert_type
            })

    return alerts