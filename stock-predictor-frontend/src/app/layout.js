import { Inter } from 'next/font/google';
import './globals.css';
import NavBar from '@/components/navigation/NavBar';
const inter = Inter({ subsets: ['latin'] });
import SessionProviderWrapper from '@/components/keycloak/SessionProviderWrapper';

export const metadata = {
  title: 'Stock Predictor',
  description: 'stock returns prediction based on LSTM models for each stock'
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <SessionProviderWrapper>
          <NavBar />
          {children}
        </SessionProviderWrapper>
      </body>
    </html>
  );
}
