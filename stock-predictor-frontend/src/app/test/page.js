import { getServerSession } from 'next-auth';
import { authOptions } from '../api/auth/[...nextauth]/route';
import axios from 'axios';
import { getAccessToken } from '@/components/keycloak/SessionTokenAccessor';
import { SetDynamicRoute } from '@/components/keycloak/setDynamicRoute';
import styles from '../stockStyles.module.scss';

async function getAllStocks() {
  const url = `${process.env.DEMO_BACKEND_URL}/stocks`;

  let accessToken = await getAccessToken();

  try {
    const resp = await axios.get(url, {
      headers: {
        'Content-Type': 'application/json',
        Authorization: 'Bearer ' + accessToken
      }
    });
    return resp.data;
  } catch (error) {
    throw new Error('Failed to fetch data. Status: ' + error.response?.status);
  }
}

export default async function Products() {
  const session = await getServerSession(authOptions);

  if (session && session.roles?.includes('user')) {
    try {
      const stocks = await getAllStocks();

      return (
        <main className={styles.mainPage}>
          <SetDynamicRoute />
          <h1>Products</h1>
          <table>
            <thead>
              <tr>
                <th>Id</th>
                <th>Ticker</th>
                <th>Date of Prediction</th>
                <th>Predicted Return</th>
                <th>Days Predicted</th>
              </tr>
            </thead>
            <tbody>
              {stocks.map((stock) => (
                <tr key={stock.Id}>
                  <td>{stock.id}</td>
                  <td>{stock.ticker}</td>
                  <td>{stock.dateOfPrediction}</td>
                  <td>{stock.predictedReturn}</td>
                  <td>{stock.daysPredicted}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </main>
      );
    } catch (err) {
      console.error(err);

      return (
        <main className={styles.mainPage}>
          <h1>Products</h1>
          <p>Sorry, an error happened. Check the server logs.</p>
        </main>
      );
    }
  }

  return (
    <main className={styles.mainPage}>
      <h1>Unauthorized</h1>
      <p>You do not have permission to view this page.</p>
    </main>
  );
}
