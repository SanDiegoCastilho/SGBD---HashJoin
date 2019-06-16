import pyodbc
import time

# Tenta conectar no banco de dados
try:
    print("Conectando ao banco de dados...")
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-MOLLHKP;'  # servidor aqui de casa
                          'Database=tpch;'
                          'Trusted_Connection=yes;'
                          # 'user=sa;'
                          # "password=Admin123 se for no lec, aqui em casa é admin
                          )
    print("Conexão realizada com sucesso!!")
    #time.sleep(5)

except pyodbc.DatabaseError as err:
    print("Ops, o erro abaixo apareceu:\n")
    raise err

