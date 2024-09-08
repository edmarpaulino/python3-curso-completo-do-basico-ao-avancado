from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

listar_tabelas = """
    SHOW TABLES;
"""

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(listar_tabelas)
            for i, tabela in enumerate(cursor, start=1):
                print(f'Tabela {i}: {tabela[0]}')
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    print(f'Erro Conexão: {e.msg}')
