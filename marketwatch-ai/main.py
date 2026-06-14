from scrapers.binance import get_binance_prices
from scrapers.save_prices import save_prices
from database.load_prices import save_to_database

data = get_binance_prices()

df = save_prices(data)

save_to_database(df)

print(df)