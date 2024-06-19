'use client';

import styles from '../stockStyles.module.scss';
import Link from 'next/link';

export default function DocsPage() {
  return (
    <div className={styles.mainPage}>
      <Link
        className={styles.linkStyle}
        href={`https://github.com/KajtekWisniewski/stockPredictor/blob/main/README.md`}
      >
        <h2>Current models doc on github</h2>
      </Link>
      <Link
        className={styles.linkStyle}
        href={`https://github.com/KajtekWisniewski/stockPredictor/blob/main/model/model_eval/legacy/readme.md`}
      >
        <h2>Legacy models doc on github</h2>
      </Link>
    </div>
  );
}
