#This file is used for debugging and recalling of functionalities for various code snippets

from CSVUtilities import CSVUtils

lastData = CSVUtils('AgentPerformance.csv')

# if lastData.length() > 0:
#     print(lastData.getLastIndexedData('Epsilon'))
# else:
#     print('No data found')

scores = list(lastData.data['Score'])
print(len(scores))