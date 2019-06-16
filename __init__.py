from QueryBox.Cursorclass import Cursor
from QueryBox.SemanticsClass import Semantics
from HashJoinStructures.TableClass import Table
from HashJoinStructures.HashTableClass import HashTable
import time


def LeftDeepTree(data, parml, parmr):
    result_table = 0
    for i in range(1, len(data)):
        result_table = Table(HashJoin(data[i - 1].Table(), data[i].Table(), parml[i - 1], parmr[i-1]), False)
        data[i] = result_table
    return result_table


def HashJoin(R, S, r, s):
    results2 = list()
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
        tuple = HR.search(Srow[y][keys])
        if tuple != None:
            for w in range(0, len(tuple)):
                Srow[y].append(tuple[w])
            results2.append(Srow[y])

    return results2

print("Olá!")
time.sleep(1)
print("Esse programa permite que você execute consultas SQL no banco TPCH.")
time.sleep(4)
print("A única restrição é que você não pode utilizar * para selecionar todas as colunas, deve faze-lo manualmente:")
time.sleep(5)
print("Entendeu? Ótimo! :)")
time.sleep(3)

obj = Cursor()
tables = list()

query = input("Digite aqui sua consulta SQL: ")
obj2 = Semantics(query)
results, joincolumns = obj2.queryTreatment()
joincolleft, joincolright = joincolumns
results = list(results)

if results[0] != "1":
    for i in range(0, int((len(results)/2))):
        obj.exec_consulta(results[i])
        tables.append(Table("query%d.txt" % (i+1), True))
if results[0] == "1":
    obj.exec_consulta(query)
    tables.append(Table("query1.txt", True))

Hr = LeftDeepTree(tables, joincolleft, joincolright)
g = open("resultado.txt", "w+")
for r in Hr.Rows():
    g.write(str(r)+"\n")








