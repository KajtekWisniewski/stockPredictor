'use client';

import { useSession, signIn, signOut } from 'next-auth/react';
import { useEffect } from 'react';

async function keycloakSessionLogOut() {
  try {
    await fetch(`/api/auth/logout`, { method: 'GET' });
  } catch (err) {
    console.error(err);
  }
}

export default function AuthStatus() {
  const { data: session, status } = useSession();

  useEffect(() => {
    if (
      status != 'loading' &&
      session &&
      session?.error === 'RefreshAccessTokenError'
    ) {
      signOut({ callbackUrl: '/' });
    }
  }, [session, status]);

  if (status == 'loading') {
    return <div>Loading...</div>;
  } else if (session) {
    return (
      <div>
        Logged in as <span>{session.user.email}</span>{' '}
        <button
          onClick={() => {
            keycloakSessionLogOut().then(() => signOut({ callbackUrl: '/' }));
          }}
        >
          Log out
        </button>
      </div>
    );
  }

  return (
    <div>
      Not logged in. <button onClick={() => signIn('keycloak')}>Log in</button>
    </div>
  );
}
