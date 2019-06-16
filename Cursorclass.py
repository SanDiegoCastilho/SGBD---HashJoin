import MySQLConnector.Connector


class Cursor:
    counter = 0
    isaquery = None
    cursor = MySQLConnector.Connector.conn.cursor()
    query = None

    def __init__(self):
        self.isaquery = "yes"

    def exec_consulta(self, query):
        self.counter += 1
        self.query = query
        self.cursor.execute(self.query)
        f = open("query%d.txt" % self.counter, "w+")
        columns = [column[0] for column in self.cursor.description]
        f.write(str(columns)+"\n")
        for row in self.cursor:
            f.write(str(row)+"\n")

    def columns(self):
        return self.cursor.description

