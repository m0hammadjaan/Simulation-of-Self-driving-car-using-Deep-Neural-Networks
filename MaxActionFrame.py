import gymnasium as gym
import numpy as np


class MaxActionFrame(gym.Wrapper):

    def __init__(self, env = None, repeat = 4, clipRewards = False, numOperations = 0, fireFirst = False):

        super(MaxActionFrame, self).__init__(env)
        self.repeat = repeat
        self.shape = env.observation_space.low.shape
        self.frameBuffer = np.zeros_like((2, self.shape))
        self.clipRewards = clipRewards
        self.numOperations = numOperations
        self.fireFirst = fireFirst

    def step(self, action):

        totalReward = float(0)
        done = False 

        for i in range(self.repeat):
            obs, reward, done, truncated, info = self.env.step(action)
            if self.clipRewards:
                reward = np.clip(np.array([reward]), -1, 1)[0]
            totalReward+=reward
            idx = i%2
            self.frameBuffer[idx] = obs

            if done:
                break

        maxFrame = np.maximum(self.frameBuffer[0], self.frameBuffer[1])

        return maxFrame, totalReward, done, truncated, info
    
    def reset(self, seed = None, options = None):

        obs = self.env.reset(seed = None, options = None)
        numObservation = np.random.randint(self.numOperations)+1 if self.numOperations > 0 else 0
        for _ in range(numObservation):
            _, _, done, _, _ = self.env.step(0)
            if done:
                self.env.reset(seed = None, options = None)
        if self.fireFirst:
            assert self.env.unwrapped.get_action_meanings()[1] == 'FIRE'
            obs, _, _, _, _ = self.env.step(1)
        self.frameBuffer = np.zeros_like((2, self.shape))
        self.frameBuffer[0] = obs

        return obs
