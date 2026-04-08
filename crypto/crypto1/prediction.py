import numpy as np
from sklearn.linear_model import LinearRegression


# ------------------------------------------------------------
# LINEAR REGRESSION PRICE PREDICTION
# ------------------------------------------------------------

def predict_next_price(prices):
    """
    Predict next day's price using Linear Regression
    """

    prices = np.array(prices)

    # Create day index
    X = np.arange(len(prices)).reshape(-1, 1)

    # Target variable
    y = prices

    # Create and train model
    model = LinearRegression()
    model.fit(X, y)

    # Predict next day
    next_day = np.array([[len(prices)]])
    prediction = model.predict(next_day)

    return prediction[0]