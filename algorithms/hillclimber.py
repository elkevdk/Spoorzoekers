from algorithms.random_R import Random_R
from algorithms.base import Base
import random

class HillClimber(Random_R, Base):
    def __init__(self, max_iterations, all_connections, max_time):
        super().__init__({}, 0, all_connections)  # Initialize with empty trajectories
        self.max_iterations = max_iterations
        self.max_time = max_time
        self.best_score = float('-inf')
        self.best_trajectories = {}

    def run(self):
        # Initial random trajectories
        random_r = Random_R(7, self.all_connections, self.max_time)
        initial_trajectories = random_r.add_trajectory()
        self.best_trajectories = initial_trajectories
        self.best_score = self.calculate_score()

        for _ in range(self.max_iterations):
            # Modify trajectories to explore the neighborhood
            new_trajectories = self.modify_trajectories(self.best_trajectories)
            new_score = self.calculate_score(new_trajectories)

            if new_score > self.best_score:
                self.best_trajectories = new_trajectories
                self.best_score = new_score

        return self.best_trajectories, self.best_score

    def modify_trajectories(self, trajectories):
        new_trajectories = trajectories.copy()
        # Ignore the 'score' key when modifying
        trajectory_keys = [key for key in new_trajectories if key != 'score']
        if trajectory_keys:
            trajectory_key = random.choice(trajectory_keys)
            if isinstance(new_trajectories[trajectory_key], list) and len(new_trajectories[trajectory_key]) > 1:
                new_trajectories[trajectory_key] = new_trajectories[trajectory_key][:-1]
        return new_trajectories

    def calculate_score(self, trajectories=None):
        t = self.trajectory_count

        unique_connections = set()
        for key, trajectory in self.all_trajectories.items():
            if key == 'score':  # Skip the score key
                continue
            if not isinstance(trajectory, list):
                raise TypeError(f"Trajectory for key {key} is not a list: {trajectory}")
            for i in range(len(trajectory) - 1):
                connection = frozenset((trajectory[i], trajectory[i + 1]))
                unique_connections.add(connection)

        total_connections = 0
        for connections in self.all_connections.values():
            total_connections += len(connections)

        p = len(unique_connections) / (total_connections / 2)

        minutes = 0
        for key, trajectory in self.all_trajectories.items():
            if key == 'score':  # Skip the score key
                continue
            for i in range(len(trajectory) - 1):
                current_station = trajectory[i]
                next_station = trajectory[i + 1]
                minutes += self.all_connections[current_station][next_station]

        k = p * 10000 - (t * 100 + minutes)

        self.all_trajectories["score"] = k

        return k
