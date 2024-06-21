'use client';

import React, { useState } from 'react';
import axios from 'axios';

const FetchStocksComponent = () => {
  const [stocks, setStocks] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const sendGetRequest = async () => {
    setLoading(true);
    setError('');

    try {
      // Fetch the access token and validate the session
      const sessionResponse = await axios.get('/api/fetch-access-token');

      if (sessionResponse.status === 200 && sessionResponse.data.accessToken) {
        const accessToken = sessionResponse.data.accessToken;

        // Fetch the stock data using the access token
        const response = await axios.get('http://localhost:4001/stocks', {
          headers: {
            'Content-Type': 'application/json',
            Authorization: 'Bearer ' + accessToken
          }
        });

        setStocks(response.data); // Adjust based on your API response structure
      } else {
        setError('You do not have permission to view this content.');
      }
    } catch (err) {
      setError('Error fetching stocks data');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <button onClick={sendGetRequest} disabled={loading}>
        {loading ? 'Loading...' : 'Fetch Stocks'}
      </button>
      {stocks.length > 0 && (
        <>
          <h1>Stocks</h1>
          <table>
            <thead>
              <tr>
                <th>Id</th>
                <th>Ticker</th>
                <th>Date of Prediction</th>
                <th>Predicted Return</th>
                <th>Days Predicted</th>
              </tr>
            </thead>
            <tbody>
              {stocks.map((stock) => (
                <tr key={stock.id}>
                  <td>{stock.id}</td>
                  <td>{stock.ticker}</td>
                  <td>{stock.dateOfPrediction}</td>
                  <td>{stock.predictedReturn}</td>
                  <td>{stock.daysPredicted}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </>
      )}
      {error && <div style={{ color: 'red' }}>{error}</div>}
    </div>
  );
};

export default FetchStocksComponent;
