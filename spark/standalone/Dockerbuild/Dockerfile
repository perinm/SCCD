FROM openjdk:16-slim-buster

COPY entrypoint /

WORKDIR /root

RUN apt update \
    && apt install -y wget \
                      procps \
    && wget https://downloads.apache.org/spark/spark-3.0.1/spark-3.0.1-bin-hadoop3.2.tgz \
    && tar xzf spark-3.0.1-bin-hadoop3.2.tgz \
    && rm spark-3.0.1-bin-hadoop3.2.tgz

ENTRYPOINT /entrypoint
