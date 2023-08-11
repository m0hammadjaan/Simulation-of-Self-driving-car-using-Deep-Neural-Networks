import numpy as np
from Agent import DoubleDQNAgent
from EnvUtilities import makeEnvironment
from utils import learningRate, epsilonDecay, epsilonMinimum, epsilon, gamma, batchSize, replace, memSize, checkpointDirectory, algorithm, envName, getInt
from CSVUtilities import CSVUtils
from Insights import Insights
import csv
import warnings


if __name__ == '__main__':
    warnings.filterwarnings("ignore")

    csvData = CSVUtils('SoftmaxAdamPerformance.csv')

    env = makeEnvironment(envName)
    if csvData.length() > 0:
        bestScore = int(csvData.getLastIndexedData('BestScore'))
        nsteps = int(csvData.getLastIndexedData('Steps'))
        lastEpisode = int(csvData.getLastIndexedData('Episode'))

    else:
        bestScore = -np.inf
        nsteps = 0
        lastEpisode = 0
    numGames = 100


    loadCheckpoint = False
    agent = DoubleDQNAgent(gamma = gamma, epsilon = epsilon, lr = learningRate,
                     inputDims = (env.observation_space.shape),
                     nActions = env.action_space.n, memSize = memSize, epsMin = epsilonMinimum,
                     batchSize = batchSize, replace = replace, epsDec = epsilonDecay,
                     chkptDir = checkpointDirectory, algo = algorithm,
                     envName = envName)
    if  loadCheckpoint:
        agent.loadModel()
    fname = agent.algo+'_'+agent.envName+'_lr'+str(agent.lr)+'_'+str(numGames)+'games'
    scores = getInt(list(csvData.data['Score']))

    with open('SoftmaxAdamPerformance.csv', 'a') as file:
        csvfile = csv.writer(file)

        for i in range(lastEpisode + 1 if csvData.length() > 0 else 1, lastEpisode + numGames + 1):
            done = False
            score = 0
            observation = env.reset(seed = None, options = None)

            while not done:
                env.render()
                action = agent.chooseAction(observation)
                observation_, reward, done, truncated, info = env.step(action)
                score += reward

                if not loadCheckpoint:
                    agent.storeTransition(observation, action, reward, observation_, int(done))

                    agent.learn()

                observation = observation_
                nsteps += 1

            scores.append(score)
            avgScore = np.mean(scores[-100:])
            print('Episode:', i, 'Score: %.4f' %score, 'Average Score: %.4f' %avgScore, 'Best Score: %.4f' %bestScore, 'Epsilon: %.4f' %agent.epsilon, 'Steps:', nsteps, 'Terminal State:', int(done))
            if score >= bestScore:
                if not loadCheckpoint:
                    agent.saveModel()
                bestScore = score


            data = [i, score, avgScore, bestScore, agent.epsilon, nsteps, int(done)]
            csvfile.writerow(data)

    env.close()
    insights = Insights('SoftmaxAdamPerformance.csv')
    insights.plotEpisodeScore()
    insights.plotAverageScore()
    insights.plotBestScore()
    insights.plotEpsilon()
    insights.plotMultipleFeatures('Score', 'AverageScore', 'BestScore')
    insights.plotSteps()