from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from functions import *

#pythonBackend/
#python -m flask --debug --app api/server.py run

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:30001"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api/predict", methods=['POST'])
def prediction():
    data = request.get_json()

    if not data['ticker'] or data['ticker'] not in ['AAPL', 'GOOG', 'MSFT', 'NVDA', 'AMZN', 'META', 'TSM', 'TSLA', 'WMT', 'V']:
        return jsonify({'error': 'Please provide a valid stock ticker'}), 400

    ticker = data['ticker']
    start_date = data.get('start_date', '2024-01-01')
    end_date = data.get('end_date', '2024-06-17')
    days = data.get('days', 30)

    try:
        if 'start_date' in data and 'end_date' in data and 'days' in data:
            response = predict_future_returns_imitation(ticker, start_date, end_date, days)
        elif 'start_date' in data and 'end_date' in data:
            response = predict_future_returns_imitation(ticker, start_date, end_date)
        elif 'days' in data:
            response = predict_future_returns_imitation(ticker, days=days)
        else:
            response = predict_future_returns_imitation(ticker)
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route("/api/test", methods=['POST'])
def test_request():
    data = request.get_json()
    print(data)
    return jsonify(data), 201