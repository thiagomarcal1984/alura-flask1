from flask import Flask, render_template

app = Flask(__name__) 

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route("/inicio")
def ola():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
    jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')

    lista = [ jogo1, jogo2, jogo3]

    return render_template("lista.html", titulo="Jogos", jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo="Novo Jogo")

# A aplicação roda a partir do comando: python <nome_do_arquivo>.py.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# Para usar "flask run", defina a variável de ambiente FLASK_APP 
# para o nome do arquivo: ($Env:FLASK_APP=<file>.py ; flask run --port 80).
