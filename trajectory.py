import random
from loading_data import LoadData

class Trajectories:
        """
        A class used to represent a trajectory.

        ...

        Parameters
        ----------
        all_connections : dict
            Contains all possible connections between stations and the corresponding
            duration.

        Attributes
        ----------
        speed : float
            speed of the creature.

        Methods
        -------
        step()
            simulate step of creature.
        """
    def __init__(self, all_connections, max_time):
        self.max_time = max_time
        self.all_connections = all_connections

    def add_trajectory(self):
        self.connections = []
        self.time = 0
        all_connections_list = list(self.all_connections.keys())
        start_station = random.choice(all_connections_list)
        self.connections.append(start_station)

        current_station = start_station
        previous_station = None


        while self.time <= self.max_time:
            possible_connections = list(self.all_connections[current_station].keys())

            # Try to exclude the previous station from the possible connections
            if previous_station:
                # Only exclude if there are other options available
                if len(possible_connections) > 1:
                    possible_connections = [station for station in possible_connections if station != previous_station]

            # If no connections are available, break the loop
            if not possible_connections:
                break

            next_station = random.choice(possible_connections)
            travel_time = self.all_connections[current_station][next_station]

            if self.time + travel_time > self.max_time:
                break

            self.connections.append(next_station)
            self.time += travel_time
            previous_station = current_station  # Update previous station
            current_station = next_station  # Move to the next station

        return self.connections
