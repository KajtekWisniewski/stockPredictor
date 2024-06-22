'use client';
import Link from 'next/link';
import styles from './NavBar.module.scss';
import Image from 'next/image';
import AuthStatus from '../keycloak/authStatus';
import { useSession } from 'next-auth/react';
import React, { useState, useEffect } from 'react';

const NavBar = ({}) => {
  const { data: session, status } = useSession();

  return (
    <>
      <nav className={styles.navbar}>
        <Link className={styles.linkStyle} href={`/stocks/`}>
          <h2>stocks</h2>
        </Link>
        <Link className={styles.linkStyle} href={`/prediction/`}>
          <h2>predict</h2>
        </Link>
        <Link className={styles.linkStyle} href={`/`}>
          <Image src="/chart_icon.png" width={75} height={75} alt="site logo" />
        </Link>
        <Link className={styles.linkStyle} href={`/docs/`}>
          <h2>docs&emsp;&ensp;</h2>
        </Link>

        <>
          {status === 'unauthenticated' ? (
            <></>
          ) : (
            <Link className={styles.linkStyle} href={`http://localhost:3000/community`}>
              <h2>community tab</h2>
            </Link>
          )}
        </>
        <AuthStatus></AuthStatus>
      </nav>
    </>
  );
};

export default NavBar;
