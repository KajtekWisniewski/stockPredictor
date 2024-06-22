# Stock Predictor

Academic project for stock return predictions using LSTM models of the following companies:
APPLE, GOOGLE, MICROSOFT, NVIDIA, AMAZON, META, TSMC, TESLA, WALMART, VISA.

Uses keycloak for authentication and authorization.

# HOW TO USE

clone the repository to your local machine. Ensure you have docker as this app is optimised for **docker usage only**.

### Light version (RECOMMENDED)

This version uses random dummy data instead of ML model to make "predictions". Its very lightweight and for
entire app functionally the same. Details on the heavy version are below the functionalities section.

- navigate to stockPredictor directory
- docker-compose up --build
- go to http://localhost:3000 in your browser
- register to have user functionalities
if you want to have admin functionalities, you need to navigate to http://localhost:8080, login to keycloak with login: **admin**, password: **admin**
change realm to myrealm, assign roles to your user account or create new admin user -> from general roles assign admin role, and from roles of clients(frontend-client, api-client) assign admin from both.

## Functionalities

- main page -> send a request to test if the ASP.NET core api works properly
- predict -> Send a request to make a prediciton. Draws a graph with predicted values and total return. **USER LOGGED IN** -> Option to save results to the database
- stocks -> check the supported stock charts
- login -> login via keycloak
- community page -> **only available if the user is logged in**, check if you are an admin, see the list of all predicitons from the database. **USER IS AN ADMIN** -> Delete any position from the database

### Very Heavy version (HIGHLY NOT RECOMMENDED)

if you want to use actual LSTM models to make predictions, use this version, however they are not very good and
randomly generated data from imitation actually looks better on the graphs. Both versions are functionally the same for the entire app.

in docker-compose file change:
```
flask-imitation:
    build:
      context: ./imitation
```
from ./imitation to ./model

be wary that tensorflow, and all the required packages are very big in size, so the container totals to around 7.6gb.

## About the model(s)

It should be noted that the results of the models are very unreliable for the following reasons:

- stock prices or returns can be pretty much summarized as being random. Hence it's impossible to predict what will happen on the stock market. Even if you tried using mathematics or models for this, if you was to do it alone, you are propably gonna be better off just using your common sense for predictions. Or you could also throw a dice.
- models are trained on respective stock log-return history, which with time almost always trends bullish, which means that the data is very biased towards positive outcomes and so are the models
- Nothing is able to predict what will happen on the stock market, however it could play a minor role in risk management if it worked better (ie. eliminating bias towards positive outcomes)

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

Readme about previous models is located here:
<https://github.com/KajtekWisniewski/stockPredictor/blob/main/model/model_eval/legacy/readme.md>

## Using the app (prediction tab)

- Select the ticker
- Select the time range to be considered for prediction
- Select amount of days into to the future for the prediction to be made, range 7-60

### This returns a graph of every day predicted returns and cumulative return over a selected period
