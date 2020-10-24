#!/bin/bash

nohup influxd &
nohup python flask-api.py &> api.log &
service grafana-server start
nohup streamlit run /code/flask-vis.py

/bin/bash
