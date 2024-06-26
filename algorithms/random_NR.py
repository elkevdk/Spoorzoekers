from algorithms.random_R import Random_R
from algorithms.base import Base
import random

class Random_NR(Random_R):
    """
    Class that runs an experiment with a set of trajectories with filtering the previous station.

    Inherits from Random_NR and adds the filter_connections method to exclude the previous station from possible connections.

    Parameters
    ----------
    possible_connections : list
        List of possible next stations.
    previous_station : str
        The previous station in the trajectory.

    Methods
    -------
    filter_connections(possible_connections, previous_station):
        Filters out the previous station from the list of possible connections if more than one connection is available.
    """
    def filter_connections(self, possible_connections, previous_station):
        # check if a previous station exists
        if previous_station:
            # only filter if there is more than one possible connection
            if len(possible_connections) > 1:
                # create an empty list to store the filtered connections
                filtered_connections = []
                # iterate through each station in possible connections
                for station in possible_connections:
                    # if the station is not the previous station, add it to the filtered list
                    if station != previous_station:
                        filtered_connections.append(station)
                # update the possible connections with the filtered list
                possible_connections = filtered_connections

        return possible_connections
