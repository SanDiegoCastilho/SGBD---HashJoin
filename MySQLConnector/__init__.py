import pyodbc

# Tenta conectar no banco de dados
try:
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-MOLLHKP;'  # servidor aqui de casa
                          'Database=tpch;'
                          'Trusted_Connection=yes;'
                          # 'user=sa;'
                          # "password=Admin123 se for no lec, aqui em casa é admin
                          )
    # cursor de consulta
    cursor = conn.cursor()
    # consulta fornecedores
    cursor.execute('select * from TPCSOURCE.NATION')
    # printa toda as fileiras da consulta
    for row in cursor:
        print(row)
# Levanta o erro do código, pode haver pretty printing aqui
except pyodbc.DatabaseError as err:
    raise err
