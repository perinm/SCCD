#!/bin/bash

nohup python flask-api.py &
service grafana-server start
nohup influxd &
nohup streamlit run /code/flask-vis.py

/bin/bash
