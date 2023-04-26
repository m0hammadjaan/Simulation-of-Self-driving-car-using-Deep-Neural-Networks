import gymnasium as gym
from MaxActionFrame import MaxActionFrame
from FramePreprocessing import FramePreprocessing
from FramesStacking import FrameStacking

def makeEnvironment(envName, shape = (84, 84, 1), repeat = 4, clipRewards = False, numOperations = 0, fireFirst = False):
    env = gym.make(envName, render_mode = 'human')
    env = MaxActionFrame(env, repeat, clipRewards, numOperations, fireFirst)
    env = FramePreprocessing(shape, env)
    env = FrameStacking(env, repeat)

    return env