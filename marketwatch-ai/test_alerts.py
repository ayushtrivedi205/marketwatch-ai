from analysis.save_alerts import save_alerts

sample_alerts = [
    {
        "symbol": "BTCUSDT",
        "current_price": 64000,
        "rolling_mean": 62000,
        "z_score": 2.5
    }
]

save_alerts(sample_alerts)

print("Alert saved")