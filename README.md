# Gameslib

## Features:

    > List games
    > Register games
    > Login 
    > Restrict access



Note about Dockerfile


Attempts to create a container only had an effect on images 1.0.8:

```Dockerfile

FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt


ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

expose 5000
CMD ['flask', 'run']
```


After configuring the flask environment variables, the container can be built

A code change also led to another version of the Dockerfile:

```python
if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000, debug=True) # add host and port in server parameters
```

```Dockerfile

FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

expose 5000
ENTRYPOINT python3 app.py
```


## Dockerfile (1.0.10)

Current dockerfile configuration

```Dockerfile

FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

expose 5000
ENTRYPOINT python3 app.py
```

### Build image

```bash
docker build -t ryann/gamelib:1.0.10
```

### Run container

```bash
docker run -d -it -p 5000:5000 --name gamelib-flask-app-1.0.10 ryann/gamelib:1.0.10 bash
```