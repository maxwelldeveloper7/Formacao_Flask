from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)# faz referencia para o proprio arquivo garantindo de que vai rodar a aplicação
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
crsf = CSRFProtect(app)

from views import *

if __name__ == '__main__':

# faz executar a aplicação, o debug=True dispensa que fiquemos restartando a aplicação
    app.run(host='0.0.0.0', port=8080, debug=True)