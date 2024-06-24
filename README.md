# PL - Projekt Łączony na bezp web (gałąź "main") i technologie chmurowe (gałąź "k8s") - Stock Predictor

Projekt akademicki do przewidywania zwrotu z akcji przy użyciu modeli LSTM następujących firm:
APPLE, GOOGLE, MICROSOFT, NVIDIA, AMAZON, META, TSMC, TESLA, WALMART, VISA.

Wykorzystuje keycloak do uwierzytelniania i autoryzacji, api we flasku, api w ASP.NET core oraz nextjs jako klient.

# JAK KORZYSTAĆ

Sklonuj repozytorium na komputer lokalny. Upewnij się, że masz dockera, ponieważ ta aplikacja jest zoptymalizowana tylko dla **dockera lub kubernetes**.

#### DLA WERSJI DOCKER - UŻYJ GAŁĘZI "MAIN"

#### DLA WERSJI KUBERNETES - UŻYJ GAŁĘZI "K8S"

### Wersja Light (ZALECANA)

Ta wersja wykorzystuje losowe fikcyjne dane zamiast modelu ML do tworzenia "prognoz". Jest bardzo lekka i dla
całości kontekstu aplikacja funkcjonalnie jest taka sama. Szczegóły dotyczące wersji ciężkiej znajdują się poniżej sekcji funkcjonalności.

- Przejdź do katalogu stockPredictor
- Odpal Docker Desktop
- (wersja docker): **_docker-compose up --build_** / (wersja kubernetes): **_docker-compose build_**, po zbudowaniu: **_kubectl apply -f k8s_**
- przejść do <http://localhost:3000>(docker) lub <http://localhost:30001>(kubernetes) w przeglądarce
- zarejestruj się, aby uzyskać funkcje użytkownika
  jeśli chcesz mieć funkcje administratora, musisz przejść do <http://localhost:8080>(docker) lub <http://localhost:30002>(kubernetes), zalogować się do keycloak z loginem: **admin**, hasło: **admin**
  zmienić realm na myrealm, przypisać role do konta użytkownika lub utworzyć nowego użytkownika admin -> z ról ogólnych przypisać rolę admin, a z ról klientów (frontend-client, api-client) przypisać admina z obu.

## Funkcjonalności

- strona główna -> wyślij żądanie, aby sprawdzić, czy ASP.NET core api działa poprawnie
- predict -> Wyślij żądanie, aby dokonać prognozy. Rysuje wykres z przewidywanymi wartościami i całkowitym zwrotem. **USER LOGGED IN** -> opcja zapisania wyników w bazie danych
- stocks -> sprawdź obsługiwane wykresy akcji
- login -> logowanie przez keycloak
- community tab -> **dostępna tylko jeśli użytkownik jest zalogowany**, sprawdź czy jesteś adminem, zobacz listę wszystkich prognoz z bazy danych. **USER IS AN ADMIN** -> Usuń dowolną pozycję z bazy danych

### Bardzo ciężka wersja (WYSOCE NIEZALECANA)

jeśli chcesz używać rzeczywistych modeli LSTM do przewidywania, użyj tej wersji, jednak nie są one zbyt dobre i
losowo wygenerowane dane z imitacji faktycznie wyglądają lepiej na wykresach. Obie wersje są funkcjonalnie takie same dla całej aplikacji.

w pliku docker-compose zmiana:

```
flask-imitation:
    build:
      context: ./imitation
```

z ./imitation do ./model

należy pamiętać, że tensorflow i wszystkie wymagane pakiety mają bardzo duży rozmiar, więc kontener wynosi około 7,6 gb.

## O modelu(ach)

Należy zauważyć, że wyniki modeli są bardzo niewiarygodne z następujących powodów:

- ceny akcji lub zwroty można podsumować jako losowe. Dlatego nie można przewidzieć, co stanie się na giełdzie. Nawet gdybyś próbował użyć do tego matematyki lub modeli, gdybyś miał to zrobić sam, prawdopodobnie lepiej byłoby po prostu użyć zdrowego rozsądku do przewidywania. Możesz też rzucić kostką.
- Modele są szkolone na podstawie historii logarytmicznych zwrotów z akcji, które z czasem prawie zawsze wykazują tendencję zwyżkową, co oznacza, że dane są bardzo stronnicze w kierunku pozytywnych wyników, podobnie jak modele.
- Nic nie jest w stanie przewidzieć tego, co wydarzy się na giełdzie, jednak mogłoby odegrać niewielką rolę w zarządzaniu ryzykiem, gdyby działało lepiej (tj. eliminując tendencyjność w kierunku pozytywnych wyników).

### Jakich danych używają modele?

Każdy model wykorzystuje następujące dane do szkolenia

