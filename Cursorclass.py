import Connector.py
import os


class Cursor:
    counter = 0
    isaquery = None
    cursor = MySQLConnector.Connector.conn.cursor()
    query = None

    def __init__(self):
        self.isaquery = "yes"

    def exec_consulta(self, query):
        self.counter += 1
        tuplas = []
        self.query = query
        self.cursor.execute(self.query)
        file = open("query%d.txt" % self.counter, "w+")
        for row in self.cursor:
            tuplas.append(str(row))
        for i in range(0, len(tuplas)):
            file.write(tuplas[i] + "\n")
