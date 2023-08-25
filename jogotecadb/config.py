SECRET_KEY = 'alura' # camada de criptografia

SQLALCHEMY_DATABASE_URI = \
    '{SGDB}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGDB = 'mysql+mysqlconnector',
        usuario = 'dev',
        senha = '#Developer7',
        servidor = 'localhost',
        database = 'jogoteca'
    )