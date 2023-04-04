FROM python:slim

LABEL maintainer="rezahili"

WORKDIR /opt/src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

CMD python main.py
