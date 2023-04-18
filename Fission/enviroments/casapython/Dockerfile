
FROM python:3.8-buster

RUN apt-get update -y && apt-get install -y python3-dev libev-dev
WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app

RUN mkdir /app/data

ENV PYTHONUNBUFFERED 1
ENTRYPOINT ["python3"]
CMD ["server.py"]
