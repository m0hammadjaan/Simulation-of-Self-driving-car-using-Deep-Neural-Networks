from CSVUtilities import CSVUtils

lastData = CSVUtils('AgentPerformance.csv')

learningRate = 0.00025
gamma = 0.95
epsilon = lastData.getLastIndexedData('Epsilon') if lastData.length() > 0 else 1.0
memSize = 20
epsilonMinimum = 0.1
batchSize = 32
replace = 1000
epsilonDecay = 1e-5
checkpointDirectory = 'models/'
algorithm = 'DoubleDQN'
envName = 'highway-v0'

def getInt(lst):
    return [int(i) for i in lst]