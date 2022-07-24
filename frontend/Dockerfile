FROM python:3.10.5-slim

LABEL Name=Streamlit_Frontend_8504 Version=1.0.0

# Maintainer info
LABEL maintainer="kevinp8001@gmail.com"

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8504

# CMD ["streamlit" , "run", "st_front.py", "--server.port", "8109"] 