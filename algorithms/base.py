import csv

class Base():
    """
    Class that calculates the score for a set of trajectories, and converts the
    results to a csv file.

    Parameters
    ----------
    max_trajectories : int
        Maximum number of trajectories to generate.
    all_connections : dict
        Dictionary containing all possible connections between stations and their durations.
    max_time : int
        Maximum time a trajectory is allowed to take.

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

    """
    def __init__(self, all_trajectories, trajectory_count, all_connections):
        self.all_trajectories = all_trajectories
        self.all_connections = all_connections
        self.trajectory_count = trajectory_count

    def calculate_score(self):
        t = self.trajectory_count

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

        self.all_trajectories["score"] = k

        return k

    def calculate_intermediate_score(self):
        t = self.trajectory_count

        unique_connections = set()
        for trajectory in self.all_trajectories.values():
            trajectory_loop = trajectory[:-1]
            for i in range(len(trajectory_loop) - 1):
                connection = frozenset((trajectory_loop[i], trajectory_loop[i + 1]))
                unique_connections.add(connection)

        total_connections = 0
        for connections in self.all_connections.values():
            total_connections += len(connections)

        p = len(unique_connections) / (total_connections / 2)

        minutes = 0
        for trajectory in self.all_trajectories.values():
            for i in range(len(trajectory_loop) - 1):
                current_station = trajectory_loop[i]
                next_station = trajectory_loop[i + 1]
                minutes += self.all_connections[current_station][next_station]

        k = p * 10000 - (t * 100 + minutes)

        self.all_trajectories["score"] = k

        return k

    def to_csv(self, experiment_path):
        with open(experiment_path, "w", newline="") as output_file:
            csv_writer = csv.writer(output_file)

            # write header
            csv_writer.writerow(["train", "stations"])

            for train, stations in self.all_trajectories.items():
                    csv_writer.writerow((train, stations))
