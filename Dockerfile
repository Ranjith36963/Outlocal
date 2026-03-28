FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install chromium --with-deps

COPY . .
RUN mkdir -p /app/data

ENV APP_ENV=production
ENV DATABASE_URL=sqlite:///./data/outlocal.db

EXPOSE 8000

CMD ["uvicorn", "src.outlocal.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
