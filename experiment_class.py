from trajectory import Trajectories
from loading_data import LoadData

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


    def run(self):
        for i in range(0, self.max_trajectories):
            # create a trajectory instance with a maximum time fo 120
            trajectory = Trajectories(self.all_connections, 120)
            # add generated trajectory to dictionary
            self.all_trajectories[f"train_{i + 1}"] = trajectory.add_trajectory()

        return self.all_trajectories
