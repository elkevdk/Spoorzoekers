import matplotlib.pyplot as plt
from algorithms.base import Base
from algorithms.random_R import Random_R
from algorithms.random_NR import Random_NR
from algorithms.greedy import Greedy

class ScoreDistribution():
    """
    Calculates and plots score distribution for an algorithm over multiple iterations.

    Parameters
    ----------
    iterations : int
        Number of iterations to run the algorithm.
    algorithm_class : class
        The algorithm class to instantiate and run.
    connections : dict
        Dictionary containing all possible connections between stations and their durations.
    file_name : str
        The name of the file to save the plot.
    title : str
        The title of the plot.
    max_trajectories : int
        Maximum number of trajectories to generate.
    all_connections : dict
        Dictionary containing all possible connections between stations and their durations.
    max_time : int
        Maximum time a trajectory is allowed to take.

    Attributes
    ----------
    score_list : list
        List to store scores from each iteration.

    Methods
    -------
    score_distribution()
        Runs the algorithm for the specified number of iterations and stores the scores.
    plot_score()
        Plots the score distribution as a histogram and saves it to a file.
    """
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

        # calculate score distribution
        self.score_distribution()
        # plot it
        self.plot_score()

    def score_distribution(self):
        for i in range(self.iterations):
            # instantiate the algorithm class
            algorithm = self.algorithm_class(self.max_trajectories, self.all_connections, self.max_time)
            # add trajectories
            algorithm.add_trajectory()
            # calculate score for generated trajectories
            results = Base(algorithm.all_trajectories, algorithm.trajectory_count, self.connections)
            self.score_list.append(results.calculate_score())

        return self.score_list

    # function to plot the score distribution as a histogram
    def plot_score(self):
        plt.figure(figsize=(10, 6))
        # plot histogram of scores
        plt.hist(self.score_list, bins=20, edgecolor='black')
        plt.title(self.title)
        plt.xlabel('Score')
        plt.ylabel('Frequency')
        # save plot to file
        plt.savefig(self.file_name)
