import { NextResponse } from 'next/server';
import { getServerSession } from 'next-auth/next';
import { authOptions } from '@/app/api/auth/[...nextauth]/route';
import { getAccessToken } from '@/components/keycloak/SessionTokenAccessor';

export async function GET() {
  try {
    const session = await getServerSession(authOptions);

    if (session && session.roles?.includes('user')) {
      const accessToken = await getAccessToken();
      return NextResponse.json({ accessToken });
    } else {
      return NextResponse.json({ error: 'Forbidden' }, { status: 403 });
    }
  } catch (error) {
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
