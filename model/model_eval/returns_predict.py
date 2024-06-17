import yfinance as yf
import numpy as np
from keras.models import load_model
import joblib
import matplotlib.pyplot as plt
import os

# Define the stock and the time frame
stock = 'V'  # Change this to the stock you want to predict
start_date = '2024-01-01'
end_date = '2024-06-01'

# Directory where models and scalers are saved
save_dir = 'saved_models'

# Fetch the historical stock data
data = yf.download(stock, start=start_date, end=end_date)['Adj Close']

# Calculate daily returns
returns = data.pct_change().dropna()

# Load the scaler
scaler_filename = f'{save_dir}/{stock}_scaler.pkl'
scaler = joblib.load(scaler_filename)

# Standardize the returns
scaled_returns = scaler.transform(returns.values.reshape(-1, 1))

# Load the trained model
model_filename = f'{save_dir}/{stock}_lstm_model.keras'
model = load_model(model_filename)

# Set sequence length
seq_length = 30

# Prepare the latest data for prediction
def create_sequences(data, seq_length):
    xs = []
    for i in range(len(data) - seq_length):
        x = data[i:i + seq_length]
        xs.append(x)
    return np.array(xs)

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
future_returns = predict_future_returns(model, scaled_returns, scaler, days=30)

# Calculate cumulative return over the next 30 days
cumulative_return = np.sum(future_returns)

# Convert cumulative return to percentage
cumulative_return_percentage = cumulative_return * 100

# Print the cumulative return percentage
print(f'Predicted cumulative return for {stock} over the next 30 days: {cumulative_return_percentage:.2f}%')


# Plot the predicted returns
plt.figure(figsize=(14, 7))
plt.plot(future_returns*100, label=stock)
plt.title(f'Predicted Returns for {stock} for the Next 30 Days')
plt.xlabel('Days')
plt.ylabel('Return in %')
plt.legend()
plt.show()
