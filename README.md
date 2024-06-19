# Stock Predictor

Academic project for stock return predictions using LSTM models of the following companies:
APPLE, GOOGLE, MICROSOFT, NVIDIA, AMAZON, META, TSMC, TESLA, WALMART, VISA

## About the model(s)

It should be noted that the results of the models are very unreliable for the following reasons:

- stock prices or returns can be pretty much summarized as being random. Hence it's impossible to predict what will happen on the stock market. Even if you tried using mathematics or models for this, if you was to do it alone, you are propably gonna be better off just using your common sense for predictions. Or you could also throw a dice.
- models are trained on respective stock log-return history, which with time almost always trends bullish, which means that the data is very biased towards positive outcomes and so are the models
- if this model was working properly I would be a multimillionaire, nothing is able to predict what will happen on the stock market, however it could play a minor role in risk management if it worked better (ie. eliminating bias towards positive outcomes)

### What data do the model(s) use?

Each model uses the following data for training

- Stock prices from 2010-01-01 till 2024-06-17, in form of log-returns
- Training set and validation set are 80/20, shuffled
- Sequence lentgh of either 30/50/100
- LSTM with 2 layers, each with 100 units, 20% dropout rate
- Adam optimizer, with early stopping
- Activation function: tanh (default)
- Batch size: 64, 100 max epochs
- However I can't seem to get validation/train curves from almost going flat, to anything else, no matter what model parameters I use.

### Previous models

Readme about previous models is located in model/model_eval/legacy

## Using the app (prediction tab)

- Select the ticker
- Select the time range to be considered for prediction
- Select amount of days into to the future for the prediction to be made, range 7-60

### This returns a graph of every day predicted returns and cumulative return over a selected period
