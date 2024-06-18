import matplotlib.pyplot as plt
from algorithms.base import Base
from algorithms.random_R import Random_R
from algorithms.random_NR import Random_NR
from algorithms.greedy import Greedy

class ScoreDistribution():
    def __init__(self, iterations, algorithm_class, connections, file_name, title, max_trajectories, all_connections, max_time):
        self.iterations = iterations
        self.algorithm_class = algorithm_class
        self.connections = connections
        self.file_name = file_name
        self.title = title
        self.max_trajectories = max_trajectories
        self.all_connections = all_connections
        self.max_time = max_time
        self.score_list = []

        self.score_distribution()
        self.plot_score()

    def score_distribution(self):
        for i in range(self.iterations):
            algorithm = self.algorithm_class(self.max_trajectories, self.all_connections, self.max_time)
            algorithm.add_trajectory()
            results = Base(algorithm.all_trajectories, algorithm.trajectory_count, self.connections)
            self.score_list.append(results.calculate_score())

        return self.score_list

    # function to plot the score distribution as a histogram
    def plot_score(self):
        plt.figure(figsize=(10, 6))
        plt.hist(self.score_list, bins=20, edgecolor='black')
        plt.title(self.title)
        plt.xlabel('Score')
        plt.ylabel('Frequency')
        plt.savefig(self.file_name)
