# 2501

This project has as scope to allow sensor monitoring and generate data for analysis and Machine Learning.

Currently a flask api is implemented that receives temperature data through a get command in the url:

http://45.79.27.184:5000/esp/temp_value (replace <temp_value> with the temp variable)


Live preview of the data at:

http://45.79.27.184:8502/

# Install

Install docker, docker-compose

At the root of this repository run:
```
sudo docker-compose up -d --build
```

Be happy!

# Code

API: https://github.com/perinm/SCCD/blob/master/flask/2501/app/flask-api.py

Streamlit: https://github.com/perinm/SCCD/blob/master/flask/2501/app/flask-vis.py
