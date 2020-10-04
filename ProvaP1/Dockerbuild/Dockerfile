FROM debian:10

MAINTAINER Lucas Manchine <lucasperinm@gmail.com>

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      default-jdk \
      ssh \
      openssh-server \
      net-tools \
      curl \
      netcat \
      gnupg \
      libsnappy-dev \
    && rm -rf /var/lib/apt/lists/*

RUN /etc/init.d/ssh start

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/

RUN curl -O https://dist.apache.org/repos/dist/release/hadoop/common/KEYS

RUN gpg --import KEYS

ENV HADOOP_VERSION 3.3.0
ENV HADOOP_URL http://ftp.unicamp.br/pub/apache/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz

RUN set -x \
    && curl -fSL "$HADOOP_URL" -o /tmp/hadoop.tar.gz \
    && tar -xvf /tmp/hadoop.tar.gz -C /opt/ \
    && rm /tmp/hadoop.tar.gz*

RUN ln -s /opt/hadoop-$HADOOP_VERSION/etc/hadoop /etc/hadoop

RUN mkdir /opt/hadoop-$HADOOP_VERSION/logs

RUN mkdir /hadoop-data

ENV HADOOP_HOME=/opt/hadoop-$HADOOP_VERSION
ENV HADOOP_CONF_DIR=/etc/hadoop
ENV MULTIHOMED_NETWORK=1
ENV USER=root
ENV PATH $HADOOP_HOME/bin/:$PATH

COPY ./core-site.xml $HADOOP_HOME/$HADOOP_CONF_DIR/
COPY ./hdfs-site.xml $HADOOP_HOME/$HADOOP_CONF_DIR/

RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa \
    && cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys \
    && chmod -R 0600 ~/.ssh/

ENV HDFS_NAMENODE_USER="root"
ENV HDFS_DATANODE_USER="root"
ENV HDFS_SECONDARYNAMENODE_USER="root"
ENV YARN_RESOURCEMANAGER_USER="root"
ENV YARN_NODEMANAGER_USER="root"

# remover instalacao inves do remove
RUN $HADOOP_HOME/bin/hdfs namenode -format

# Fix JAVA_HOME env variable
COPY ./hadoop-env.sh $HADOOP_HOME/$HADOOP_CONF_DIR/

# Fix for start-dfs
COPY ./hadoop-functions.sh $HADOOP_HOME/libexec/

# Config parameters for yarn
COPY ./mapred-site.xml $HADOOP_HOME/$HADOOP_CONF_DIR/
COPY ./yarn-site.xml $HADOOP_HOME/$HADOOP_CONF_DIR/

EXPOSE 9870 8088

COPY entrypoint.sh /
ENTRYPOINT /entrypoint.sh
