'use client';

import React, { useState } from 'react';
import styles from '../stockStyles.module.scss';
import { Suspense } from 'react';
import { ClipLoader } from 'react-spinners';
import PredictionForm from '@/components/PredictionForm';
import StockPredictionChart from '@/components/StockPredictionChart';

export default function StocksPage() {
  const [predictionParams, setPredictionParams] = useState(null);

  const handleFormSubmit = (params) => {
    setPredictionParams(params);
  };

  return (
    <div className={styles.mainDiv}>
      <div className={styles.returnWidget}>
        <Suspense
          fallback={
            <ClipLoader
              color="#ffffff"
              size={150}
              aria-label="Loading Spinner"
              data-testid="loader"
            ></ClipLoader>
          }
        >
          <div>
            <PredictionForm onSubmit={handleFormSubmit} />
            {predictionParams && (
              <StockPredictionChart
                stock={predictionParams.ticker}
                startDate={predictionParams.startDate}
                endDate={predictionParams.endDate}
                days={predictionParams.days}
              />
            )}
          </div>
        </Suspense>
      </div>
    </div>
  );
}
