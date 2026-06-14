import numpy as np


def forecast_prices(series, steps=5):
    """
    Simple moving-average-based price forecast.
    Takes a pandas Series of prices and returns a list of forecasted values.
    """
    if len(series) < 2:
        return []

    prices = series.dropna().values
    window = min(5, len(prices))
    moving_avg = float(np.mean(prices[-window:]))

    # Compute simple linear trend from last window
    if len(prices) >= window:
        x = np.arange(window)
        y = prices[-window:]
        slope = float(np.polyfit(x, y, 1)[0])
    else:
        slope = 0.0

    forecast = [round(moving_avg + slope * (i + 1), 4) for i in range(steps)]
    return forecast
