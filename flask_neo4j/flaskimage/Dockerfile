
FROM python:3.6-alpine
MAINTAINER "Paolo D'Onorio De Meo <p.donoriodemeo@cineca.it>"

COPY requirements.txt /tmp/
WORKDIR /tmp
RUN pip3 install --upgrade \
    --force-reinstall --no-cache-dir -r requirements.txt

ENV TERM=xterm-256color
