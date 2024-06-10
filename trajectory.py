import random
from loading_data import LoadData

class ():
    """
    A class used to represent a trajectory.

    ...
    Parameters
    ----------
    all_connections : dict
        Contains all possible connections between stations and the corresponding
        duration.
    max_time : int
        Maximum time a trajectory is allowed to take.

    Attributes
    ----------
    max_time : int
        Maximum time for the trajectory.
    all_connections : dict
        All possible connections between stations and their durations.
    connections : list
        List of stations in the current trajectory
    time : int
        Elapsed time in current trajectory.

    Methods
    -------
    add_trajectory()
        Generates a trajectory within the allowed maximum time.
    """
    def __init__(self, all_connections, max_time):
        self.max_time = max_time
        self.all_connections = all_connections

    def make_pairs(self):
        # initialize set to store pairs in
        connection_pairs = set()
        # loop over stations and connections and store each possible connection
        # as a seperate pair in a set to ensure that the order of the stations
        # doesn't matter and filter duplicates
        for start_station, connections in self.all_connections.items():
            station_names = list(connections.keys())

            for i in range(len(station_names)):
                # use frozenset inside set
                connection_pairs.add(frozenset((start_station, station_names[i])))
