FROM python:3.8.6-buster

COPY requirements.txt /tmp
RUN mkdir /code && pip install -r /tmp/requirements.txt

WORKDIR /code

#CMD nohup python app.py

# Installing grafana
RUN apt-get update \
	&& apt-get install -y apt-transport-https \
				software-properties-common \
				wget \
	&& wget -q -O - https://packages.grafana.com/gpg.key | apt-key add - \
	&& echo "deb https://packages.grafana.com/oss/deb stable main" | tee -a /etc/apt/sources.list.d/grafana.list \
	&& apt-get update \
	&& apt-get install -y grafana

#RUN service grafana-server start

RUN wget -O ~/ryuk.jpg "https://pm1.narvii.com/6578/c17a4c393bd522f338829d6fff065dbeb26f0614_00.jpg" \
    && wget -O ~/peregoso.jpg "https://ichef.bbci.co.uk/news/976/cpsprodpb/7727/production/_103330503_musk3.jpg" \
    && wget -O ~/waru.jpg "https://imaginaire.com/en/images/GHOST-IN-THE-SHELL--MOTOKO-KUSANAGI-44-X-33-STAND-ALONE-COMPLEX-2ND-GIG__0699858996797-Z.JPG"

RUN wget -q -O - https://repos.influxdata.com/influxdb.key | apt-key add - \
    #&& source /etc/os-release \
    && echo "deb https://repos.influxdata.com/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/influxdb.list \
    && apt-get update && apt-get install -y influxdb

COPY influxdb.conf /etc/influxdb/
COPY entrypoint.sh /
ENTRYPOINT /entrypoint.sh

#CMD nohup python flask-api.py
