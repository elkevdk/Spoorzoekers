import random
import copy

from algorithms.random_R import Random_R

class Greedy(Random_R):
    """
    Class that generates trajectories using a greedy approach starting from randomly selected stations,
    ensuring each connection is used only once across all trajectories.
    Inherits from Random_R for trajectory generation logic.
    """

    def __init__(self, max_trajectories, all_connections, max_time):
        """
        Initialize the Greedy class.

        Parameters:
        - max_trajectories: Maximum number of trajectories to generate.
        - all_connections: Dictionary containing all possible connections between stations and their durations.
        - max_time: Maximum time a trajectory is allowed to take.
        """
        super().__init__(max_trajectories, all_connections, max_time)
        self.used_connections = set()  # Set to track used connections globally

    def make_trajectory(self, city, count, max_time, all_connections):
        """
        Create a trajectory starting from the given city using a greedy approach,
        ensuring each connection is used only once across all trajectories.
        """
        endtime = 0
        time_elapsed = 0
        traject = [city]

        while time_elapsed < max_time and city in all_connections:
            best_stop_time = float('inf')
            best_stop_city = ""

            # Filter connections to exclude globally used ones
            possible_connections = [(conn, conn_time) for conn, conn_time in all_connections[city].items() if conn not in self.used_connections]

            # Search for the nearest station in the filtered connections
            for connection, connection_time in possible_connections:
                if connection_time < best_stop_time and connection_time + time_elapsed <= max_time:
                    best_stop_time = connection_time
                    best_stop_city = connection

            if best_stop_city:
                # Update time and mark connection as used globally
                time_elapsed += best_stop_time
                endtime = time_elapsed
                self.used_connections.add(best_stop_city)

                # Update all_connections to remove used connections bidirectionally
                del all_connections[city][best_stop_city]
                del all_connections[best_stop_city][city]

                if not all_connections[city]:
                    del all_connections[city]

                if not all_connections[best_stop_city]:
                    del all_connections[best_stop_city]

                city = best_stop_city
                traject.append(city)
            else:
                endtime = time_elapsed
                break

        # Ensure the trajectory has at least two stations
        if len(traject) == 1:
            connections = self.all_connections[traject[0]]
            endcity = min(connections, key=connections.get)
            endtime = connections[endcity]
            traject.append(endcity)

        self.all_trajectories[f"train_{count}"] = traject

    def add_trajectory(self):
        """
        Add multiple trajectories using the Greedy approach,
        ensuring each connection is used only once across all trajectories.
        """
        for count in range(1, self.max_trajectories + 1):
            start_station = random.choice(list(self.all_connections.keys()))
            self.make_trajectory(start_station, count, self.max_time, copy.deepcopy(self.all_connections))

    def calculate_p_for_trajectory(self, trajectory):
        """
        Calculate the performance measure P for a given trajectory.
        """
        unique_connections = set()
        for i in range(len(trajectory) - 1):
            connection = frozenset((trajectory[i], trajectory[i + 1]))
            unique_connections.add(connection)
        total_connections = self.calculate_total_connections()
        p = len(unique_connections) / (total_connections / 2)
        return p

    def filter_connections(self, possible_connections, previous_station):
        """
        Filter connections to exclude the previous station.
        """
        if previous_station in possible_connections:
            possible_connections.remove(previous_station)
        return possible_connections
