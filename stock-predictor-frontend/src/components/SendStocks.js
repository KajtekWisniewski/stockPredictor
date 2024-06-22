'use client';

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SendStocks = ({ predictionParams }) => {
  const [loading, setLoading] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState('');

  const sendPostRequest = async () => {
    setLoading(true);
    setError('');

    try {
      const sessionResponse = await axios.get('/api/fetch-access-token');

      if (sessionResponse.status === 200 && sessionResponse.data.accessToken) {
        const accessToken = sessionResponse.data.accessToken;
        //console.log(accessToken)

        // Prepare data according to the StockDto structure
        const stocksData = {
          Ticker: predictionParams.stock,
          DateOfPrediction: predictionParams.startDate,
          PredictedReturn: predictionParams.cumulative_return_percentage_number,
          DaysPredicted: predictionParams.days
        };

        // Send the formatted data in a POST request
        await axios.post(
          `${process.env.NEXT_PUBLIC_DEMO_BACKEND_URL}/stocks`,
          stocksData,
          {
            headers: {
              'Content-Type': 'application/json',
              Authorization: 'Bearer ' + accessToken
            }
          }
        );

        setSubmitted(true);
      } else {
        setError('You do not have permission to perform this action.');
      }
    } catch (err) {
      setError('Error saving stocks data');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  if (!predictionParams || submitted) {
    return null;
  }

  return (
    <div>
      <button onClick={sendPostRequest} disabled={loading}>
        {loading ? 'Sending...' : 'Save Stock Data'}
      </button>
      {error && <div style={{ color: 'red' }}>{error}</div>}
    </div>
  );
};

export default SendStocks;
