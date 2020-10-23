# 2501

This project has as scope to allow sensor monitoring and generate data for analysis and Machine Learning.

Currently a flask api is implemented that receives temperature data through a get command in the url:

http://45.79.27.184:5000/esp/<string:temperatura>

Live preview of the data at:

http://45.79.27.184:8502/

# Install

Install docker, docker-compose

Run
```
sudo docker-compose up -d --build
```

Be happy!
