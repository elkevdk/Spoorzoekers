from algorithms.random_R import Random_R
import random

class Random_NR(Random_R):
    """
    Class that runs an experiment with a set of trajectories with filtering the previous station.

    Inherits from Random_NR and adds the filter_connections method to exclude the previous station from possible connections.
    """
    def filter_connections(self, possible_connections, previous_station):
    # filter out the previous station
        if previous_station:
            if len(possible_connections) > 1:
                possible_connections = [station for station in possible_connections if station != previous_station]
        return possible_connections
