from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Ana', '98765-4321'),
    ('Bia', '98765-4322'),
    ('Luca', '98765-4323'),
    ('Lu', '98765-4324'),
    ('Gui', '98765-4325'),
    ('Beca', '98765-4326'),
    ('Pedro', '98765-4327'),
)


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros!')
