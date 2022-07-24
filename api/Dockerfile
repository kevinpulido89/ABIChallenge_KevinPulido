FROM python:3.10.5-slim

LABEL Name=Sentiment_Analysis_API_8505 Version=2.0.1

# Maintainer info
LABEL maintainer="kevinp8001@gmail.com"

WORKDIR /code/

ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /code/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN python -c "import nltk; nltk.download('omw-1.4'); nltk.download('wordnet')"

COPY . /code

EXPOSE 8505