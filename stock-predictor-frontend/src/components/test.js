'use client';

import React, { useState } from 'react';
import axios from 'axios';

const PutRequestComponent = () => {
  const [responseMessage, setResponseMessage] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const sendPutRequest = async () => {
    setLoading(true);
    setError('');
    try {
      const response = await axios.put(`http://localhost:4001/stocks`);
      setResponseMessage(response.data.message); // Adjust based on your API response structure
    } catch (err) {
      setError('Error sending PUT request');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <button onClick={sendPutRequest} disabled={loading}>
        {loading ? 'Loading...' : 'Send PUT Request'}
      </button>
      {responseMessage && <div>Response: {responseMessage}</div>}
      {error && <div style={{ color: 'red' }}>{error}</div>}
    </div>
  );
};

export default PutRequestComponent;
