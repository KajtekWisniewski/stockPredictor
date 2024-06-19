'use client';

import TradingViewWidget from '@/components/TradingViewWidget';
import styles from '../stockStyles.module.scss';

export default function StocksPage() {
  return (
    <div className={styles.mainDiv}>
      <div className={styles.stockWidget}>
        <TradingViewWidget />
      </div>
    </div>
  );
}
