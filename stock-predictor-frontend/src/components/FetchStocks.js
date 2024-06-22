'use client';

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import AdminRoute from './keycloak/AdminRoute';

const FetchStocks = () => {
  const [stocks, setStocks] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [isAdmin, setIsAdmin] = useState(false);
  
  useEffect(() => {
    const checkAdminStatus = async () => {
      try {
        const sessionResponse = await axios.get('/api/fetch-admin-token');
        if (sessionResponse.status === 200 && sessionResponse.data.accessToken) {
          setIsAdmin(true);
        } else {
          setIsAdmin(false);
        }
      } catch (err) {
        console.error('Error checking admin status', err);
      }
    };

    checkAdminStatus();
  }, []);

  const sendGetRequest = async () => {
    setLoading(true);
    setError('');

    try {
      // Fetch the access token and validate the session
      const sessionResponse = await axios.get('/api/fetch-access-token');

      if (sessionResponse.status === 200 && sessionResponse.data.accessToken) {
        const accessToken = sessionResponse.data.accessToken;

        // Fetch the stock data using the access token
        const response = await axios.get(
          `${process.env.NEXT_PUBLIC_DEMO_BACKEND_URL}/stocks`,
          {
            headers: {
              'Content-Type': 'application/json',
              Authorization: 'Bearer ' + accessToken
            }
          }
        );

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

  const handleDelete = async (id) => {
    setLoading(true);
    setError('');

    try {
      const adminSessionResponse = await axios.get('/api/fetch-admin-token');

      if (adminSessionResponse.status === 200 && adminSessionResponse.data.accessToken) {
        const adminAccessToken = adminSessionResponse.data.accessToken;

        await axios.delete(
          `${process.env.NEXT_PUBLIC_DEMO_BACKEND_URL}/stocks/${id}`,
          {
            headers: {
              'Content-Type': 'application/json',
              Authorization: 'Bearer ' + adminAccessToken
            }
          }
        );

        setStocks(stocks.filter(stock => stock.id !== id));
      } else {
        setError('You do not have permission to delete this content.');
      }
    } catch (err) {
      setError('Error deleting stock data');
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
                {isAdmin && <th>Admin Action</th>}
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
                  {isAdmin && <td>
                    <button onClick={() => handleDelete(stock.id)} disabled={loading}>
                      Delete
                    </button>
                  </td> }
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

export default FetchStocks;
