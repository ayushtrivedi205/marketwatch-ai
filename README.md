
# 📈 MarketWatch AI

A real-time cryptocurrency market monitoring and analysis dashboard built with Python and Streamlit. Tracks live prices from Binance and CoinGecko, detects anomalies, forecasts trends, and identifies arbitrage opportunities.

---

## 🚀 Features

- **Live Price Tracking** — Fetches real-time BTC, ETH, and SOL prices from Binance
- **Price History Charts** — Interactive Plotly charts with historical data
- **Anomaly Detection** — Z-score based alerts for unusual price movements
- **Arbitrage Detection** — Compares Binance vs CoinGecko prices to find spreads
- **Price Forecasting** — Moving average + linear trend forecasting
- **Auto Refresh** — Dashboard auto-updates every 60 seconds
- **Data Export** — Download all tracked data as CSV
- **PostgreSQL Storage** — Persists all price data to a local database

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** — Dashboard UI
- **Pandas / NumPy** — Data processing
- **Plotly** — Interactive charts
- **SQLAlchemy + PostgreSQL** — Database
- **Scikit-learn** — Forecasting
- **Requests** — API calls (Binance, CoinGecko)

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/ayushtrivedi205/marketwatch-ai.git
cd marketwatch-ai
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
.\venv\Scripts\Activate.ps1

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the database

Open `database/db.py` and update your PostgreSQL credentials:
```python
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "marketwatch"
```

Make sure you have PostgreSQL running and a database named `marketwatch` created.

### 5. Collect some data first
```bash
python main.py
```

### 6. Run the dashboard
```bash
streamlit run dashboard/app.py
```

Open your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
marketwatch-ai/
├── main.py                  # Entry point — fetch and save prices
├── requirements.txt
│
├── scrapers/
│   ├── binance.py           # Fetch prices from Binance API
│   ├── coingecko.py         # Fetch prices from CoinGecko API
│   └── save_prices.py       # Save prices to CSV
│
├── database/
│   ├── db.py                # Database connection
│   └── load_prices.py       # Save prices to PostgreSQL
│
├── analysis/
│   ├── arbitrage.py         # Arbitrage detection logic
│   ├── forecast.py          # Price forecasting
│   ├── anomaly_detector.py  # Z-score anomaly detection
│   ├── save_alerts.py       # Save alerts to JSON
│   ├── load_alerts.py       # Load alerts from database
│   ├── get_data.py          # Load price history from DB
│   └── db_metrics.py        # Database summary metrics
│
├── dashboard/
│   └── app.py               # Streamlit dashboard
│
└── data/
    └── processed/
        └── prices.csv       # Local CSV backup of prices
```

---

## 📊 How It Works

1. `main.py` calls the Binance API, filters BTC/ETH/SOL prices, and saves them to both CSV and PostgreSQL
2. The Streamlit dashboard reads from PostgreSQL and displays live metrics, charts, and analysis
3. Every 60 seconds the dashboard auto-refreshes to show the latest data
4. Anomalies are detected using a rolling Z-score and saved as alerts

---

## 🧪 Running Tests

```bash
python test_coingecko.py      # Test CoinGecko API connection
python test_arbitrage.py      # Test arbitrage detection
python test_forecast.py       # Test price forecasting
python test_alerts.py         # Test alert saving
```

---

## 📌 Notes

- CoinGecko free tier has rate limits — if you see empty arbitrage data, wait a minute and refresh
- Make sure PostgreSQL is running before launching the dashboard
- Run `python main.py` periodically (or set up a scheduler) to keep data fresh

---

## 👤 Author

**Ayush Trivedi**
[GitHub](https://github.com/ayushtrivedi205)

---
