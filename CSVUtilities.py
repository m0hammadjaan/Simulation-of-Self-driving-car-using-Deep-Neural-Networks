import csv

def writeCSV(colNames, data, fileName):
    with open(fileName, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(colNames)
        for row in data:
            writer.writerow(row)