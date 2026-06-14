import time

from scrapers.binance import get_binance_prices
from scrapers.save_prices import save_prices

while True:

    try:

        data = get_binance_prices()

        save_prices(data)

        print("Saved Successfully")

    except Exception as e:

        print(f"Error: {e}")

    time.sleep(60)