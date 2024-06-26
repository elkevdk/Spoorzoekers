import random

class Random_R():
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
    calculate_total_connections():
        Calculates total number of connections in all_connections dictionary.
    initialize_trajectory():
        Initializes a trajectory by selecting a random start station.
    select_random_station():
        Selects a random station from all_connections.
    calculate_p():
        Calculates the proportion of unique connections used in the trajectories.
    select_next_station():
        Selects the next station randomly from the list of possible connections.
    update_trajectory():
        Updates the current trajectory with the next station and travel time.
    filter_connections():
        Returns the possible connections without filtering out the previous station.
    renumber_trajectories():
        Renumber the trajectories to ensure the keys are numbered 1 through N sequentially.
    add_trajectory():
        Generates a trajectory within the allowed maximum time.
    remove_trajectory():
        Removes a randomly chosen trajectory from the set of trajectories.
    """
    def __init__(self, max_trajectories, all_connections, max_time):
        self.max_trajectories = max_trajectories
        self.all_trajectories = {}
        self.all_connections = all_connections
        self.max_time = max_time
        self.trajectory_count = 0

    def calculate_total_connections(self):
        # calculate total number of connections in all_connections
        total_connections = 0
        for connections in self.all_connections.values():
            total_connections += len(connections)
        return total_connections

    def initialize_trajectory(self):
        # initialize a trajecory by selecting a random start station
        self.connections = []
        self.time = 0
        start_station = self.select_random_station()
        self.connections.append(start_station)
        return start_station

    def select_random_station(self):
        # select a random station from all_connections
        all_connections_list = list(self.all_connections.keys())
        return random.choice(all_connections_list)

    def calculate_p(self, total_connections):
        # calculate the proportion of unique connections used in the trajectory
        unique_connections = set()
        for key, trajectory in self.all_trajectories.items():
            if isinstance(trajectory, list):
                for i in range(len(trajectory) - 1):
                    connection = frozenset((trajectory[i], trajectory[i + 1]))
                    unique_connections.add(connection)
        p = len(unique_connections) / (total_connections / 2)
        return p

    def select_next_station(self, possible_connections):
        # select the next station randomly from list of possible connections
        return random.choice(possible_connections)

    def update_trajectory(self, next_station, travel_time, current_station):
        # update current trajectory with the next station and travel time
        self.connections.append(next_station)
        self.time += travel_time
        return current_station, next_station

    def filter_connections(self, possible_connections, previous_station):
        # base class does not filter out the previous station
        return possible_connections

    def renumber_trajectories(self):
        # renumber trajectories to ensure keys are numbered 1 through N
        new_all_trajectories = {}
        for i, (key, value) in enumerate(self.all_trajectories.items(), 1):
            if key != "score":
                new_all_trajectories[f"train_{i}"] = value
        self.all_trajectories = new_all_trajectories

    def add_trajectory(self):
        # generate trajectories within allowed maximum time
        total_connections = self.calculate_total_connections()

        # generate trajectories until the maximum number is reached
        while self.trajectory_count < self.max_trajectories:
            current_station = self.initialize_trajectory()
            previous_station = None

            # continue adding stations until max time exceeded
            while self.time <= self.max_time:

                # calculate proportion of unique connections used
                p = self.calculate_p(total_connections)

                # if all unique connections have been used, return trajectories
                if p >= 1:
                    return self.all_trajectories

                # get possible connections for current station
                possible_connections = list(self.all_connections[current_station].keys())
                # filter out previous station
                possible_connections = self.filter_connections(possible_connections, previous_station)

                # if there are no possible connections, break the loop
                if not possible_connections:
                    break

                # select next station randomly
                next_station = self.select_next_station(possible_connections)
                # get the travel time to the next station
                travel_time = self.all_connections[current_station][next_station]

                # if adding this station exceeds the maximum time, break loop
                if self.time + travel_time > self.max_time:
                    break

                # update trajectory with next station and travel time
                previous_station, current_station = self.update_trajectory(next_station, travel_time, current_station)

            # increment trajectory count and store current trajectory
            self.trajectory_count += 1
            self.all_trajectories[f"train_{self.trajectory_count}"] = self.connections

        # renumber trajectoreis for sequential numbering
        self.renumber_trajectories()

        return self.all_trajectories

    def remove_trajectory(self):
        # remove a randomly chosen trajectory from the set of trajectories
        trajectories_to_choose = []
        for key in self.all_trajectories.keys():
            if key != "score":
                trajectories_to_choose.append(key)

        # if there are trajectories to choose from
        if trajectories_to_choose:
            # select a random trajectory to remove
            trajectory_to_remove = random.choice(trajectories_to_choose)
            # remove the selected trajectory
            del self.all_trajectories[trajectory_to_remove]
            # decrement the trajectory count
            self.trajectory_count -= 1
            # renumber the remaining trajectories
            self.renumber_trajectories()
