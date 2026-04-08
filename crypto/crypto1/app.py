import streamlit as st
import requests
import statistics
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.title(" Crypto Portfolio Analyzer")

TOTAL_INVESTMENT = 10000
RISK_FREE_RATE = 0.01
COINS = ["bitcoin", "ethereum", "cardano", "solana", "ripple"]


# -----------------------------------
# Fetch Historical Prices
# -----------------------------------

def fetch_historical_prices(coin):

    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"

    params = {
        "vs_currency": "usd",
        "days": 30
    }

    response = requests.get(url, params=params)
    data = response.json()
    prices = [p[1] for p in data["prices"]]
    return prices


# -----------------------------------
# Calculate Returns
# -----------------------------------

def calculate_returns(prices):

    returns = []

    for i in range(1, len(prices)):
        r = (prices[i] - prices[i-1]) / prices[i-1]
        returns.append(r)

    return returns


# -----------------------------------
# Volatility
# -----------------------------------

def calculate_volatility(returns):

    if len(returns) > 1:
        return statistics.stdev(returns)
    return 0


# -----------------------------------
# Expected Return
# -----------------------------------

def calculate_expected_return(returns):

    if returns:
        return statistics.mean(returns)
    return 0


# -----------------------------------
# Sharpe Ratio
# -----------------------------------

def sharpe_ratio(expected_return, volatility):

    if volatility == 0:
        return 0
    return (expected_return - RISK_FREE_RATE) / volatility


# -----------------------------------
# Linear Regression Prediction
# -----------------------------------

def predict_next_price(prices):
    
    prices = np.array(prices)
    X = np.arange(len(prices)).reshape(-1,1)
    y = prices
    model = LinearRegression()
    model.fit(X,y)
    next_day = np.array([[len(prices)]])
    prediction = model.predict(next_day)
    return prediction[0], model

def plot_prediction(prices, model):
    
    X = np.arange(len(prices)).reshape(-1,1)
    # Future days for prediction
    future_days = np.arange(len(prices) + 5).reshape(-1,1)
    predicted_line = model.predict(future_days)
    fig, ax = plt.subplots()
    ax.plot(prices, label="Historical Prices")
    ax.plot(future_days, predicted_line, linestyle="--", label="Prediction Trend")
    ax.set_title("Price Prediction (Linear Regression)")
    ax.set_xlabel("Days")
    ax.set_ylabel("Price (USD)")
    ax.legend()
    return fig


# -----------------------------------
# Streamlit Button
# -----------------------------------

if st.button("Run Crypto Analysis"):

    volatility_data = {}
    sharpe_data = {}
    predictions = {}

    for coin in COINS:

        prices = fetch_historical_prices(coin)
        returns = calculate_returns(prices)
        exp_return = calculate_expected_return(returns)
        vol = calculate_volatility(returns)
        sharpe = sharpe_ratio(exp_return, vol)
        pred, model = predict_next_price(prices)
        volatility_data[coin] = vol
        sharpe_data[coin] = sharpe
        predictions[coin] = pred

        st.subheader(coin.upper())

        st.write("Expected Return:", round(exp_return,6))
        st.write("Volatility:", round(vol,6))
        st.write("Sharpe Ratio:", round(sharpe,4))
        st.write("Predicted Next Price:", round(pred,2))

        # Price trend chart
        fig, ax = plt.subplots()
        ax.plot(prices)
        ax.set_title(f"{coin} Price Trend")
        st.pyplot(fig)
        st.write("Predicted Next Price:", round(pred,2))
        prediction_fig = plot_prediction(prices, model)
        st.pyplot(prediction_fig)


    # -------------------------------
    # Portfolio Allocation
    # -------------------------------

    sorted_coins = sorted(volatility_data.items(), key=lambda x: x[1])
    low = [c[0] for c in sorted_coins[:2]]
    medium = [c[0] for c in sorted_coins[2:4]]
    high = [c[0] for c in sorted_coins[4:]]

    allocation = {}

    for coin in low:
        allocation[coin] = TOTAL_INVESTMENT * 0.5 / len(low)

    for coin in medium:
        allocation[coin] = TOTAL_INVESTMENT * 0.3 / len(medium)

    for coin in high:
        allocation[coin] = TOTAL_INVESTMENT * 0.2 / len(high)

    st.header("Portfolio Allocation (₹10,000)")

    for coin, amount in allocation.items():
        st.write(f"{coin} → ₹{round(amount,2)}")


    # Pie Chart
    fig2, ax2 = plt.subplots()
    ax2.pie(allocation.values(), labels=allocation.keys(), autopct="%1.1f%%")
    st.pyplot(fig2)