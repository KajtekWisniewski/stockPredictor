import NextAuth from 'next-auth';
import KeycloakProvider from 'next-auth/providers/keycloak';

const handler = NextAuth({
  providers: [
    KeycloakProvider({
      clientId: 'frontend-client',
      clientSecret: 'wyCGGwKw4ByGwb6JbQLaiuIC7A7C3Q07',
      issuer: 'http://localhost:8080/realms/myrealm'
    })
  ]
});

export { handler as GET, handler as POST };
