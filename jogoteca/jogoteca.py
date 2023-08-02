from flask import Flask, render_template, request, redirect, session, flash

class Jogo:
    def __init__(self, nome, categoria, console) -> None:
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('Gog of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)# faz referencia para o proprio arquivo garantindo de que vai rodar a aplicação
app.secret_key = 'alura' # camada de criptografia

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos = lista)


@app.route('/novo')

def novo():
    return render_template('novo.html', titulo = 'Novo Jogo')

# necessário o methods Post para que a função não apareça na barra de endereços
@app.route('/criar', methods=['POST',]) 

def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']    
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'alohomora' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!') # exibe mesangem de usuário logado com sucesso
        return redirect('/')
    else:
        flash('Usuário não logado!')
        return redirect('/login')

# faz executar a aplicação, o debug=True dispensa que fiquemos restartando a aplicação
app.run(host='0.0.0.0', port=8080, debug=True)