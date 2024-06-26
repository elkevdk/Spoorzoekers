import random

class Random_R:
    """
    Class that runs an experiment with a set of trajectories without filtering the previous station.

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
    max_time : int
        Maximum time a trajectory is allowed to take.
    trajectory_count : int
        Number of trajectories generated so far.

    Methods
    -------
    calculate_total_connections()
        Calculates total number of connections in all_connections dictionary.
    initialize_trajectory()
        Initializes a trajectory by selecting a random start station.
    select_random_station()
        Selects a random station from all_connections.
    calculate_p(total_connections)
        Calculates the proportion of unique connections used in the trajectories.
    select_next_station(possible_connections)
        Selects the next station randomly from the list of possible connections.
    update_trajectory(next_station, travel_time, current_station)
        Updates the current trajectory with the next station and travel time.
    filter_connections(possible_connections, previous_station)
        Returns the possible connections without filtering out the previous station.
    renumber_trajectories()
        Renumber the trajectories to ensure the keys are numbered 1 through N sequentially.
    add_trajectory()
        Generates a trajectory within the allowed maximum time.
    remove_trajectory()
        Removes a randomly chosen trajectory from the set of trajectories.
    """
    def __init__(self, max_trajectories, all_connections, max_time):
        self.max_trajectories = max_trajectories
        self.all_trajectories = {}
        self.all_connections = all_connections
        self.max_time = max_time
        self.trajectory_count = 0

    def calculate_total_connections(self):
        total_connections = 0
        for connections in self.all_connections.values():
            total_connections += len(connections)
        return total_connections

    def initialize_trajectory(self):
        self.connections = []
        self.time = 0
        start_station = self.select_random_station()
        self.connections.append(start_station)
        return start_station

    def select_random_station(self):
        all_connections_list = list(self.all_connections.keys())
        return random.choice(all_connections_list)

    def calculate_p(self, total_connections):
        unique_connections = set()
        for key, trajectory in self.all_trajectories.items():
            if isinstance(trajectory, list):
                for i in range(len(trajectory) - 1):
                    connection = frozenset((trajectory[i], trajectory[i + 1]))
                    unique_connections.add(connection)
        p = len(unique_connections) / (total_connections / 2)
        return p

    def select_next_station(self, possible_connections):
        return random.choice(possible_connections)

    def update_trajectory(self, next_station, travel_time, current_station):
        self.connections.append(next_station)
        self.time += travel_time
        return current_station, next_station

    def filter_connections(self, possible_connections, previous_station):
        # base class does not filter out the previous station
        return possible_connections

    def renumber_trajectories(self):
        new_all_trajectories = {}
        for i, (key, value) in enumerate(self.all_trajectories.items(), 1):
            if key != "score":
                new_all_trajectories[f"train_{i}"] = value
        self.all_trajectories = new_all_trajectories

    def add_trajectory(self):
        total_connections = self.calculate_total_connections()

        while self.trajectory_count < self.max_trajectories:
            current_station = self.initialize_trajectory()
            previous_station = None

            while self.time <= self.max_time:
                p = self.calculate_p(total_connections)

                if p >= 1:
                    return self.all_trajectories

                possible_connections = list(self.all_connections[current_station].keys())
                possible_connections = self.filter_connections(possible_connections, previous_station)

                if not possible_connections:
                    break

                next_station = self.select_next_station(possible_connections)
                travel_time = self.all_connections[current_station][next_station]

                if self.time + travel_time > self.max_time:
                    break

                previous_station, current_station = self.update_trajectory(next_station, travel_time, current_station)

            self.trajectory_count += 1
            self.all_trajectories[f"train_{self.trajectory_count}"] = self.connections

        self.renumber_trajectories()

        return self.all_trajectories

    def remove_trajectory(self):
        trajectories_to_choose = []
        for key in self.all_trajectories.keys():
            if key != "score":
                trajectories_to_choose.append(key)

        if trajectories_to_choose:
            trajectory_to_remove = random.choice(trajectories_to_choose)
            del self.all_trajectories[trajectory_to_remove]
            self.trajectory_count -= 1
            self.renumber_trajectories()
