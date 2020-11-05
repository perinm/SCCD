# 2501

This project has as scope to allow sensor monitoring and generate data for analysis and Machine Learning.

Currently a flask api is implemented that receives temperature data through a get command in the url:

http://45.79.27.184:5000/esp/<tempValue>_<bool1>_<bool2>_<bool3> (replace "<tempValue>" with the temp variable and "<booln>" with 0 or 1)

This received data is stored in an InfluxDB database and visualized in a grafana live dashboard.

Live preview of the data at:

http://45.79.27.184:3000/d/Oo9ql8tGk/henrique?orgId=1&refresh=5s&from=1604606280542&to=1604609880542

# Install

Install docker, docker-compose

At the root of this folder run:
```
sudo docker-compose up -d --build
```

Be happy!

# Code

API: https://github.com/perinm/SCCD/blob/master/flask/2501/app/flask-api.py

Streamlit: https://github.com/perinm/SCCD/blob/master/flask/2501/app/flask-vis.py
