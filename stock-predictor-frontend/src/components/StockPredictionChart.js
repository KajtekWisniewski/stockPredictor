import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import 'chart.js/auto';
import axios from 'axios';
import { ClipLoader } from 'react-spinners';

const StockPredictionChart = ({ stock, startDate, endDate, days }) => {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    setError(null);
    setData(null);

    axios
      .post(`${process.env.NEXT_PUBLIC_DEMO_BACKEND_URL_2}/api/predict`, {
        ticker: stock,
        start_date: startDate,
        end_date: endDate,
        days: days
      })
      .then((response) => {
        const data = response.data;
        if (data.error) {
          throw new Error(data.error);
        }
        setData(data);
        setLoading(false);
      })
      .catch((error) => {
        setError(error);
        setLoading(false);
      });
  }, [stock, startDate, endDate, days]);

  if (loading) {
    return (
      <div>
        <ClipLoader
          color="#256168"
          size={150}
          aria-label="Loading Spinner"
          data-testid="loader"
        />
      </div>
    );
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  if (!data) {
    return <div>No data available</div>;
  }

  const { future_returns, cumulative_return_percentage } = data;

  if (!future_returns || cumulative_return_percentage === undefined) {
    return <div>Invalid data received from API</div>;
  }

  // Generate dates for the X-axis
  const today = new Date();
  const labels = Array.from({ length: days }, (_, i) => {
    const date = new Date(today);
    date.setDate(today.getDate() + i);
    return date.toISOString().split('T')[0];
  });

  const chartData = {
    labels,
    datasets: [
      {
        label: `Predicted Returns for ${stock}`,
        data: future_returns,
        fill: false,
        backgroundColor: 'rgba(75,192,192,0.2)',
        borderColor: 'rgba(75,192,192,1)',
        tension: 0.1
      }
    ]
  };

  return (
    <div>
      <h1>Predicted Cumulative Return: {cumulative_return_percentage.toFixed(2)}%</h1>
      <Line data={chartData} />
    </div>
  );
};

export default StockPredictionChart;
