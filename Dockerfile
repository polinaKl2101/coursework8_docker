FROM python:3.11-slim

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip3 install -r requirements.txt

COPY . .