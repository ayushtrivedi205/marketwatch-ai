import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )))

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import time

from analysis.save_alerts import save_alerts
from analysis.db_metrics import get_metrics
from analysis.forecast import forecast_prices
from analysis.load_alerts import load_alerts
from analysis.get_data import load_data
from analysis.arbitrage import find_arbitrage
from analysis.anomaly_detector import detect_anomalies

from scrapers.coingecko import get_coingecko_prices

# -----------------
# PAGE CONFIG
# -----------------

st.set_page_config(
    page_title="MarketWatch AI",
    layout="wide"
)

# -----------------
# AUTO REFRESH
# -----------------

# Auto-refresh every 60 seconds using native Streamlit
if "last_refresh" not in st.session_state:
    st.session_state.last_refresh = time.time()

if time.time() - st.session_state.last_refresh > 60:
    st.session_state.last_refresh = time.time()
    st.rerun()

st.title("📈 MarketWatch AI")

st.write(
    "Last Refresh:",
    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

# -----------------
# LOAD DATA
# -----------------

df = load_data()

df["timestamp"] = pd.to_datetime(
    df["timestamp"]
)

# -----------------
# KPI CARDS
# -----------------

metrics = get_metrics()

st.subheader("Database Metrics")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Total Records",
    metrics["records"]
)

c2.metric(
    "Tracked Coins",
    metrics["coins"]
)

c3.metric(
    "Average Price",
    round(metrics["avg_price"], 2)
)

# -----------------
# LATEST PRICES
# -----------------

latest = (
    df.sort_values("timestamp")
      .groupby("symbol")
      .tail(1)
)

st.subheader("Live Prices")

col1, col2, col3 = st.columns(3)

btc = latest[
    latest["symbol"] == "BTCUSDT"
]["price"].values[0]

eth = latest[
    latest["symbol"] == "ETHUSDT"
]["price"].values[0]

sol = latest[
    latest["symbol"] == "SOLUSDT"
]["price"].values[0]

col1.metric(
    "BTC",
    f"${btc:,.2f}"
)

col2.metric(
    "ETH",
    f"${eth:,.2f}"
)

col3.metric(
    "SOL",
    f"${sol:,.2f}"
)

# -----------------
# PRICE HISTORY
# -----------------

st.subheader("Price History")

coin = st.selectbox(
    "Select Coin",
    ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
)

coin_df = (
    df[df["symbol"] == coin]
    .sort_values("timestamp")
)

fig = px.line(
    coin_df,
    x="timestamp",
    y="price",
    title=f"{coin} Price History",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------
# ANOMALIES
# -----------------

st.subheader("🚨 Anomaly Alerts")

alerts = detect_anomalies(df)

if len(alerts) == 0:

    st.success(
        "No anomalies detected"
    )

else:

    save_alerts(alerts)

    st.dataframe(
        pd.DataFrame(alerts)
    )

# -----------------
# ARBITRAGE
# -----------------

st.subheader("💰 Arbitrage Opportunities")

cg = get_coingecko_prices()

arb_df = find_arbitrage(
    latest,
    cg
)

if len(arb_df) == 0:

    st.success(
        "No arbitrage opportunities"
    )

else:

    st.dataframe(
        arb_df
    )

# -----------------
# FORECAST
# -----------------

st.subheader("📈 BTC Forecast")

btc_df = (
    df[df["symbol"] == "BTCUSDT"]
    .sort_values("timestamp")
    .copy()
)

forecast = forecast_prices(
    btc_df["price"]
)

if forecast is not None:

    history_df = btc_df.tail(30).copy()

    future_df = pd.DataFrame({
        "price": forecast
    })

    future_df["timestamp"] = [
        f"Forecast {i + 1}"
        for i in range(len(future_df))
    ]

    history_chart = history_df[
        ["timestamp", "price"]
    ].copy()

    history_chart["type"] = "Historical"

    future_chart = future_df.copy()

    future_chart["type"] = "Forecast"

    chart_df = pd.concat(
        [
            history_chart,
            future_chart
        ]
    )

    fig = px.line(
        chart_df,
        x="timestamp",
        y="price",
        color="type",
        title="BTC Historical + Forecast"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.warning(
        "Not enough data for forecasting."
    )

# -----------------
# DATA OVERVIEW
# -----------------

st.subheader("Dataset Overview")

st.dataframe(
    df.tail(20)
)

# -----------------
# DOWNLOAD DATA
# -----------------

csv = df.to_csv(
    index=False
)

st.download_button(
    "📥 Download Data",
    csv,
    "marketwatch_data.csv",
    "text/csv"
)

# -----------------
# ALERT HISTORY
# -----------------

st.subheader("📋 Alert History")

alerts_df = load_alerts()

st.dataframe(
    alerts_df
)