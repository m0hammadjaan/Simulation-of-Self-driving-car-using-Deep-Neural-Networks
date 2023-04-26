import gymnasium as gym
import numpy as np
import collections


class FrameStacking(gym.ObservationWrapper):
    def __init__(self, env, repeat):
        super(FrameStacking, self).__init__(env)
        self.observation_space = gym.spaces.Box(
            low = np.array(env.observation_space.low.repeat(repeat, axis = 0), dtype = np.float32),
            high = np.array(env.observation_space.high.repeat(repeat, axis = 0), dtype = np.float32),
            dtype = np.float32

        )
        self.stack = collections.deque(maxlen = repeat)

    def reset(self, seed = None, options = None):
        self.stack.clear()
        observation, info = self.env.reset(seed = None, options = None)
        for _ in range(self.stack.maxlen):
            self.stack.append(observation)

        return np.array(self.stack).reshape(self.observation_space.low.shape)
    
    def observation(self, observation):
        self.stack.append(observation)
        
        return np.array(self.stack, dtype = None).reshape(self.observation_space.low.shape)
