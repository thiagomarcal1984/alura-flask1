from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    flash,
    url_for,
)

app = Flask(__name__) 

# Você só pode escrever na sessão depois de definir a secret key.
app.secret_key = 'alura' 

from jogos import Jogo
lista = Jogo.todos()

from usuarios import Usuario
usuarios = Usuario.todos()

@app.route("/")
def index():
    return render_template("lista.html", titulo="Jogos", jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo="Novo Jogo")

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template(
        'login.html', 
        titulo="Faça seu login", 
        proxima=proxima,
    )

@app.route('/autenticar', methods=['POST'])
def autenticar():
    proxima = request.form.get('proxima')
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(f"Usuário {session['usuario_logado']} logado com sucesso.")
        return redirect(proxima) # Redirecionar pra rota mesmo, não pra função.
    else:
        flash("Usuário não logado.")
        return redirect(url_for('login', proxima=proxima))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso.')
    return redirect(url_for('index'))

# A aplicação roda a partir do comando: python <nome_do_arquivo>.py.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# Para usar "flask run", defina a variável de ambiente FLASK_APP 
# para o nome do arquivo: ($Env:FLASK_APP=<file>.py ; flask run --port 80).
