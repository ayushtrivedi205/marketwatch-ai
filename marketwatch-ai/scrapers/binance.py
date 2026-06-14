import requests

def get_binance_prices():

    url = "https://api.binance.com/api/v3/ticker/price"

    response = requests.get(
        url,
        timeout=10
    )

    response.raise_for_status()

    return response.json()