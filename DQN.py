import os
import torch as T
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np


class DeepQNetwork(nn.Module):
    def __init__(self, lr, nActions, name, inputDims, chkptDir):
        super(DeepQNetwork, self).__init__()
        self.checkpointDir = chkptDir
        self.checkpointFile = os.path.join(self.checkpointDir, name)
        self.conv1 = nn.Conv2d(inputDims[0], 32, 8, stride = 4)
        self.conv2 = nn.Conv2d(32, 64, 4, stride = 2)
        self.conv3 = nn.Conv2d(64, 64, 3, stride = 1)
        fcInputDims = self.calculateConvOutputDims(inputDims)

        self.fc1 = nn.Linear(fcInputDims, 512)
        self.fc2 = nn.Linear(512, nActions)
        self.optimizer = optim.Adam(self.parameters(), lr = lr)
        self.loss = nn.MSELoss()
        self.device = T.device('cuda:0' if T.cuda.is_available() else 'cpu')
        self.to(self.device)

    def calculateConvOutputDims(self, inputDims):
        state = T.zeros(1, *inputDims)
        dims = self.conv1(state)
        dims = self.conv2(dims)
        dims = self.conv3(dims)
        return int(np.prod(dims.size()))
    def forward(self, state):
        conv1 = F.relu(self.conv1(state))
        conv2 = F.relu(self.conv2(conv1))
        conv3 = F.relu(self.conv3(conv2))

        convState = conv3.view(conv3.size()[0], -1)
        flat1 = F.relu(self.fc1(convState))
        actions = self.fc2(flat1)
        return actions

    def saveCheckpoint(self):
        print('saving checkpoint...')
        T.save(self.state_dict(), self.checkpointFile)

    def loadCheckpoint(self):
        print('loading checkpoint ...')
        self.load_state_dict(T.load(self.checkpointFile))