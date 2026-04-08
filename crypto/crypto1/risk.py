# ------------------------------------------------------------
# RISK ANALYSIS MODULE
# ------------------------------------------------------------

import requests
import statistics
import time

COINS = ["bitcoin", "ethereum", "cardano", "solana", "ripple"]


# ------------------------------------------------------------
# Fetch Crypto Prices
# ------------------------------------------------------------

def fetch_crypto_prices(coin):

    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"

    params = {
        "vs_currency": "usd",
        "days": 30
    }

    try:
        response = requests.get(url, params=params)

        response.raise_for_status()

        data = response.json()

        # Check if prices exist in response
        if "prices" not in data:
            print("API Error:", data)
            return []

        prices = [price[1] for price in data["prices"]]

        return prices

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
        return []


# ------------------------------------------------------------
# Calculate Daily Returns
# ------------------------------------------------------------

def calculate_returns(prices):

    returns = []

    for i in range(1, len(prices)):

        change = (prices[i] - prices[i-1]) / prices[i-1]

        returns.append(change)

    return returns

# ------------------------------------------------------------
# Expected Return
# ------------------------------------------------------------

def calculate_expected_return(returns):

    if len(returns) == 0:
        return 0

    expected_return = sum(returns) / len(returns)

    return expected_return


# ------------------------------------------------------------
# Calculate Volatility (Risk)
# ------------------------------------------------------------

def calculate_volatility(returns):

    if len(returns) > 1:
        return statistics.stdev(returns)

    return 0


# ------------------------------------------------------------
# Risk Classification
# ------------------------------------------------------------

def classify_risk(volatility):

    if volatility < 0.005:
        return "Low Risk"

    elif volatility < 0.01:
        return "Medium Risk"

    else:
        return "High Risk"


# ------------------------------------------------------------
# Main Risk Analysis
# ------------------------------------------------------------

def main():

    print("\n----- CRYPTO RISK ANALYSIS -----\n")

    for coin in COINS:

        print("Analyzing", coin.capitalize(), "...")

        prices = fetch_crypto_prices(coin)

        # Skip if no data
        if not prices:
            print("No data available\n")
            continue

        returns = calculate_returns(prices)

        volatility = calculate_volatility(returns)

        risk_level = classify_risk(volatility)

        print("Volatility:", round(volatility,6))

        print("Risk Level:", risk_level)

        print("-----------------------------\n")

        # Prevent API rate limit
        time.sleep(5)


# ------------------------------------------------------------

if __name__ == "__main__":
    main()