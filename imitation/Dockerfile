FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "-m", "flask", "--debug", "--app", "api/server.py", "run", "--host=0.0.0.0"]