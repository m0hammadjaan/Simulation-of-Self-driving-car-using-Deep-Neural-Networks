import numpy as np
from Agent import Agent
from EnvUtilities import makeEnvironment
from utils import learningRate, epsilonDecay, epsilonMinimum, epsilon, gamma, batchSize, replace, memSize, checkpointDirectory, algorithm, envName
import csv
import warnings


if __name__ == '__main__':
    warnings.filterwarnings("ignore")

    env = makeEnvironment(envName)
    bestScore = -np.inf
    loadCheckpoint = False
    numGames = 500
    agent = Agent(gamma = gamma, epsilon = epsilon, lr = learningRate,
                     inputDims = (env.observation_space.shape),
                     nActions = env.action_space.n, memSize = memSize, epsMin = epsilonMinimum,
                     batchSize = batchSize, replace = replace, epsDec = epsilonDecay,
                     chkptDir = checkpointDirectory, algo = algorithm,
                     envName = envName)
    if  loadCheckpoint:
        agent.loadModel()
    fname = agent.algo+'_'+agent.envName+'_lr'+str(agent.lr)+'_'+str(numGames)+'games'
    nsteps = 0
    scores, epsHistory, stepsArray = [], [], []
    header = ['Episode', 'Score', 'Average Score', 'Best Score', 'Epsilon', 'Steps']

    with open('AgentPerformance.csv', 'w') as file:
        csvfile = csv.writer(file)
        csvfile.writerow(header)

        for i in range(numGames):
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
            stepsArray.append(nsteps)
            avgScore = np.mean(scores[-100:])
            print('Episode:', i, 'Score: %.4f' %score, 'Average Score: %.4f' %avgScore, 'Best Score: %.4f' %bestScore, 'Epsilon: %.4f' %agent.epsilon, 'Steps', nsteps)
            if avgScore > bestScore:
                if not loadCheckpoint:
                    agent.saveModel()
                bestScore = avgScore

            epsHistory.append(agent.epsilon)
            data = [i, score, avgScore, bestScore, agent.epsilon, nsteps]
            csvfile.writerow(data)
