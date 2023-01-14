from flask import Flask

app = Flask(__name__) 

@app.route("/inicio")
def ola():
    return "<h1>Hello, world!</h1>"


# A aplicação roda a partir do comando: python <nome_do_arquivo>.py.
if __name__ == '__main__':
    app.run(port=8080)

# Para usar "flask run", defina a variável de ambiente FLASK_APP 
# para o nome do arquivo: ($Env:FLASK_APP=<file>.py ; flask run --port 80).
