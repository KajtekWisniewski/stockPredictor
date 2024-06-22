'use client';

import styles from '../stockStyles.module.scss';
import FetchStocks from '@/components/FetchStocks';

export default function Home() {
  return (
    <div>
      <div className={styles.mainPage}>
        <FetchStocks></FetchStocks>
      </div>
    </div>
  );
}
