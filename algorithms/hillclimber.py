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
