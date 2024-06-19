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
matplotlib.use('Agg') 
import matplotlib.pyplot as plt


tech_list = ['AAPL', 'GOOG', 'MSFT', 'NVDA', 'AMZN', 'META', 'TSM', 'TSLA', 'WMT', 'V']
start_date = '2010-01-01'
end_date = '2023-01-01'

save_dir = 'saved_models'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)


def train_and_save_model(stock):

    data = yf.download(stock, start=start_date, end=end_date)['Adj Close']

  
    log_returns = np.log(data / data.shift(1)).dropna()

    scaler = StandardScaler()
    scaled_log_returns = scaler.fit_transform(log_returns.values.reshape(-1, 1))


    scaler_filename = f'{save_dir}/{stock}_scaler.pkl'
    joblib.dump(scaler, scaler_filename)


    def create_sequences(data, seq_length):
        xs, ys = [], []
        for i in range(len(data) - seq_length):
            x = data[i:i + seq_length]
            y = data[i + seq_length]
            xs.append(x)
            ys.append(y)
        return np.array(xs), np.array(ys)


    seq_length = 100

    X, y = create_sequences(scaled_log_returns, seq_length)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = Sequential()
    model.add(LSTM(100, return_sequences=True, input_shape=(seq_length, 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(100))
    model.add(Dropout(0.2))
    model.add(Dense(1))
    
    model.compile(optimizer='adam', loss='mse')


    early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

    history = model.fit(X_train, y_train, epochs=100, batch_size=64, validation_split=0.2, callbacks=[early_stopping])


    model_filename = f'{save_dir}/{stock}_lstm_model.keras'
    model.save(model_filename)
    print(f'model saved: ${stock}')

    plt.figure(figsize=(14, 7))
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title(f'Training and Validation Loss for {stock}')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig(f'{save_dir}/{stock}_training_validation_loss.png')
    plt.close()


for stock in tech_list:
    train_and_save_model(stock)
