FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

expose 5000
ENTRYPOINT python3 app.py