'use client';

import { useSession } from 'next-auth/react';
import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import styles from '../stockStyles.module.scss';

export default function CommunityPage() {
  const { data: session, status } = useSession();
  const router = useRouter();
  const [isAdmin, setIsAdmin] = useState(false);
  const [showInfo, setShowInfo] = useState(false);

  useEffect(() => {
    if (status === 'unauthenticated') {
      router.push('/');
      router.refresh();
    }
  }, [status, router]);

  const checkIfAdmin = () => {
    if (session?.roles?.includes('admin')) {
      setIsAdmin(true);
      setShowInfo(true);
    } else {
      setIsAdmin(false);
      setShowInfo(true);
    }
  };

  return (
    <div className={styles.mainPage}>
      <div>
        <div>protected</div>
        <button onClick={checkIfAdmin}>Check if Admin</button>
      </div>
      {showInfo && (
        <>
          {isAdmin ? (
            <div>
              <h2>Community Tab</h2>
              <p>Admin Info: Here is some protected information for admins only.</p>
            </div>
          ) : (
            <h2>Not an Admin</h2>
          )}
        </>
      )}
    </div>
  );
}
