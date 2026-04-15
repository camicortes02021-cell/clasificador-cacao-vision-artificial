from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return " Proyecto Clasificador de Cacao funcionando "

if __name__ == '__main__':
    print(" Iniciando servidor...")
    app.run(debug=True)