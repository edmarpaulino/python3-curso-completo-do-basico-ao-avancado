try:
    from mysql import connector as _
except ModuleNotFoundError:
    _
    print('MySQL Connector não instalado!')
else:
    print('MySQL Connector instalado e pronto!')
