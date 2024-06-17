This is a folder containing previous versions of models which were made with wrong approach for the following reasons:
a - using actual prices as inputs, and using min-max scaler on them - this doesn't make sense as stock prices are not bound. Meaning even if historic data
contains prices from range for example 100$-200$ it doesn't mean they cant go lower or higher, this would make predicting prices and using min-max scaler very unreliable
as the model would have no idea what to do with values that were never present in the dataset.
b - trying to predict actual prices as output - this is practially impossible to predict perfectly and besides uses prices from test-set which is usually the most fresh prices,
and this isn't very effective
c - not actually using sequential data in an LSTM model

using:
https://www.kaggle.com/code/faressayah/stock-market-analysis-prediction-using-lstm/comments

and chatgpt; google gemini
