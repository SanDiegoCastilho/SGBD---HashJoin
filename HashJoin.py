def LeftDeepTree(data):
    for i in range(1, len(data)):
    ResultTable = Table(HashJoin(data[i-1], data[i]))
    data[i] = ResultTable

  return ResultTable

def HashhJoin():