## This is a folder containing previous versions of models.

### They were created with a wrong approach for the following reasons:

- using actual prices as inputs, and using min-max scaler on them - this doesn't make sense as stock prices are not bound. Meaning even if historic data
  contains prices from range for example 100$-200$ it doesn't mean they cant go lower or higher, this would make predicting prices and using min-max scaler very unreliable
  as the model would have no idea what to do with values that were never present in the dataset.
- trying to predict actual prices as output - this is practially impossible to predict perfectly and besides uses prices from test-set which is usually the most fresh prices,
  and this isn't very effective
- not actually using sequential data in an LSTM model

### What I've used to created them:

1. https://www.kaggle.com/code/faressayah/stock-market-analysis-prediction-using-lstm/comments
2. https://github.com/jaungiers/LSTM-Neural-Network-for-Time-Series-Prediction/tree/master
3. https://medium.com/accredian/leveraging-lstm-and-llm-models-for-stock-price-prediction-79bf15d681ec
4. https://towardsdatascience.com/predicting-stock-prices-using-a-keras-lstm-model-4225457f0233
5. ChatGPT & Google Gemini
