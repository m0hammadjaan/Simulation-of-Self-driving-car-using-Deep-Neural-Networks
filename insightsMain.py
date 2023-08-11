from Insights import Insights

insights = Insights('SoftmaxAdamPerformance.csv')
insights.plotEpisodeScore()
insights.plotAverageScore()
insights.plotBestScore()
insights.plotEpsilon()
insights.plotMultipleFeatures('Score', 'AverageScore', 'BestScore')
insights.plotSteps()