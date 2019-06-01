from QueryBox.Cursorclass import Cursor
from QueryBox.SemanticsClass import Semantics
import time
import os

print("Olá!")
time.sleep(1)
print("Esse programa permite que você execute consultas SQL no banco TPCH.")
time.sleep(4)
print("A única restrição é que você deve utilizar ESPAÇOS e VÍRGULAS durante a consulta. Por Exemplo: ")
time.sleep(5)
print("select A , B , C from Tabela1 , Tabela2")
time.sleep(5)
print("Entendeu? Ótimo! :)")
time.sleep(3)

obj = Cursor()

query = input("Digite aqui sua consulta SQL: ")

obj2 = Semantics(query)
results = obj2.queryTreatment()

if results[0] != "1":
    for i in range(0, len(results)):
        obj.exec_consulta(results[i])
if results[0] == "1":
    obj.exec_consulta(query)

time.sleep(20)
print("Limpando tabelas...")
for k in range(1, len(results)+1):
    os.remove("query%d.txt" %k)
time.sleep(1)
print("Tudo feito!")








