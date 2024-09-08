from bd import nova_conexao
from mysql.connector import ProgrammingError

excluir_tabela_email = """
    DROP TABLE emails;
"""

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(excluir_tabela_email)
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    print(f'Erro Conexão: {e.msg}')
