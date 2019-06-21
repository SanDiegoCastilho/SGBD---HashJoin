import pyodbc
from config import DB_SERVER, DB_NAME, DB_DRIVER, DB_USER, DB_PASS, DB_PREFIX

# Tenta conectar no banco de dados
try:
    conn_str = 'Driver={%s};Server=%s;Database=%s;' % (DB_DRIVER, DB_SERVER, DB_NAME)
    if DB_USER != '' and DB_PASS != '':
        conn_str += 'user=%s;pwd=%s' % (DB_USER, DB_PASS)
    else:
        conn_str += 'Trusted_Connection=yes'

    conn = pyodbc.connect(conn_str)
    # cursor de consulta
    cursor = conn.cursor()
    # consulta fornecedores
    cursor.execute('select * from %s.NATION' % (DB_PREFIX))
    # printa toda as fileiras da consulta
    for row in cursor:
        print(row)
# Levanta o erro do código, pode haver pretty printing aqui
except pyodbc.DatabaseError as err:
    raise err
