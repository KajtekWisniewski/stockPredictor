import yfinance as yf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Function to create dataset for the LSTM model
def create_dataset(data, time_step=1):
    X, Y = [], []
    for i in range(len(data) - time_step - 1):
        a = data[i:(i + time_step), 0]
        X.append(a)
        Y.append(data[i + time_step, 0])
    return np.array(X), np.array(Y)

# Function to predict future prices
def predict_future_days(model, data, days, time_step):
    future_predictions = []
    last_data = data[-time_step:]

    for _ in range(days):
        prediction = model.predict(last_data.reshape(1, time_step, 1))
        future_predictions.append(prediction[0, 0])
        last_data = np.append(last_data[1:], prediction[0, 0]).reshape(-1, 1)

    return scaler.inverse_transform(np.array(future_predictions).reshape(-1, 1))

# Load the trained model
model = tf.keras.models.load_model('apple_stock_lstm_modelv2.keras')

# Load the stock data
ticker = 'AAPL'
data = yf.download(ticker, start='2010-01-01', end='2024-01-01')

# Use the 'Close' column for prediction
close_prices = data['Close'].values.reshape(-1, 1)

# Scale the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(close_prices)

# Predict future prices for the next time frame
future_days = 30  # Change this value for different prediction time frames (e.g., 1 for 1 day, 7 for 1 week, etc.)
future_prices = predict_future_days(model, scaled_data, future_days, 30)

# Plot the actual and predicted prices
last_known_date = data.index[-1]
future_dates = [last_known_date + timedelta(days=i) for i in range(1, future_days + 1)]

# Plot the actual and predicted prices
plt.figure(figsize=(14, 5))
plt.plot(data.index, data['Close'], label='Actual Prices', color='blue')
plt.plot(future_dates, future_prices, label='Predicted Trend', color='red')
plt.xlabel('Date')
plt.ylabel('Close Price USD')
plt.legend()
plt.show()
