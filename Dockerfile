# Stage 1

# --platform=linux/amd64
FROM python:3.10-slim

WORKDIR /app

# Stage 2

COPY requirements.txt ./

RUN python -m pip install -r requirements.txt

# Stage 3

COPY bot.py ./

CMD ["python", "bot.py"]