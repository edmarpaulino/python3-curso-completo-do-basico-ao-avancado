from mysql.connector import connect
from contextlib import contextmanager

parametros = dict(
    host='',
    port='',
    user='',
    passwd='',
    database='agenda'
)


@contextmanager
def nova_conexao():
    conexao = connect(**parametros)
    try:
        yield conexao
    finally:
        if (conexao and conexao.is_connected()):
            conexao.close()
