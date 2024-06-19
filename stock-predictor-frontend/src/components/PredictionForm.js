'use client';
import React, { useState } from 'react';
import styles from './componentStyles.module.scss';

const PredictionForm = ({ onSubmit }) => {
  const currentDate = new Date().toJSON().slice(0, 10);
  const [ticker, setTicker] = useState('AAPL');
  const [startDate, setStartDate] = useState('2024-01-01');
  const [endDate, setEndDate] = useState(currentDate);
  const [days, setDays] = useState(30);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ ticker, startDate, endDate, days: Number(days) });
  };

  return (
    <form className={styles.formStyle} onSubmit={handleSubmit}>
      <div className={styles.selectStyle}>
        <label>
          Ticker:
          <select value={ticker} onChange={(e) => setTicker(e.target.value)}>
            <option value="AAPL">AAPL</option>
            <option value="GOOG">GOOG</option>
            <option value="MSFT">MSFT</option>
            <option value="NVDA">NVDA</option>
            <option value="AMZN">AMZN</option>
            <option value="META">META</option>
            <option value="TSM">TSM</option>
            <option value="TSLA">TSLA</option>
            <option value="WMT">WMT</option>
            <option value="V">V</option>
          </select>
        </label>
      </div>
      <div className={styles.dateStyle}>
        <label>
          Start Date:
          <input
            type="date"
            value={startDate}
            onChange={(e) => setStartDate(e.target.value)}
          />
        </label>
      </div>
      <div className={styles.dateStyle}>
        <label>
          End Date:
          <input
            type="date"
            value={endDate}
            onChange={(e) => setEndDate(e.target.value)}
          />
        </label>
      </div>
      <div className={styles.rangeStyle}>
        <label>
          Days:
          <input
            type="range"
            min="7"
            max="60"
            value={days}
            onChange={(e) => setDays(e.target.value)}
          />
          {days}
        </label>
      </div>
      <button type="submit">Predict</button>
    </form>
  );
};

export default PredictionForm;
