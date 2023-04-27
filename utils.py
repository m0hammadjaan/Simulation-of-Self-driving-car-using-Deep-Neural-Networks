from CSVUtilities import CSVUtils

lastData = CSVUtils('data.csv')

learningRate = 0.0001
gamma = 0.95
epsilon = lastData.getLastIndexedData('Epsilon')
memSize = 20
epsilonMinimum = 0.1
batchSize = 32
replace = 1000
epsilonDecay = 1e-5
checkpointDirectory = 'models/'
algorithm = 'DQN'
envName = 'highway-v0'