# ------------------------------------------------------------
# EDA PORTFOLIO ANALYSIS WITH VISUALIZATION + FINANCIAL METRICS
# ------------------------------------------------------------

import requests
import statistics
import time
import matplotlib.pyplot as plt
from prediction import predict_next_price
TOTAL_INVESTMENT = 10000
RISK_FREE_RATE = 0.01

COINS = ["bitcoin", "ethereum", "cardano", "solana", "ripple"]


# ------------------------------------------------------------
# STEP 1: Fetch 30-Day Historical Prices
# ------------------------------------------------------------

def fetch_historical_prices(coin_id):

    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"

    params = {
        "vs_currency": "usd",
        "days": 30
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    prices = [price_point[1] for price_point in data["prices"]]

    return prices


# ------------------------------------------------------------
# STEP 2: Calculate Returns
# ------------------------------------------------------------

def calculate_returns(prices):

    returns = []

    for i in range(1, len(prices)):
        r = (prices[i] - prices[i-1]) / prices[i-1]
        returns.append(r)

    return returns


# ------------------------------------------------------------
# STEP 3: Expected Return
# ------------------------------------------------------------

def calculate_expected_return(returns):

    if len(returns) > 0:
        return statistics.mean(returns)

    return 0


# ------------------------------------------------------------
# STEP 4: Volatility (Risk)
# ------------------------------------------------------------

def calculate_volatility(returns):

    if len(returns) > 1:
        return statistics.stdev(returns)

    return 0


# ------------------------------------------------------------
# STEP 5: Sharpe Ratio
# ------------------------------------------------------------

def calculate_sharpe_ratio(expected_return, volatility):

    if volatility == 0:
        return 0

    sharpe = (expected_return - RISK_FREE_RATE) / volatility
    return sharpe


# ------------------------------------------------------------
# STEP 6: Risk Classification
# ------------------------------------------------------------

def classify_risk(volatility_data):

    sorted_coins = sorted(volatility_data.items(), key=lambda x: x[1])

    n = len(sorted_coins)

    risk_groups = {
        "low": [],
        "medium": [],
        "high": []
    }

    for i, (coin, vol) in enumerate(sorted_coins):

        if i < n/3:
            risk_groups["low"].append(coin)

        elif i < 2*n/3:
            risk_groups["medium"].append(coin)

        else:
            risk_groups["high"].append(coin)

    return risk_groups


# ------------------------------------------------------------
# STEP 7: Investment Allocation
# ------------------------------------------------------------

def allocate_investment(risk_groups):

    allocation_ratio = {
        "low": 0.5,
        "medium": 0.3,
        "high": 0.2
    }

    final_allocation = {}

    for level, coins in risk_groups.items():

        if coins:

            amount_per_coin = (TOTAL_INVESTMENT * allocation_ratio[level]) / len(coins)

            for coin in coins:
                final_allocation[coin] = round(amount_per_coin, 2)

    return final_allocation


# ------------------------------------------------------------
# VISUALIZATION FUNCTIONS
# ------------------------------------------------------------

def plot_price_trend(coin, prices):

    plt.figure()
    plt.plot(prices)
    plt.title(f"{coin.capitalize()} - 30 Day Price Trend")
    plt.xlabel("Days")
    plt.ylabel("Price (USD)")
    plt.show()


def plot_volatility(volatility_data):

    plt.figure()
    coins = list(volatility_data.keys())
    values = list(volatility_data.values())
    plt.bar(coins, values)
    plt.title("Volatility Comparison")
    plt.xlabel("Coins")
    plt.ylabel("Volatility")
    plt.xticks(rotation=45)
    plt.show()


def plot_allocation(final_mix):

    plt.figure()
    coins = list(final_mix.keys())
    amounts = list(final_mix.values())
    plt.pie(amounts, labels=coins, autopct="%1.1f%%")
    plt.title("₹10,000 Portfolio Allocation")
    plt.show()

def plot_prediction(prices, predicted_price):
    
    X = list(range(len(prices)))
    plt.plot(X, prices, label="Actual Prices")
    plt.scatter(len(prices), predicted_price, color="red", label="Predicted Price")
    plt.title("Price Prediction")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

# ------------------------------------------------------------
# MAIN EXECUTION
# ------------------------------------------------------------

def main():

    volatility_data = {}
    expected_returns = {}
    sharpe_ratios = {}
    print("----- EDA & PORTFOLIO ANALYSIS -----\n")

    for coin in COINS:

        try:

            prices = fetch_historical_prices(coin)
            plot_price_trend(coin, prices)
            returns = calculate_returns(prices)
            exp_return = calculate_expected_return(returns)
            volatility = calculate_volatility(returns)
            sharpe = calculate_sharpe_ratio(exp_return, volatility)
            predicted_price = predict_next_price(prices)
            plot_prediction(prices, predicted_price)
            volatility_data[coin] = volatility
            expected_returns[coin] = exp_return
            sharpe_ratios[coin] = sharpe

            print(f"{coin.upper()}")
            print("Expected Return:", round(exp_return,6))
            print("Volatility:", round(volatility,6))
            print("Sharpe Ratio:", round(sharpe,4))
            print("Predicted Next Price:", round(predicted_price,2))
            print("-----------------------------------")

            time.sleep(2)

        except Exception as e:
            print(f"Error for {coin}: {e}")
            time.sleep(5)

    if not volatility_data:
        print("No data available.")
        return


    # Plot volatility comparison
    plot_volatility(volatility_data)
    # Risk classification
    risk_groups = classify_risk(volatility_data)

    print("\nRisk Classification:")

    for level, coins in risk_groups.items():
        print(level.upper(), "RISK →", coins)


    # Portfolio allocation
    final_mix = allocate_investment(risk_groups)

    print("\nPortfolio Allocation (₹10,000):")

    for coin, amount in final_mix.items():

        weight = (amount / TOTAL_INVESTMENT) * 100
        print(f"{coin} → ₹{amount} | Weight: {round(weight,2)}%")


    # Pie chart
    plot_allocation(final_mix)
    print("\n----- ANALYSIS COMPLETE -----")
    
if __name__ == "__main__":
    main()