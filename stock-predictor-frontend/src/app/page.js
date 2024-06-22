import Image from 'next/image';
import styles from './stockStyles.module.scss';
import PutRequestComponent from '@/components/TestRequest';

export default function Home() {
  return (
    <div>
      <div className={styles.mainPage}>
        <h1 className={styles.welcomePage}>Welcome to Stock Predictor</h1>
        <Image src="/bar_icon.png" width={150} height={150} alt="site logo" />
        <h3 className={styles.welcomePage}>
          Use LSTM models to predict given stock return
        </h3>
        <PutRequestComponent></PutRequestComponent>
      </div>
    </div>
  );
}
