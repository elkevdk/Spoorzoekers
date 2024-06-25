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
    """

    def __init__(self, max_trajectories, all_connections, max_time, iterations=100, remove_count=1):
        super().__init__(max_trajectories, all_connections, max_time)
        self.iterations = iterations
        self.remove_count = remove_count
        self.current_score = self.calculate_current_score()

    def calculate_current_score(self):
        base = Base(self.all_trajectories, self.trajectory_count, self.all_connections)
        return base.calculate_score()

    def remove_trajectories(self, count):
        for i in range(count):
            self.remove_trajectory()

    def run(self):
        self.changes = 0
        for iteration in range(self.iterations):
            new_random_r = copy.deepcopy(self)
            new_random_r.remove_trajectories(self.remove_count)
            new_random_r.add_trajectory()

            new_trajectories = {}
            for key, value in new_random_r.all_trajectories.items():
                if key != "score":
                    new_trajectories[key] = value

            new_base = Base(new_trajectories, new_random_r.trajectory_count, self.all_connections)
            new_score = new_base.calculate_score()

            if new_score > self.current_score:
                self.all_trajectories = new_random_r.all_trajectories
                self.trajectory_count = new_random_r.trajectory_count
                self.current_score = new_score
                self.changes += 1

        # assign final score to all_trajectories
        self.all_trajectories['score'] = self.current_score

        return self.all_trajectories, self.current_score