- Ceny akcji od 2010-01-01 do 2024-06-17, w postaci logarytmicznych stóp zwrotu.
- Zestaw treningowy i zestaw walidacyjny to 80/20, tasowane
- Długość sekwencji 30/50/100
- LSTM z 2 warstwami, każda po 100 jednostek, współczynnik porzucania 20%
- Optymalizator Adam, z wczesnym zatrzymaniem
- Funkcja aktywacji: tanh (domyślnie)
- Rozmiar partii: 64, maks. 100 epok

### Poprzednie modele

Readme o poprzednich modelach znajduje się tutaj:
<https://github.com/KajtekWisniewski/stockPredictor/blob/main/model/model_eval/legacy/readme.md>.

## Korzystanie z aplikacji (zakładka prediction)

- Wybierz ticker
- Wybierz zakres czasu, który ma być brany pod uwagę przy prognozowaniu
- Wybierz liczbę dni w przyszłości, dla których ma zostać wykonana prognoza, zakres 7-60

### Zwróci to wykres codziennych przewidywanych zwrotów i skumulowanych zwrotów w wybranym okresie.

# ENG - Stock Predictor

Academic project for stock return predictions using LSTM models of the following companies:
APPLE, GOOGLE, MICROSOFT, NVIDIA, AMAZON, META, TSMC, TESLA, WALMART, VISA.

Uses keycloak for authentication and authorization.

# HOW TO USE

clone the repository to your local machine. Ensure you have docker as this app is optimised for **docker or kubernetes usage only**.

#### FOR DOCKER VERSION - USE BRANCH "MAIN"

#### FOR KUBERNETES VERSION - USE BRANCH "K8S"

### Light version (RECOMMENDED)

This version uses random dummy data instead of ML model to make "predictions". Its very lightweight and for
entire app functionally the same. Details on the heavy version are below the functionalities section.

- navigate to stockPredictor directory
- docker-compose up --build
- go to http://localhost:3000(docker) or http://localhost:30001(kubernetes) in your browser
- register to have user functionalities
  if you want to have admin functionalities, you need to navigate to http://localhost:8080(docker) or http://localhost:30002(kubernetes), login to keycloak with login: **admin**, password: **admin**
  change realm to myrealm, assign roles to your user account or create new admin user -> from general roles assign admin role, and from roles of clients(frontend-client, api-client) assign admin from both.

## Functionalities

- main page -> send a request to test if the ASP.NET core api works properly
- predict -> Send a request to make a prediciton. Draws a graph with predicted values and total return. **USER LOGGED IN** -> Option to save results to the database
- stocks -> check the supported stock charts
- login -> login via keycloak
- community page -> **only available if the user is logged in**, check if you are an admin, see the list of all predicitons from the database. **USER IS AN ADMIN** -> Delete any position from the database

### Very Heavy version (HIGHLY NOT RECOMMENDED)

if you want to use actual LSTM models to make predictions, use this version, however they are not very good and
randomly generated data from imitation actually looks better on the graphs. Both versions are functionally the same for the entire app.

in docker-compose file change:

```
flask-imitation:
    build:
      context: ./imitation
```

from ./imitation to ./model

be wary that tensorflow, and all the required packages are very big in size, so the container totals to around 7.6gb.

## About the model(s)

It should be noted that the results of the models are very unreliable for the following reasons:

- stock prices or returns can be pretty much summarized as being random. Hence it's impossible to predict what will happen on the stock market. Even if you tried using mathematics or models for this, if you was to do it alone, you are propably gonna be better off just using your common sense for predictions. Or you could also throw a dice.
- models are trained on respective stock log-return history, which with time almost always trends bullish, which means that the data is very biased towards positive outcomes and so are the models
- Nothing is able to predict what will happen on the stock market, however it could play a minor role in risk management if it worked better (ie. eliminating bias towards positive outcomes)

### What data do the model(s) use?

Each model uses the following data for training

- Stock prices from 2010-01-01 till 2024-06-17, in form of log-returns
- Training set and validation set are 80/20, shuffled
- Sequence lentgh of either 30/50/100
- LSTM with 2 layers, each with 100 units, 20% dropout rate
- Adam optimizer, with early stopping
- Activation function: tanh (default)
- Batch size: 64, 100 max epochs
- However I can't seem to get validation/train curves from almost going flat, to anything else, no matter what model parameters I use.

### Previous models

Readme about previous models is located here:
<https://github.com/KajtekWisniewski/stockPredictor/blob/main/model/model_eval/legacy/readme.md>

## Using the app (prediction tab)

- Select the ticker
- Select the time range to be considered for prediction
- Select amount of days into to the future for the prediction to be made, range 7-60

### This returns a graph of every day predicted returns and cumulative return over a selected period
