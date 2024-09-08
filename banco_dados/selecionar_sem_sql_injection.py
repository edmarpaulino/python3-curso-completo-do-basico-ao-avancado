from bd import nova_conexao

sql = "SELECT * FROM  contatos WHERE nome like %s"

with nova_conexao() as conexao:
    nome = input('Contato a localizar: ')
    args = (f'%{nome}%',)
    # args = ('%'.join(f'{x}' for x in [*nome]),) # = %n%o%m%e%

    cursor = conexao.cursor()
    cursor.execute(sql, args)

    for x in cursor:
        print(x)
