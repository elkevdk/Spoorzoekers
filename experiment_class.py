from trajectory import Trajectories
from loading_data import LoadData
import csv

class Experiment():
    """
    Class that runs an experiment with a set of trajectories.

    Parameters
    ----------
    max_trajectories : int
        Maximum number of trajectories to generate.
    all_connections : dict
        Dictionary containing all possible connections between stations and their durations.

    Attributes
    ----------
    max_trajectories : int
        Maximum number of trajectories to generate.
    all_trajectories : dict
        Dictionary to store trajectories.
    all_connections : dict
        Dictionary containing all possible connections between stations and their durations.

    Methods
    -------
    make_pairs()
        Creates unique pairs of connected stations.
    run()
        Generates trajectories and stores them in all_trajectories.
    """
    def __init__(self, max_trajectories, all_connections):
        self.max_trajectories = max_trajectories
        self.all_trajectories = {}
        self.all_connections = all_connections

    def run(self):
        for i in range(0, self.max_trajectories):
            # create a trajectory instance with a maximum time fo 120
            trajectory = Trajectories(self.all_connections, 120)
            # add generated trajectory to dictionary
            self.all_trajectories[f"train_{i + 1}"] = trajectory.add_trajectory()

        return self.all_trajectories

    def calculate_score(self):
        # TODO: change t to reflect true value
        t = self.max_trajectories

        unique_connections = set()
        for trajectory in self.all_trajectories.values():
            for i in range(len(trajectory) - 1):
                connection = frozenset((trajectory[i], trajectory[i + 1]))
                unique_connections.add(connection)

        total_connections = 0
        for connections in self.all_connections.values():
            total_connections += len(connections)

        p = len(unique_connections) / (total_connections / 2)

        minutes = 0
        for trajectory in self.all_trajectories.values():
            for i in range(len(trajectory) - 1):
                current_station = trajectory[i]
                next_station = trajectory[i + 1]
                minutes += self.all_connections[current_station][next_station]

        k = p * 10000 - (t * 100 + minutes)

        return k

    def to_csv(self, experiment_path):
        with open(experiment_path, "w", newline="") as output_file:
            csv_writer = csv.writer(output_file)

            # write header
            csv_writer.writerow(["train", "stations"])

            for train, stations in self.all_trajectories.items():
                csv_writer.writerow((train, stations))
