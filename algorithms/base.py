import csv

class Base():
    """
    Class that calculates the score for a set of trajectories, and converts the
    results to a csv file.

    Parameters
    ----------
    all_trajectories : dict
        Dictionary to store trajectories.
    trajectory_count : int
        Number of trajectories generated.
    all_connections : dict
        Dictionary containing all possible connections between stations and their durations.

    Attributes
    ----------
    all_trajectories : dict
        Dictionary to store trajectories.
    all_connections : dict
        Dictionary containing all possible connections between stations and their durations.
    trajectory_count : int
        Number of trajectories generated.

    Methods
    -------
    calculate_score()
        Calculates the final score based on unique connections, total trajectories, and total time.
    calculate_intermediate_score()
        Calculates an intermediate score without including the score in the dictionary.
    to_csv(experiment_path)
        Converts the trajectories and their scores to a CSV file.

    """
    def __init__(self, all_trajectories, trajectory_count, all_connections):
        self.all_trajectories = all_trajectories
        self.all_connections = all_connections
        self.trajectory_count = trajectory_count

    def calculate_score(self):
        t = self.trajectory_count

        # calculate unique connections
        unique_connections = set()
        for trajectory in self.all_trajectories.values():
            for i in range(len(trajectory) - 1):
                connection = frozenset((trajectory[i], trajectory[i + 1]))
                unique_connections.add(connection)

        # calculate the total number of possible connections
        total_connections = 0
        for connections in self.all_connections.values():
            total_connections += len(connections)

        # calculate proportion of unique connections
        p = len(unique_connections) / (total_connections / 2)

        # calculate total travel time
        minutes = 0
        for trajectory in self.all_trajectories.values():
            for i in range(len(trajectory) - 1):
                current_station = trajectory[i]
                next_station = trajectory[i + 1]
                minutes += self.all_connections[current_station][next_station]

        # calculate the final score
        k = p * 10000 - (t * 100 + minutes)

        # store the score in the all_trajectories dictionary
        self.all_trajectories["score"] = k

        return k

    def calculate_intermediate_score(self):
        t = self.trajectory_count

        # calculate unique connections, excluding thee last station in each trajectory
        unique_connections = set()
        for trajectory in self.all_trajectories.values():
            trajectory_loop = trajectory[:-1]
            for i in range(len(trajectory_loop) - 1):
                connection = frozenset((trajectory_loop[i], trajectory_loop[i + 1]))
                unique_connections.add(connection)

        # calculate the total number of possible connectinos
        total_connections = 0
        for connections in self.all_connections.values():
            total_connections += len(connections)

        # calculate the proportion of unique connections
        p = len(unique_connections) / (total_connections / 2)

        # calculate the total travel time, excluding the last station in each trajectory
        minutes = 0
        for trajectory in self.all_trajectories.values():
            for i in range(len(trajectory_loop) - 1):
                current_station = trajectory_loop[i]
                next_station = trajectory_loop[i + 1]
                minutes += self.all_connections[current_station][next_station]

        # calculate the intermediate score
        k = p * 10000 - (t * 100 + minutes)

        self.all_trajectories["score"] = k

        return k

    def to_csv(self, experiment_path):
        with open(experiment_path, "w", newline="") as output_file:
            csv_writer = csv.writer(output_file)

            # write header
            csv_writer.writerow(["train", "stations"])

            # write each trajectory and its stations
            for train, stations in self.all_trajectories.items():
                    csv_writer.writerow((train, stations))
