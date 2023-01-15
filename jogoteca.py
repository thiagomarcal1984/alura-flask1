from flask import Flask, render_template, request, redirect

app = Flask(__name__) 

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')

lista = [ jogo1, jogo2, jogo3]

@app.route("/")
def index():
    return render_template("lista.html", titulo="Jogos", jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo="Novo Jogo")

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect("/")

@app.route('/login')
def login():
    return render_template('login.html', titulo="Faça seu login")

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'alohomora' == request.form['senha']:
        return redirect("/")
    else:
        return redirect("/login")

# A aplicação roda a partir do comando: python <nome_do_arquivo>.py.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# Para usar "flask run", defina a variável de ambiente FLASK_APP 
# para o nome do arquivo: ($Env:FLASK_APP=<file>.py ; flask run --port 80).
