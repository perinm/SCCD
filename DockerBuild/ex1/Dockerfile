FROM debian

MAINTAINER Lucas Manchine 

COPY ./app.py /

RUN apt-get update ; \
    apt-get install -y python-flask ; \
    export FLASK_APP=/app.py

ENTRYPOINT python -m flask run --host=0.0.0.0

#ENTRYPOINT run /app.py
