from flask import Flask
from flask import request
import os
from datetime import datetime
from influxdb import InfluxDBClient

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'pyexample')
client.create_database('pyexample')
client.switch_database('pyexample')
app = Flask(__name__)

@app.route('/')
def hello():
    return("Hello World")

@app.route('/hora')
def hora():
    import time
    return time.strftime("%m/%d/%Y, %H:%M:%S")

@app.route('/soma/<int:n1>_<int:n2>')
def soma(n1,n2):
    return f'{n1+n2}'

@app.route('/esp/<string:n1>_<string:n2>')#_<string:n2>_<string:n3>')
def esp(n1,n2,n3=0):
    filename="texto-v1.csv"
    if os.path.exists(filename):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new if not
    tabela = open(filename,append_write)
    if append_write == 'w':
        tabela.write("ip,date,time,T (ºC),estado\n")#,n2,n3\n")
    lista=[str(request.remote_addr),
            datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
            n1,
            n2
    ]
    tabela.write(','.join(lista)+'\n')
    tabela.close()

    #client = InfluxDBClient('localhost', 8086, 'root', 'root', 'pyexample')
    #client.create_database('pyexample')
    #client.switch_database('pyexample')

    json_body = [
    {
        "measurement": "temp_ryuk",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "fields": {
            "value": float(n1),
            "bool": bool(n2)
        }
    }]
    client.write_points(json_body)
    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
