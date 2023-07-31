from flask import Flask

app = Flask(__name__)# faz referencia para o proprio arquivo garantindo de que vai rodar a aplicação

@app.route('/inicio')
def ola():
    return '<h1>Olá Mundo!</h1>'

app.run()# faz executar a aplicação