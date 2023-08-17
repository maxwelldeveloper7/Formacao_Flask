from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)# faz referencia para o proprio arquivo garantindo de que vai rodar a aplicação
app.secret_key = 'alura' # camada de criptografia

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGDB}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGDB = 'mysql+mysqlconnector',
        usuario = 'dev',
        senha = '#Developer7',
        servidor = 'localhost',
        database = 'jogoteca'
    )

db = SQLAlchemy(app)



# faz executar a aplicação, o debug=True dispensa que fiquemos restartando a aplicação
app.run(host='0.0.0.0', port=8080, debug=True)