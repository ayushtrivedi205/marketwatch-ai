# 📊 MarketWatch AI

A real-time cryptocurrency analytics platform that performs live data collection, anomaly detection, arbitrage opportunity discovery, and price forecasting using Python, PostgreSQL, and Streamlit.

---

## 🚀 Live Demo

> *(Add this after deployment to Streamlit Cloud)*
> https://your-app-url.streamlit.app

---

## 📌 Overview

MarketWatch AI is a full-stack data analytics project that simulates a real-world financial monitoring system. It collects live cryptocurrency prices from multiple APIs, stores them in a PostgreSQL database, and visualizes insights through an interactive Streamlit dashboard.

It demonstrates **end-to-end data engineering + analytics workflow**:

```
Data Collection → Database → Processing → Analytics → Dashboard
```

---

## ✨ Features

### 📡 Real-Time Data Pipeline

* Fetches live crypto prices (BTC, ETH, SOL)
* Stores time-series data in PostgreSQL
* Auto-refreshing data pipeline

### 📊 Analytics Engine

* Price history visualization
* Moving trends analysis
* KPI metrics (total records, average price, tracked coins)

### 🚨 Anomaly Detection

* Z-score based anomaly detection
* Automatic alert generation
* Stores alerts in PostgreSQL

### 💰 Arbitrage Detection

* Compares Binance vs CoinGecko prices
* Identifies price discrepancies across platforms

### 📈 Forecasting

* ARIMA-based time series forecasting
* Predicts short-term BTC price movement
* Visual comparison of historical vs predicted data

### 📋 Monitoring Dashboard

* Streamlit interactive UI
* Live prices dashboard
* Alert history tracking
* Downloadable dataset

---

## 🧠 Tech Stack

* Python 🐍
* Pandas
* PostgreSQL 🛢️
* SQLAlchemy
* Streamlit 📊
* Plotly
* Statsmodels (ARIMA)
* Requests (API handling)

---

## 🏗️ Project Architecture

```
                +------------------+
                |  Crypto APIs     |
                | (Binance, CG)    |
                +--------+---------+
                         |
                         v
                +------------------+
                | Data Collector   |
                +------------------+
                         |
                         v
                +------------------+
                | PostgreSQL DB    |
                +------------------+
                         |
        +----------------+----------------+
        |                                 |
        v                                 v
+------------------+           +----------------------+
| Analytics Engine |           | Streamlit Dashboard |
| - Anomaly Detect |           | - Charts            |
| - Arbitrage      |           | - KPIs              |
| - Forecasting    |           | - Alerts            |
+------------------+           +----------------------+
```

---

## 📁 Project Structure

```
marketwatch-ai/
│
├── analysis/          # Analytics logic (forecast, anomalies, arbitrage)
├── dashboard/         # Streamlit dashboard
├── database/          # DB connection & setup
├── scrapers/          # API data collectors
├── data/              # Processed datasets
├── sql/               # SQL schema (optional)
├── main.py            # Data pipeline entry point
└── scheduler.py       # Auto data collection (optional)
```

---

## ⚙️ Installation

### 1. Clone repository

```bash
git clone https://github.com/ayushtrivedi205/marketwatch-ai.git
cd marketwatch-ai
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🛢️ Database Setup

Create PostgreSQL database:

```sql
CREATE DATABASE marketwatch;
```

Update credentials in:

```
database/db.py
```

---

## ▶️ Running the Project

### 1. Start data collection

```bash
python main.py
```

### 2. (Optional) Run auto scheduler

```bash
python scheduler.py
```

### 3. Launch dashboard

```bash
streamlit run dashboard/app.py
```

---

## 📊 Key Insights

* Detects abnormal price spikes using statistical methods
* Finds arbitrage opportunities between exchanges
* Provides short-term BTC price forecasts
* Tracks live crypto market movements in real time

---

## 📌 Future Improvements

* Email/SMS alert notifications
* Docker deployment
* More exchanges (Coinbase, Kraken)
* Advanced ML forecasting models (LSTM)
* Cloud deployment (AWS / GCP)

---

## 🧑‍💻 Author

**Ayush Trivedi**
Aspiring Data Analyst

---

