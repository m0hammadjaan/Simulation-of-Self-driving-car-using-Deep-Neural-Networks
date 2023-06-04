import numpy as np
import torch as T
from DQN import DeepQNetwork
from AgentMemory import AgentMemory

class DoubleDQNAgent:
    def __init__(self, gamma, epsilon, lr, nActions, inputDims, batchSize,
                 memSize, epsMin = 0.01, epsDec = 5e-7, replace = 1000,
                 algo = None, envName = None, chkptDir = 'tmp/dqn'):
        self.gamma = gamma
        self.epsilon = epsilon
        self.lr = lr
        self.nActions = nActions
        self.inputDims = inputDims
        self.batchSize = batchSize
        self.epsMin = epsMin
        self.epsDec = epsDec
        self.replaceTargetCount = replace
        self.algo = algo
        self.envName = envName
        self.chkptDir = chkptDir
        self.actionSpace = [i for i in range(nActions)]
        self.learnStepCounter = 0
        self.memory = AgentMemory(memSize, inputDims, nActions)
        self.qEval = DeepQNetwork(self.lr, self.nActions, inputDims = self.inputDims,
                                  name = self.envName + '_' + self.algo + '_qOnline',
                                  chkptDir = self.chkptDir)
        self.qNext = DeepQNetwork(self.lr, self.nActions, inputDims = self.inputDims,
                                  name = self.envName + '_' + self.algo + '_qTarget',
                                  chkptDir = self.chkptDir)
    def chooseAction(self, observation):
        if np.random.random() > self.epsilon:
            state = T.tensor([observation], dtype = T.float).to(self.qEval.device)
            actions = self.qEval.forward(state)
            action = T.argmax(actions).item()
        else:
            action = np.random.choice(self.actionSpace)
        return action
    def storeTransition(self, state, action, reward, state_, done):
        self.memory.storeTransition(state, action, reward, state_, done)

    def sampleMemory(self):
        state, action, reward, newState, done = self.memory.sampleMemoryBuffer(self.batchSize)
        states = T.tensor(state).to(self.qEval.device)
        actions = T.tensor(action).to(self.qEval.device)
        rewards = T.tensor(reward).to(self.qEval.device)
        states_ = T.tensor(newState).to(self.qEval.device)
        dones = T.tensor(done).to(self.qEval.device)

        return states, actions, rewards, states_, dones
    

    def replaceTargetNetwork(self):
        if self.learnStepCounter % self.replaceTargetCount == 0:
            self.qNext.load_state_dict(self.qEval.state_dict())
    
    def decrementEpsilon(self):
        self.epsilon = self.epsilon - self.epsDec if self.epsilon > self.epsMin else self.epsMin

    def saveModel(self):
        self.qEval.saveCheckpoint()
        self.qNext.saveCheckpoint()

    def loadModel(self):
        self.qEval.loadCheckpoint()
        self.qNext.loadCheckpoint()
    
    def learn(self):
        if self.memory.memCounter < self.batchSize:
            return
        
        self.qEval.optimizer.zero_grad()
        self.replaceTargetNetwork()

        states, actions, rewards, states_, dones = self.sampleMemory()
        indices = np.arange(self.batchSize)

        qPred = self.qEval.forward(states)[indices, actions]
        qNext = self.qNext.forward(states_)
        qEval = self.qEval.forward(states_)

        maxActions = T.argmax(qEval, dim = 1)
        qNext[dones] = 0
        qTarget = rewards + self.gamma * qNext[indices, maxActions]
        loss = self.qEval.loss(qTarget, qPred).to(self.qEval.device)
        loss.backward()

        self.qEval.optimizer.step()
        self.learnStepCounter += 1
        self.decrementEpsilon()

