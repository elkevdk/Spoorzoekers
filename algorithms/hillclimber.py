import copy
import matplotlib.pyplot as plt
from algorithms.base import Base
from algorithms.random_R import Random_R

class HillClimber(Random_R):
    """
    Class that runs a hill-climbing optimization to improve a set of trajectories.

    Parameters
    ----------
    max_trajectories : int
        Maximum number of trajectories to generate.
    all_connections : dict
        Dictionary containing all possible connections between stations and their durations.
    max_time : int
        Maximum time a trajectory is allowed to take.
    iterations : int
        Number of iterations to run the hill-climbing algorithm.
    remove_count : int
        Number of trajectories to remove in each iteration.

    Attributes
    ----------
    max_trajectories : int
        Maximum number of trajectories to generate.
    all_connections : dict
        Dictionary containing all possible connections between stations and their durations.
    max_time : int
        Maximum time a trajectory is allowed to take.
    iterations : int
        Number of iterations to run the hill-climbing algorithm.
    remove_count : int
        Number of trajectories to remove in each iteration.
    current_score : float
        The current score of the trajectories.
    changes : int
        Count of how many times the solution has been improved.
    """

    def __init__(self, max_trajectories, all_connections, max_time, iterations=100, remove_count=1):
        super().__init__(max_trajectories, all_connections, max_time)
        self.iterations = iterations
        self.remove_count = remove_count
        self.current_score = self.calculate_current_score()
        self.score_history = []

    def calculate_current_score(self):
        """
        Calculate the current score of the trajectories using the Base class.
        """
        base = Base(self.all_trajectories, self.trajectory_count, self.all_connections)
        return base.calculate_score()

    def remove_trajectories(self, count):
        """
        Remove a specified number of trajectories.
        """
        for i in range(count):
            self.remove_trajectory()

    def run(self):
        """
        Run the hill-climbing optimization algorithm.
        """
        self.changes = 0

        for iteration in range(self.iterations):
            # create a deep copy of the current state
            new_random_r = copy.deepcopy(self)
            # remove trajectories and add a new one
            new_random_r.remove_trajectories(self.remove_count)
            new_random_r.add_trajectory()

            new_trajectories = {}
            # extract new trajectories excluding the score key
            for key, value in new_random_r.all_trajectories.items():
                if key != "score":
                    new_trajectories[key] = value

            # calculate the score for the new set of trajectories
            new_base = Base(new_trajectories, new_random_r.trajectory_count, self.all_connections)
            new_score = new_base.calculate_score()

            # if the new score is better, update the current state
            if new_score > self.current_score:
                self.all_trajectories = new_random_r.all_trajectories
                self.trajectory_count = new_random_r.trajectory_count
                self.current_score = new_score
                self.changes += 1

            self.score_history.append(self.current_score)

        # assign final score to all_trajectories
        self.all_trajectories['score'] = self.current_score

        return self.all_trajectories, self.current_score

    def plot_score_history(self, output_path):
        """
        Plot the score history over iterations.
        """
        plt.plot(range(len(self.score_history)), self.score_history)
        plt.xlabel('Iteration')
        plt.ylabel('Score')
        plt.title('Score Improvement Over Iterations')
        plt.savefig(output_path)
        plt.show()
        plt.close()
