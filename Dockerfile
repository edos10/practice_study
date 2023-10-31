FROM python:3.10
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
RUN pip3 install uvicorn
RUN apt-get update && apt-get install -y --no-install-recommends \
  && apt-get install -y redis-server \
  && rm -rf /var/lib/apt/lists/*
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
