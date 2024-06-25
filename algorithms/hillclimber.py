import copy
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
    """

    def __init__(self, max_trajectories, all_connections, max_time, iterations=10):
        super().__init__(max_trajectories, all_connections, max_time)
        self.iterations = iterations
        self.current_score = self.calculate_current_score()

    def calculate_current_score(self):
        base = Base(self.all_trajectories, self.trajectory_count, self.all_connections)
        return base.calculate_score()

    def run(self):
        for iteration in range(self.iterations):
            new_random_r = copy.deepcopy(self)
            new_random_r.remove_trajectory()
            new_random_r.add_trajectory()

            new_base = Base({k: v for k, v in new_random_r.all_trajectories.items() if k != "score"},
                            new_random_r.trajectory_count,
                            self.all_connections)
            new_score = new_base.calculate_score()

            if new_score > self.current_score:
                self.all_trajectories = new_random_r.all_trajectories
                self.trajectory_count = new_random_r.trajectory_count
                self.current_score = new_score
                print(f"Iteration {iteration + 1}: New better score found: {self.current_score}")

        return self.all_trajectories, self.current_score
