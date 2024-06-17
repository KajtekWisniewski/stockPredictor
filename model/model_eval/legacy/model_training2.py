import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import yfinance as yf
from datetime import datetime
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import matplotlib.pyplot as plt

# Fetch the stock data
tech_list = ['AAPL', 'GOOG', 'MSFT', 'NVDA', 'AMZN', 'META', 'TSM', 'TSLA', 'WMT', 'V']
ticker = tech_list[0]
df = yf.download(ticker, start='2019-01-01', end=datetime.now())

# Prepare the data
data = df.filter(['Close'])
dataset = data.values
training_data_len = int(np.ceil(len(dataset) * 0.95))

# Scale the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)

# Create the training and validation data sets
train_data = scaled_data[0:int(training_data_len), :]
val_data = scaled_data[int(training_data_len) - 60:, :]

# Prepare the training data
x_train = []
y_train = []

for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# Prepare the validation data
x_val = []
y_val = []

for i in range(60, len(val_data)):
    x_val.append(val_data[i-60:i, 0])
    y_val.append(val_data[i, 0])

x_val, y_val = np.array(x_val), np.array(y_val)
x_val = np.reshape(x_val, (x_val.shape[0], x_val.shape[1], 1))

# Build the model
model = Sequential()
model.add(LSTM(128, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
history = model.fit(x_train, y_train, validation_data=(x_val, y_val), batch_size=32, epochs=2)

# Save the model
model.save(f'{ticker}_stock_lstm_modelv2.keras')

# Predict future values
# We will predict the next 60 days based on the last 60 days from the entire dataset
last_60_days = scaled_data[-60:]
x_future = [last_60_days]
x_future = np.array(x_future)
x_future = np.reshape(x_future, (x_future.shape[0], x_future.shape[1], 1))

future_predictions = []

for _ in range(15):
    pred = model.predict(x_future)
    future_predictions.append(pred[0][0])
    pred_reshaped = np.reshape(pred, (1, 1, 1))  # Reshape pred to match the dimensions
    x_future = np.append(x_future[:, 1:, :], pred_reshaped, axis=1)

future_predictions = scaler.inverse_transform(np.array(future_predictions).reshape(-1, 1))

# Get the RMSE for the validation set
predictions = model.predict(x_val)
predictions = scaler.inverse_transform(predictions)
rmse = np.sqrt(np.mean(((predictions - y_val) ** 2)))
print(f'Validation RMSE: {rmse}')

# Plot the training history
plt.figure(figsize=(12, 6))
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper right')
plt.show()

# Plot the data
train = data[:training_data_len]
valid = data[training_data_len:]
valid['Predictions'] = predictions

plt.figure(figsize=(16, 6))
plt.title('Model')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
plt.show()

# Plot future predictions
plt.figure(figsize=(16, 6))
plt.title('Future Predictions')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.plot(data.index, data['Close'])

# Generate future dates without using 'closed' parameter
future_dates = pd.date_range(start=data.index[-1], periods=61)

plt.plot(future_dates[1:], future_predictions, linestyle='--', marker='o')
plt.legend(['Historical', 'Future Predictions'], loc='lower right')
plt.show()