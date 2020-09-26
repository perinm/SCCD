from flask import Flask

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

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
