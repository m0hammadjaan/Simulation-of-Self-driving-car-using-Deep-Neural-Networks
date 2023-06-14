import pandas as pd
import matplotlib.pyplot as plt

class Insights:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
    
    def plotEpisodeScore(self):
        plt.plot(self.data['Episode'], self.data['Score'])
        plt.xlabel('Episode')
        plt.ylabel('Score')
        plt.title('Episode Score')
        plt.show()
    
    def plotAverageScore(self):
        plt.plot(self.data['Episode'], self.data['AverageScore'])
        plt.xlabel('Episode')
        plt.ylabel('Average Score')
        plt.title('Average Score')
        plt.show()
    
    def plotBestScore(self):
        plt.plot(self.data['Episode'], self.data['BestScore'])
        plt.xlabel('Episode')
        plt.ylabel('Best Score')
        plt.title('Best Score')
        plt.show()
    
    def plotEpsilon(self):
        plt.plot(self.data['Episode'], self.data['Epsilon'])
        plt.xlabel('Episode')
        plt.ylabel('Epsilon')
        plt.title('Epsilon')
        plt.show()
    
    
    def plotMultipleFeatures(self, *features):
        for feature in features:
            plt.plot(self.data['Episode'], self.data[feature], label=feature)
        plt.xlabel('Episode')
        plt.ylabel('Value')
        plt.legend()
        plt.title('Multiple Features')
        plt.show()
    def plotSteps(self):
            episodic_steps = [self.data['Steps'][0]]
            for i in range(1, len(self.data['Steps'])):
                episodic_step = self.data['Steps'][i] - self.data['Steps'][i-1]
                episodic_steps.append(episodic_step)
            
            plt.bar(self.data['Episode'], episodic_steps)
            plt.xlabel('Episode')
            plt.ylabel('Episodic Steps')
            plt.title('Steps')
            plt.show()