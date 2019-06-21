import time
import os

from Cursorclass import Cursor
from SemanticsClass import Semantics
from TableClass import Table
from HashTableClass import HashTable
from config import OUTPUT_DIR

def LeftDeepTree(data, parml, parmr):
    result_table = data[0]
    for i in range(1, len(data)):
        result_table = Table(HashJoin(data[i - 1].Table(), data[i].Table(), parml[i - 1], parmr[i-1]), False)
        data[i] = result_table
    return result_table


def HashJoin(R, S, r, s):
    results2 = []
    keyr, keys = 0, 0
    Rrow, Rcol = R
    Srow, Scol = S

    HR = HashTable(len(Rrow))
    for x in range(0, len(Rcol)):
        if Rcol[x] in r:
            keyr = x

    for k in range(0, len(Rrow)):
        HR.insert(Rrow[k][keyr], Rrow[k])

    for z in range(0, len(Scol)):
        if Scol[z] in s:
            keys = z

    for v in range(0, len(Rcol)):
        Scol.append(Rcol[v])

    results2.append(Scol)

    for y in range(0, len(Srow)):
        tuple_ = HR.search(Srow[y][keys])
        if tuple_ != None:
            for w in range(0, len(tuple_)):
                Srow[y].append(tuple_[w])
            results2.append(Srow[y])

    return results2


intructions = [
    "Olá!",
    "Esse programa permite que você execute consultas SQL no banco TPCH.",
    "Instruções:",
    "1 - Pressione enter quando o simbolo '>' aparecer para continuar.",
    "2 - Em junções, a operação 'hash join' deve ser especificada.",
    "3 - O operador '*' não poderá ser utilizado na seleção.",
    "Entendeu? Ótimo! :)"
]
for instruction in intructions:
    print(instruction)
    input('>')

cursor = Cursor()
tables = []

query = input("Digite aqui sua consulta SQL: ")
obj2 = Semantics(query)
results, joincolumns = obj2.query_treatment()
joincolleft, joincolright = joincolumns
results = list(results)

num_files = 0
if results[0] != "1":
    for i in range(0, int((len(results)/2))):
        cursor.exec_consulta(results[i])
        tables.append(Table(OUTPUT_DIR + "/query%d.txt" % (i+1), True))
        num_files = i + 1
if results[0] == "1":
    cursor.exec_consulta(query)
    tables.append(Table(OUTPUT_DIR + "/query1.txt", True))

Hr = LeftDeepTree(tables, joincolleft, joincolright)
g = open(OUTPUT_DIR + "/resultado.txt", "w+")
for r in Hr.Rows():
    g.write(str(r)+"\n")

print('Os arquivos ' + ", ".join(["'query%d.txt'" % i for i in range(1, num_files + 1)]) + " e 'resultado.txt' foram criados na pasta '/outputs'.")
input('>')






