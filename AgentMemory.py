import numpy as np


class AgentMemory:
    def __init__(self, maxSize, inputShape, nActions):
        self.memSize = maxSize
        self.memCounter = 0
        self.stateMemory = np.zeros((self.memSize, *inputShape),
                                    dtype = np.float32)
        self.newStateMemory = np.zeros((self.memSize, *inputShape),
                                       dtype = np.float32)
        self.actionMemory = np.zeros(self.memSize, dtype = np.int64)
        self.rewardMemory = np.zeros(self.memSize, dtype = np.float32)
        self.terminalMemory = np.zeros(self.memSize, dtype = np.uint8)

    def storeTransition(self, state, action, reward, state_, done):
        index = self.memCounter % self.memSize
        self.stateMemory[index] = state
        self.newStateMemory[index] = state_
        self.actionMemory[index] = action
        self.rewardMemory[index] = reward
        self.terminalMemory[index] = done
        self.memCounter+=1

    def sampleMemoryBuffer(self, batch_size):
        maxMemory = min(self.memCounter, self.memSize)
        batch = np.random.choice(maxMemory, batch_size, replace = True)
        states = self.stateMemory[batch]
        actions = self.actionMemory[batch]
        rewards = self.rewardMemory[batch]
        states_ = self.newStateMemory[batch]
        dones = self.terminalMemory[batch]

        return states, actions, rewards, states_, dones 
