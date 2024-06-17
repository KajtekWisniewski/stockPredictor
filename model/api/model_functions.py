from flask import Flask, request, jsonify
import joblib
import numpy as np
from keras.models import load_model
import yfinance as yf
import os
# Path to the directory containing saved models and scalers
models_dir = 'model_eval/saved_models'

# Function to predict future returns
def predict_future_returns(ticker, start_date='2024-01-01', end_date='2024-06-17', days=30):
    # Load the scaler
    scaler_filename = (f'{models_dir}/{ticker}_scaler.pkl')
    scaler = joblib.load(scaler_filename)

    # Load the trained model
    model_filename = os.path.join(models_dir, f'{ticker}_lstm_model.keras')
    model = load_model(model_filename)

    # Fetch the historical stock data
    data = yf.download(ticker, start=start_date, end=end_date)['Adj Close']

    # Calculate daily returns
    returns = data.pct_change().dropna()

    # Standardize the returns
    scaled_returns = scaler.transform(returns.values.reshape(-1, 1))

    # Prepare the latest data for prediction
    def create_sequences(data, seq_length):
        xs = []
        for i in range(len(data) - seq_length):
            x = data[i:i + seq_length]
            xs.append(x)
        return np.array(xs)

    # Set sequence length
    seq_length = 30

    # Create sequences from the latest data
    X_new = create_sequences(scaled_returns, seq_length)

    # Reshape input to match the model's expected input shape (batch_size, seq_length, num_features)
    X_new = np.expand_dims(X_new, axis=2)

    # Predict the future returns
    def predict_future_returns(model, data, scaler, days=30):
        predictions = []
        current_batch = data[-seq_length:]
        current_batch = current_batch.reshape(1, seq_length, 1)

        for _ in range(days):
            predicted_return = model.predict(current_batch)[0]
            predictions.append(predicted_return)
            current_batch = np.append(current_batch[:, 1:, :], [[predicted_return]], axis=1)

        predictions = scaler.inverse_transform(predictions)
        return predictions

    # Predict returns for the next 30 days
    future_returns = predict_future_returns(model, scaled_returns, scaler, days=days)

    # Calculate cumulative return over the next 30 days
    cumulative_return = np.sum(future_returns)
    cumulative_return_percentage = cumulative_return * 100

    # Prepare the data for the response
    future_returns_list = future_returns.flatten().tolist()
    scaled_list = []
    for item in future_returns_list:
        scaled_list.append(item*100)
    response = {
        'future_returns': scaled_list,
        'cumulative_return_percentage': cumulative_return_percentage
    }

    return response