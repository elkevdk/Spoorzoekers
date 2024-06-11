import random

class Random_NR():
    """
    Class that runs an experiment with a set of trajectories.

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
    add_trajectory()
        Generates a trajectory within the allowed maximum time.
    """
    def __init__(self, max_trajectories, all_connections, max_time):
        self.max_trajectories = max_trajectories
        self.all_trajectories = {}
        self.all_connections = all_connections
        self.max_time = max_time
        self.trajectory_count = 0

    def add_trajectory(self):
        total_connections = 0
        for connections in self.all_connections.values():
            total_connections += len(connections)

        while self.trajectory_count < self.max_trajectories:

            # initialize list of connections for the current trajectory
            self.connections = []
            # initialize elapsed time
            self.time = 0
            # turn the outer dictionary into a list
            all_connections_list = list(self.all_connections.keys())
            # select a random starting station
            start_station = random.choice(all_connections_list)
            # add starting station to trajectory
            self.connections.append(start_station)

            current_station = start_station
            previous_station = None
            p = 0

            # continue filling trajectory until max time is exceeded
            while self.time <= self.max_time:
                unique_connections = set()
                for trajectory in self.all_trajectories.values():
                    for i in range(len(trajectory) - 1):
                        connection = frozenset((trajectory[i], trajectory[i + 1]))
                        unique_connections.add(connection)

                p = len(unique_connections) / (total_connections / 2)

                # retrieve list of possible connections from the current station
                possible_connections = list(self.all_connections[current_station].keys())

                if p >= 1:
                    return self.all_trajectories

                # try to exclude the previous station from the possible connections
                if previous_station:
                    # only exclude if there are other stations available
                    if len(possible_connections) > 1:
                        # use list comprehension to store all stations in possible all_connections
                        # that are not equal to the previous station
                        new_possible_connections = []
                        for station in possible_connections:
                            if station != previous_station:
                                new_possible_connections.append(station)
                        possible_connections = new_possible_connections

                # if no connections are available, break the loop
                if not possible_connections:
                    break

                # select next station randomly
                next_station = random.choice(possible_connections)
                travel_time = self.all_connections[current_station][next_station]

                # break the loop if adding the next station exceeds the max time
                if self.time + travel_time > self.max_time:
                    break

                # add next station to the current trajectory
                self.connections.append(next_station)
                # update corresponding time
                self.time += travel_time
                # set previous station to the current station for the next iteration
                previous_station = current_station
                current_station = next_station

            self.trajectory_count += 1
            self.all_trajectories[f"train_{self.trajectory_count}"] = self.connections

        return self.all_trajectories
