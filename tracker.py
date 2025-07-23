import time
import requests
import pandas as pd
import matplotlib.pyplot as plt

COINS = ["bitcoin", "ethereum", "solana", "dogecoin", "cardano"]
API_URL = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(COINS)}&vs_currencies=usd"

def fetch_prices():
    response = requests.get(API_URL)
    data = response.json()
    prices = {coin: data[coin]["usd"] for coin in COINS}
    return prices

def save_to_csv(prices, filename="crypto_prices.csv"):
    df = pd.DataFrame(prices.items(), columns=["Coin", "Price (USD)"])
    df["Timestamp"] = pd.Timestamp.now()
    df.to_csv(filename, index=False)
    print(f"[✓] Saved to {filename}")

def plot_prices(prices):
    plt.figure(figsize=(8, 4))
    plt.bar(prices.keys(), prices.values())
    plt.title("Crypto Prices (USD)")
    plt.ylabel("Price")
    plt.tight_layout()
    plt.savefig("crypto_prices_chart.png")
    plt.show()

if __name__ == "__main__":
    while True:
        print("⏳ Fetching latest prices...")
        prices = fetch_prices()
        save_to_csv(prices)
        plot_prices(prices)
        print("Sleeping 5 minutes...\n")
        time.sleep(300)
