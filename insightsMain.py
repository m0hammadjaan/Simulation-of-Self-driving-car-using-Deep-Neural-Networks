from Insights import Insights

insights = Insights('AgentPerformance.csv')
insights.plotEpisodeScore()
insights.plotAverageScore()
insights.plotBestScore()
insights.plotEpsilon()
insights.plotMultipleFeatures('Score', 'AverageScore', 'BestScore')
insights.plotSteps()