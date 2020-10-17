FROM python:3.8.6-buster

COPY requirements.txt /tmp
RUN mkdir /code && pip install -r /tmp/requirements.txt

WORKDIR /code
CMD nohup python app.py

# Installing grafana
RUN apt-get update \
	&& apt-get install -y apt-transport-https \
				software-properties-common \
				wget \
	&& wget -q -O - https://packages.grafana.com/gpg.key | apt-key add - \
	&& echo "deb https://packages.grafana.com/oss/deb stable main" | tee -a /etc/apt/sources.list.d/grafana.list \
	&& apt-get update \
	&& apt-get install -y grafana

RUN service grafana-server start
