from mysql.connector import connect

conexao = connect(
    host='',
    port='',
    user='',
    passwd=''
)

cursor = conexao.cursor()
cursor.execute('CREATE DATABASE agenda')
