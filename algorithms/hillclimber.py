from algorithms.random_R import Random_R
from algorithms.base import Base
import random

class HillClimber:
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
    all_trajectories : dict
        Dictionary to store trajectories.
    all_connections : dict
        Dictionary containing all possible connections between stations and their durations.
    iterations : int
        Number of iterations to run the hill-climbing algorithm.
    """

    def __init__(self, max_trajectories, all_connections, max_time, iterations=1000):
        self.max_trajectories = max_trajectories
        self.all_trajectories = {}
        self.all_connections = all_connections
        self.max_time = max_time
        self.iterations = iterations
        self.trajectory_count = 0

    def initialize_trajectories(self):
        """Initializes the trajectories using a simple random approach."""
        random_r = Random_R(self.max_trajectories, self.all_connections, self.max_time)
        self.all_trajectories = random_r.add_trajectory()
        self.trajectory_count = random_r.trajectory_count

    def mutate_trajectory(self, trajectory):
        """Mutates a trajectory by altering one of its connections."""
        if len(trajectory) < 3:
            return trajectory  # Not enough connections to mutate

        idx = random.randint(1, len(trajectory) - 2)
        new_station = random.choice(list(self.all_connections[trajectory[idx - 1]].keys()))
        while new_station == trajectory[idx] or new_station in trajectory:
            new_station = random.choice(list(self.all_connections[trajectory[idx - 1]].keys()))

        mutated_trajectory = trajectory[:idx] + [new_station] + trajectory[idx + 1:]
        return mutated_trajectory

    def run(self):
        """Runs the hill-climbing algorithm to optimize trajectories."""
        self.initialize_trajectories()
        base_evaluator = Base(self.all_trajectories, self.trajectory_count, self.all_connections)
        current_score = base_evaluator.calculate_score()

        for _ in range(self.iterations):
            new_trajectories = self.all_trajectories.copy()
            random_train = random.choice(list(new_trajectories.keys())[:-1])  # Exclude the score key
            new_trajectories[random_train] = self.mutate_trajectory(new_trajectories[random_train])

            new_evaluator = Base(new_trajectories, self.trajectory_count, self.all_connections)
            new_score = new_evaluator.calculate_score()

            if new_score > current_score:
                self.all_trajectories = new_trajectories
                current_score = new_score

        return self.all_trajectories, current_score
