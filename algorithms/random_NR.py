from algorithms.random_R import Random_R
from algorithms.base import Base
import random

class Random_NR(Random_R):
    """
    Class that runs an experiment with a set of trajectories with filtering the previous station.

    Inherits from Random_NR and adds the filter_connections method to exclude the previous station from possible connections.
    """
    def filter_connections(self, possible_connections, previous_station):
        # Check if a previous station exists
        if previous_station:
            # Only filter if there is more than one possible connection
            if len(possible_connections) > 1:
                # Create an empty list to store the filtered connections
                filtered_connections = []
                # Iterate through each station in possible connections
                for station in possible_connections:
                    # If the station is not the previous station, add it to the filtered list
                    if station != previous_station:
                        filtered_connections.append(station)
                # Update the possible connections with the filtered list
                possible_connections = filtered_connections
                
        return possible_connections
