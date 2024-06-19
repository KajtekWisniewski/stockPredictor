'use client';
import Link from 'next/link';
import styles from './NavBar.module.scss';
import Image from 'next/image';

const NavBar = ({}) => {
  return (
    <>
      <nav className={styles.navbar}>
        <Link className={styles.linkStyle} href={`/stocks/`}>
          <h2>stocks</h2>
        </Link>
        <Link className={styles.linkStyle} href={`/prediction/`}>
          <h2>predictions</h2>
        </Link>
        <Link className={styles.linkStyle} href={`/`}>
          <Image src="/chart_icon.png" width={75} height={75} alt="site logo" />
        </Link>
        <Link className={styles.linkStyle} href={`/docs/`}>
          <h2>documentation</h2>
        </Link>
        <Link className={styles.linkStyle} href={`/account/`}>
          <h2>account</h2>
        </Link>
      </nav>
    </>
  );
};

export default NavBar;
