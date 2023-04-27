import pandas as pd

class CSVUtils:
    def __init__(self, fileName):
        self.fileName = fileName
        self.data = pd.read_csv(self.fileName)
    def getLastIndexedData(self, columnName):
        return self.data[columnName][self.data.index[-1]]

    def length(self):
        return len(self.data.index)