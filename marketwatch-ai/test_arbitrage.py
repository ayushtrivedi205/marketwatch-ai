from scrapers.binance import get_binance_prices
from scrapers.save_prices import save_prices

from scrapers.coingecko import (
    get_coingecko_prices
)

from analysis.arbitrage import (
    find_arbitrage
)

data = get_binance_prices()

df = save_prices(data)

cg = get_coingecko_prices()

results = find_arbitrage(
    df,
    cg
)

for r in results:
    print(r)