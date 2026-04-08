import smtplib
from email.mime.text import MIMEText
from risk import (
    fetch_crypto_prices,
    calculate_returns,
    calculate_volatility
)

#  Enter your details here
SENDER_EMAIL = "geethavalluri09@gmail.com"
SENDER_PASSWORD = "riro ktme xhto oaxb"
RECEIVER_EMAIL = "geethavalluri09@gmail.com"

VOLATILITY_THRESHOLD = 0.005  # Change as needed


def send_email_alert(subject, message):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)

    print(" Alert email sent successfully!")


def check_risk_and_alert(coin):
    prices = fetch_crypto_prices(coin)
    returns = calculate_returns(prices)
    volatility = calculate_volatility(returns)

    print(f"{coin.capitalize()} Volatility: {volatility:.5f}")

    if volatility > VOLATILITY_THRESHOLD:
        subject = f" High Risk Alert: {coin.capitalize()}"
        message = f"{coin.capitalize()} volatility is high: {volatility:.5f}"
        send_email_alert(subject, message)
    else:
        print(" Risk level is normal.")


if __name__ == "__main__":
    check_risk_and_alert("cardano")