import requests
import csv

API_URL = "https://api.coingecko.com/api/v3/coins/markets"
SNAPSHOT_CSV = "market_snapshot.csv"

def fetch_market_data():
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": "false"
    }

    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    return response.json()

def save_to_csv(data):
    with open(SNAPSHOT_CSV, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["coin_id", "name", "current_price", "market_cap"])

        for coin in data:
            writer.writerow([
                coin["id"],
                coin["name"],
                coin["current_price"],
                coin["market_cap"]
            ])

def main():
    print("Fetching market data...")
    data = fetch_market_data()
    save_to_csv(data)
    print("Market data saved to market_snapshot.csv")

if __name__ == "__main__":
    main()