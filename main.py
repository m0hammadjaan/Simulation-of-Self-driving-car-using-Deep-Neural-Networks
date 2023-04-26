import numpy as np
from Agent import Agent
from EnvUtilities import makeEnvironment
import warnings


if __name__ == '__main__':
    warnings.filterwarnings("ignore")

    env = makeEnvironment('highway-v0')
    bestScore = -np.inf
    loadCheckpoint = False
    numGames = 500
    agent = Agent(gamma=0.99, epsilon=1, lr=0.0001,
                     inputDims = (env.observation_space.shape),
                     nActions = env.action_space.n, memSize = 20, epsMin = 0.1,
                     batchSize = 32, replace = 1000, epsDec = 1e-5,
                     chkptDir = 'models/', algo = 'DQNAgent',
                     envName = 'highway-v0')
    if  loadCheckpoint:
        agent.loadModel()
    fname = agent.algo+'_'+agent.envName+'_lr'+str(agent.lr)+'_'+str(numGames)+'games'
    nsteps = 0
    scores, epsHistory, stepsArray = [], [], []

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