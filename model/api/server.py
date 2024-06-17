from flask import Flask, request, jsonify
from model_functions import *
from flask_cors import CORS, cross_origin

#pythonBackend/
#python -m flask --debug --app api/server.py run

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api/predict", methods=['POST'])
def how_many_accs():
    data = request.get_json()

    if not data['ticker'] or data['ticker'] not in ['AAPL', 'GOOG', 'MSFT', 'NVDA', 'AMZN', 'META', 'TSM', 'TSLA', 'WMT', 'V']:
        return jsonify({'error': 'Please provide a valid stock ticker'}), 400

    try:
        response = predict_future_returns(data['ticker'])
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route("/api/test", methods=['POST'])
def test_request():
    data = request.get_json()
    print(data)
    return jsonify(data), 201