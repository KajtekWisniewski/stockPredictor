'use client';

import TradingViewWidget from '@/components/TradingViewWidget';
import styles from '../stockStyles.module.scss';

export default function StocksPage() {
  return (
    <div className={styles.mainDiv}>
      <header className="App-header">
        <h1>My Trading Dashboard</h1>
      </header>
      <div className={styles.stockWidget}>
        <TradingViewWidget />
      </div>
    </div>
  );
}
