def find_arbitrage(binance_df, coingecko_data):
    """
    Compare prices between Binance and CoinGecko to find arbitrage opportunities.
    Returns a list of dicts with symbol, binance_price, coingecko_price, diff_pct.
    """
    symbol_map = {
        "BTCUSDT": "bitcoin",
        "ETHUSDT": "ethereum",
        "SOLUSDT": "solana",
    }

    results = []

    for _, row in binance_df.iterrows():
        symbol = row["symbol"]
        cg_id = symbol_map.get(symbol)

        if cg_id and cg_id in coingecko_data:
            binance_price = float(row["price"])
            cg_price = float(coingecko_data[cg_id]["usd"])
            diff_pct = ((binance_price - cg_price) / cg_price) * 100

            results.append({
                "symbol": symbol,
                "binance_price": binance_price,
                "coingecko_price": cg_price,
                "diff_pct": round(diff_pct, 4),
            })

    return results
