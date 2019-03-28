FROM python:3.6-alpine

RUN mkdir -p /etc/pokemail/

WORKDIR /etc/pokemail/

COPY ./ ./

RUN pip install -r ./requirements.txt