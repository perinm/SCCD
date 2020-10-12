#!/bin/bash

nohup python flask-api.py &
nohup streamlit run /code/flask-vis.py

/bin/bash
