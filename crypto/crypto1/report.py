# ------------------------------------------------------------
# CRYPTO ANALYSIS REPORT
# ------------------------------------------------------------

from risk import (
    fetch_crypto_prices,
    calculate_returns,
    calculate_volatility,
    calculate_expected_return,
    classify_risk
)

import time

COINS = ["bitcoin", "ethereum", "cardano", "solana", "ripple"]


# ------------------------------------------------------------
# Generate Report
# ------------------------------------------------------------

def generate_report():

    report_file = open("crypto_report.txt", "w")

    print("\n========== CRYPTO PORTFOLIO REPORT ==========\n")
    report_file.write("========== CRYPTO PORTFOLIO REPORT ==========\n\n")

    for coin in COINS:

        print("Analyzing:", coin.capitalize())
        report_file.write(f"Analyzing: {coin.capitalize()}\n")

        prices = fetch_crypto_prices(coin)

        if not prices:
            print("No data available\n")
            report_file.write("No data available\n\n")
            continue

        returns = calculate_returns(prices)

        expected_return = calculate_expected_return(returns)

        volatility = calculate_volatility(returns)

        risk = classify_risk(volatility)

        print("Expected Return:", round(expected_return, 6))
        print("Volatility:", round(volatility, 6))
        print("Risk Level:", risk)
        print("-----------------------------------\n")

        report_file.write(f"Expected Return: {round(expected_return,6)}\n")
        report_file.write(f"Volatility: {round(volatility,6)}\n")
        report_file.write(f"Risk Level: {risk}\n")
        report_file.write("-----------------------------------\n\n")

        time.sleep(2)

    print("=========== REPORT COMPLETE ===========")
    report_file.write("=========== REPORT COMPLETE ===========")

    report_file.close()


# ------------------------------------------------------------

if __name__ == "__main__":
    generate_report()