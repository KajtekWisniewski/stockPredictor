import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping
import joblib
import os
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for matplotlib
import matplotlib.pyplot as plt

# Define the list of companies and the time frame
tech_list = ['AAPL', 'GOOG', 'MSFT', 'NVDA', 'AMZN', 'META', 'TSM', 'TSLA', 'WMT', 'V']
start_date = '2010-01-01'
end_date = '2023-01-01'

# Directory to save models and scalers
save_dir = 'saved_models'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Function to train and save model for a stock
def train_and_save_model(stock):
    # Fetch the historical stock data
    data = yf.download(stock, start=start_date, end=end_date)['Adj Close']

    # Calculate daily returns
    returns = data.pct_change().dropna()

    # Standardize the returns
    scaler = StandardScaler()
    scaled_returns = scaler.fit_transform(returns.values.reshape(-1, 1))

    # Save the scaler for later use
    scaler_filename = f'{save_dir}/{stock}_scaler.pkl'
    joblib.dump(scaler, scaler_filename)

    # Prepare the data for LSTM
    def create_sequences(data, seq_length):
        xs, ys = [], []
        for i in range(len(data) - seq_length):
            x = data[i:i + seq_length]
            y = data[i + seq_length]
            xs.append(x)
            ys.append(y)
        return np.array(xs), np.array(ys)

    # Set sequence length
    seq_length = 30

    # Create sequences
    X, y = create_sequences(scaled_returns, seq_length)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Build the LSTM model with Dropout regularization
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(seq_length, 1)))
    model.add(Dropout(0.2))  # Dropout layer
    model.add(LSTM(50))
    model.add(Dropout(0.2))  # Dropout layer
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mse')

    # Early stopping callback
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

    # Train the model with early stopping
    history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, callbacks=[early_stopping])

    # Save the trained model
    model_filename = f'{save_dir}/{stock}_lstm_model.keras'
    model.save(model_filename)

    # Plot the training and validation loss
    plt.figure(figsize=(14, 7))
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title(f'Training and Validation Loss for {stock}')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig(f'{save_dir}/{stock}_training_validation_loss.png')
    plt.close()

# Train and save models for each stock
for stock in tech_list:
    train_and_save_model(stock)
