from flask import Flask
import os

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

@app.route('/esp/<string:n1>_<string:n2>_<string:n3>')
def esp(n1,n2,n3):
    filename="texto.csv"
    print(f'{n1},{n2},{n3}')
    if os.path.exists(filename):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new if not
    tabela = open(filename,append_write)
    if append_write == 'w':
        tabela.write("n1,n2,n3\n")
    tabela.write(n1+','+n2+','+n3+'\n')
    tabela.close()
    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
