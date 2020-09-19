FROM debian

MAINTAINER Lucas Manchine <lucasperinm@gmail.com>

RUN apt-get update ; \
    apt-get install -y apache2

COPY ./start.sh /

ENTRYPOINT /start.sh
