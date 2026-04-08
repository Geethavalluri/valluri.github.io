import streamlit as st
import requests
import numpy as np
import statistics
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.title(" Crypto Investment Manager Dashboard")

COINS = ["bitcoin","ethereum","cardano","solana","ripple"]
TOTAL_INVESTMENT = 10000

# ---------------------------------------------------
# Fetch Historical Prices
# ---------------------------------------------------

def fetch_prices(coin):

    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"

    params = {
        "vs_currency":"usd",
        "days":30
    }

    response = requests.get(url, params=params)
    data = response.json()

    prices = [p[1] for p in data["prices"]]

    return prices


# ---------------------------------------------------
# Calculate Returns
# ---------------------------------------------------

def calculate_returns(prices):

    returns = []

    for i in range(1,len(prices)):
        r = (prices[i] - prices[i-1]) / prices[i-1]
        returns.append(r)

    return returns


# ---------------------------------------------------
# Prediction Model
# ---------------------------------------------------

def predict_price(prices):

    X = np.arange(len(prices)).reshape(-1,1)
    y = np.array(prices)

    model = LinearRegression()
    model.fit(X,y)

    next_day = np.array([[len(prices)]])
    prediction = model.predict(next_day)

    return prediction[0]


# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

selected_coin = st.sidebar.selectbox("Select Cryptocurrency", COINS)
investment = st.sidebar.number_input("Investment Amount", value=10000)

# ---------------------------------------------------
# Fetch Data
# ---------------------------------------------------

prices = fetch_prices(selected_coin)
returns = calculate_returns(prices)

volatility = statistics.stdev(returns)
avg_return = statistics.mean(returns)

predicted_price = predict_price(prices)

# ---------------------------------------------------
# Dashboard Layout
# ---------------------------------------------------

col1, col2 = st.columns(2)

# Price Trend
with col1:

    st.subheader("Price Trend (30 Days)")

    fig, ax = plt.subplots()
    ax.plot(prices)
    ax.set_title(selected_coin.capitalize())

    st.pyplot(fig)


# Prediction Chart
with col2:

    st.subheader("Price Prediction")

    fig2, ax2 = plt.subplots()

    x = list(range(len(prices)))
    ax2.plot(x, prices)

    ax2.scatter(len(prices), predicted_price)

    ax2.set_title("Next Day Prediction")

    st.pyplot(fig2)


# ---------------------------------------------------
# Metrics
# ---------------------------------------------------

st.subheader("Market Metrics")

col3, col4, col5 = st.columns(3)

col3.metric("Average Return", round(avg_return,5))
col4.metric("Volatility (Risk)", round(volatility,5))
col5.metric("Predicted Price", round(predicted_price,2))


# ---------------------------------------------------
# Portfolio Allocation
# ---------------------------------------------------

st.subheader("Portfolio Allocation")

low = investment * 0.5
medium = investment * 0.3
high = investment * 0.2

labels = ["Low Risk","Medium Risk","High Risk"]
values = [low,medium,high]

fig3, ax3 = plt.subplots()
ax3.pie(values,labels=labels,autopct="%1.1f%%")

st.pyplot(fig3)