class Table:
    rows = []
    colunms = []

    def __init__(self, data):
        arq = open("query%.txt" % data + 1, "r")
        lines = arq.readlines()


        for x in range(0, len(lines)):
            self.rows[x] = lines[x].replace(')', '') 
            self.rows[x] = lines[x].replace('(', '') 
            self.rows[x] = lines[x].replace(',', '') 

        arq.close()

    def Rows(self):
    	return self.rows