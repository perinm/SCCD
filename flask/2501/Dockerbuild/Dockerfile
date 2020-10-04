FROM python:3.8.6-buster

COPY requirements.txt /tmp
RUN mkdir /code && pip install -r /tmp/requirements.txt

WORKDIR /code
CMD nohup python app.py
