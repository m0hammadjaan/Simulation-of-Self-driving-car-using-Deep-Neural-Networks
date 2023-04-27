import numpy as np
from Agent import Agent
from EnvUtilities import makeEnvironment
from utils import learningRate, epsilonDecay, epsilonMinimum, epsilon, gamma, batchSize, replace, memSize, checkpointDirectory, algorithm, envName, getInt
from CSVUtilities import CSVUtils
import csv
import warnings


if __name__ == '__main__':
    warnings.filterwarnings("ignore")

    csvData = CSVUtils('AgentPerformance.csv')

    env = makeEnvironment(envName)
    if csvData.length() > 0:
        bestScore = int(csvData.getLastIndexedData('BestScore'))
        nsteps = int(csvData.getLastIndexedData('Steps'))
        lastEpisode = int(csvData.getLastIndexedData('Episode'))

    else:
        bestScore = -np.inf
        nsteps = 0
        lastEpisode = 0
    numGames = 500


    loadCheckpoint = False
    agent = Agent(gamma = gamma, epsilon = epsilon, lr = learningRate,
                     inputDims = (env.observation_space.shape),
                     nActions = env.action_space.n, memSize = memSize, epsMin = epsilonMinimum,
                     batchSize = batchSize, replace = replace, epsDec = epsilonDecay,
                     chkptDir = checkpointDirectory, algo = algorithm,
                     envName = envName)
    if  loadCheckpoint:
        agent.loadModel()
    fname = agent.algo+'_'+agent.envName+'_lr'+str(agent.lr)+'_'+str(numGames)+'games'
    scores = getInt(list(csvData.data['Score']))

    with open('AgentPerformance.csv', 'a') as file:
        csvfile = csv.writer(file)

        for i in range(lastEpisode if csvData.length() > 0 else 1, lastEpisode + numGames):
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
            if avgScore >= bestScore:
                if not loadCheckpoint:
                    agent.saveModel()
                bestScore = avgScore

            data = [i, score, avgScore, bestScore, agent.epsilon, nsteps, int(done)]
            csvfile.writerow(data)
