from flask import Flask, render_template

app = Flask(__name__)# faz referencia para o proprio arquivo garantindo de que vai rodar a aplicação

@app.route('/inicio')
def ola():
    return render_template('lista.html')

app.run(host='0.0.0.0', port=8080)# faz executar a aplicação