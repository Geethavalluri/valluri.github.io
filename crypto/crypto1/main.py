import requests
import numpy as np
import matplotlib.pyplot as plt
import smtplib
from email.mime.text import MIMEText


# ============================================
# CONFIGURATION
# ============================================

COINS = ["bitcoin", "ethereum", "cardano","solana","ripple"]
DAYS = 30
VOLATILITY_THRESHOLD = 0.05

# Email Config (Fill these if using email alert)
SENDER_EMAIL = "geethavalluri09@gmail.com"
SENDER_PASSWORD = "riro ktme xhto oaxb"
RECEIVER_EMAIL = "geethavalluri09@gmail.com"


# ============================================
# DATA FETCHING
# ============================================

def fetch_crypto_prices(coin_id, days=30):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": "usd", "days": days}

    response = requests.get(url, params=params)
    data = response.json()

    prices = [price[1] for price in data["prices"]]
    return np.array(prices)


# ============================================
# RISK CALCULATIONS
# ============================================

def calculate_returns(prices):
    return np.diff(prices) / prices[:-1]


def calculate_volatility(returns):
    return np.std(returns)


def calculate_expected_return(returns):
    return np.mean(returns)


def calculate_sharpe_ratio(expected_return, volatility, risk_free_rate=0.01):
    if volatility == 0:
        return 0
    return (expected_return - risk_free_rate) / volatility


# ============================================
# VISUALIZATIONS
# ============================================

def plot_price_trend(coin, prices):
    plt.figure()
    plt.plot(prices)
    plt.title(f"{coin.capitalize()} - {DAYS} Day Price Trend")
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


# ============================================
# REPORT GENERATION
# ============================================

def generate_report(results, filename="crypto_report.txt"):
    with open(filename, "w") as file:
        file.write("CRYPTO RISK ANALYSIS REPORT\n")
        file.write("=" * 40 + "\n\n")

        for coin, data in results.items():
            file.write(f"Coin: {coin.capitalize()}\n")
            file.write(f"Volatility: {data['volatility']:.5f}\n")
            file.write(f"Expected Return: {data['expected_return']:.5f}\n")
            file.write(f"Sharpe Ratio: {data['sharpe_ratio']:.5f}\n")
            file.write("-" * 40 + "\n")

    print(" Report generated successfully!")


# ============================================
# EMAIL ALERT
# ============================================

def send_email_alert(subject, message):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)

    print(" Email alert sent!")


# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":

    print("\n CRYPTO RISK MONITORING SYSTEM\n")

    results = {}
    volatility_data = {}

    for coin in COINS:
        print(f"Analyzing {coin.capitalize()}...")

        prices = fetch_crypto_prices(coin, DAYS)
        returns = calculate_returns(prices)

        volatility = calculate_volatility(returns)
        expected_return = calculate_expected_return(returns)
        sharpe_ratio = calculate_sharpe_ratio(expected_return, volatility)

        results[coin] = {
            "volatility": volatility,
            "expected_return": expected_return,
            "sharpe_ratio": sharpe_ratio
        }

        volatility_data[coin] = volatility

        print(f"Volatility: {volatility:.5f}")
        print(f"Expected Return: {expected_return:.5f}")
        print(f"Sharpe Ratio: {sharpe_ratio:.5f}")
        print("-" * 40)

        # Show price trend
        plot_price_trend(coin, prices)

        # Email Alert
        if volatility > VOLATILITY_THRESHOLD:
            subject = f" High Risk Alert: {coin.capitalize()}"
            message = f"{coin.capitalize()} volatility is high: {volatility:.5f}"
            # Uncomment below to enable email
            # send_email_alert(subject, message)

    # Show volatility comparison
    plot_volatility(volatility_data)

    # Generate report file
    generate_report(results)

    print("\nSystem Execution Completed Successfully!")