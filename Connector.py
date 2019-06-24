import pyodbc
import time
from config import DB_SERVER, DB_NAME, DB_DRIVER, DB_USER, DB_PASS

# Tenta conectar no banco de dados
try:
    print("Conectando ao banco de dados...")
    conn_str = 'Driver={%s};Server=%s;Database=%s;' % (DB_DRIVER, DB_SERVER, DB_NAME)
    if DB_USER != '' and DB_PASS != '':
        conn_str += 'user=%s;pwd=%s' % (DB_USER, DB_PASS)
    else:
        conn_str += 'Trusted_Connection=yes'

    conn = pyodbc.connect(conn_str)
    print("Conexão realizada com sucesso.")
    #time.sleep(5)

except pyodbc.DatabaseError as err:
    print("Ops, o erro abaixo apareceu:\n")
    raise err

