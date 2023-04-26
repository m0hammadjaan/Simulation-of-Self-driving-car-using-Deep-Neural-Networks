import gymnasium as gym
import numpy as np
import cv2
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 


class FramePreprocessing(gym.ObservationWrapper):

    def __init__(self, shape, env = None):
        super(FramePreprocessing, self).__init__(env)
        self.shape = (shape[2], shape[0], shape[1])
        self.observation_space = gym.spaces.Box(low = float(0), high = float(1), 
                                                shape = self.shape, dtype = object)
    
    def observation(self, obs):

        if len(obs.shape) == 3 and obs.shape[2] > 1:
            newFrame = cv2.cvtColor(obs, cv2.COLOR_RGB2GRAY)
        else:
            newFrame = obs
        
        resizedScreen = cv2.resize(newFrame, self.shape[1:],
                                   interpolation=cv2.INTER_AREA)
        
        newObs = np.array(resizedScreen, dtype=np.uint8).reshape(self.shape)
        newObs = newObs/255
        
        return newObs