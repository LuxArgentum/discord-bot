FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY bot.py ./

EXPOSE 8000

CMD ["python", "bot.py"]