# 💰 Crypto Price Tracker (CoinGecko API)

This Python script tracks the live price of five popular cryptocurrencies using the free [CoinGecko API](https://www.coingecko.com/en/api) and:

- Saves prices with timestamps to a CSV file
- Generates a bar chart of current prices
- Updates every 5 minutes automatically

---

## 🚀 What It Does

- Connects to CoinGecko's API
- Fetches USD prices for:
  - Bitcoin
  - Ethereum
  - Solana
  - Dogecoin
  - Cardano
- Saves the prices and timestamp to `crypto_prices.csv`
- Displays and saves a bar chart as `crypto_prices_chart.png`
- Runs continuously, updating every 5 minutes

---

## ✅ Example Use Cases

- Crypto dashboard monitoring
- Automated price tracking for reports
- CSV data analysis for trends
- Building future trading tools

---

## 🛠 Setup Instructions

1. **Clone this repo**:
   ```bash
   git clone https://github.com/yourusername/crypto-price-tracker.git
   cd crypto-price-tracker
