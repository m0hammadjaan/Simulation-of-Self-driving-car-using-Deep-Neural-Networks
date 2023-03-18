import tensorflow as tf
import numpy as np
import os
import random

class CNN:
    def __init__(self, modelName, numActions = 5, target = False):
        self.modelName = modelName
        self,numActions = numActions
        
        self.graph = tf.Graph()
        with self.graph.as_default():
            activation = tf.nn.relu()
            init = tf.keras.initializers.truncated_normal(mean = 0.0, stddev = 1e-5)
            self.learningRate = tf.keras.Input(tf.float32, shape = [])
            self.NewQValues = tf.keras.Input(tf.float32,
                                             shape = [None, numActions],
                                             name = 'NewQValues')
            self.countEpisodes = tf.Variable(initial_value = 0,
                                        trainable = False,
                                        dtype = tf.int64,
                                        name = 'countEpisodes')
            self.countStates = tf.Variable(initial_value = 0,
                                           trainable = False,
                                           dtype = tf.int64,
                                           name = 'countStates')
            
            