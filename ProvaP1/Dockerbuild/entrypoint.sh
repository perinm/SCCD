#!/bin/bash

service ssh start
#if [ -z "$(ssh-keygen -F $IP)" ]; then
#  ssh-keyscan -H $IP >> ~/.ssh/known_hosts
#fi
ssh-keyscan -H localhost >> ~/.ssh/known_hosts
ssh-keyscan -H $(hostname) >> ~/.ssh/known_hosts
$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh

/bin/bash
