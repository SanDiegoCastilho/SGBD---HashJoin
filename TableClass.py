class Table:
    rows = list()
    columns = []

    def __init__(self, file, isfile):
        if isfile:
            arq = open(file, "r+")
            lines = arq.readlines()
            if lines:
                scolumns = lines[0]
                scolumns = scolumns.replace('[', '')
                scolumns = scolumns.replace(']', '')
                scolumns = scolumns.replace(' ', '')
                scolumns = scolumns.replace("'", '')
                scolumns = scolumns.replace("\n", '')
                self.columns = scolumns.split(',')

                self.rows = [[] for _ in range(len(lines)-1)]

                for x in range(1, len(lines)):
                    srows = lines[x]
                    srows = srows.replace('(', '')
                    srows = srows.replace(')', '')
                    srows = srows.replace(' ', '')
                    srows = srows.replace('\n', '')
                    self.rows[x-1] = srows.split(',')
            arq.close()
        else:
            self.columns = file[0]
            self.rows = file

    def Table(self):
        return self.rows, self.columns

    def Rows(self):
        return self.rows

    def Columns(self):
        return self.columns

    def TableSize(self):
        return size
