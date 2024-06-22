'use client';

import { useEffect, useState } from 'react';

const PrivateRoute = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const fetchAccessToken = async () => {
      try {
        const response = await fetch('/api/fetch-access-token');
        const data = await response.json();

        if (response.ok && data.accessToken) {
          setIsLoggedIn(true);
        } else {
          setIsLoggedIn(false);
        }
      } catch (error) {
        console.error('Error fetching access token:', error);
        setIsLoggedIn(false);
      }
    };

    fetchAccessToken();
  }, []);

  return isLoggedIn ? children : null;
};

export default PrivateRoute;
