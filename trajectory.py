import random
from loading_data import LoadData

class Trajectories:
    def __init__(self, all_connections, max_time):
        self.connections = []
        self.max_time = max_time
        self.all_connections = all_connections

    def make_pairs(self):
        connection_pairs = set()
        for start_station, connections in self.all_connections.items():
            station_names = list(connections.keys())

            for i in range(len(station_names)):
                # use frozenset inside set
                connection_pairs.add(frozenset((start_station, station_names[i])))

        print(connection_pairs)

    def add_trajectory(self):
        self.time = 0
        all_connections_list = list(self.all_connections.keys())
        start_station = random.choice(all_connections_list)
        self.connections.append(start_station)

        current_station = start_station
        while self.time <= self.max_time:
            possible_connections = list(self.all_connections[current_station].keys())
            next_station = possible_connections[random.randint(0, len(possible_connections) - 1)]
            travel_time = self.all_connections[current_station][next_station]

            if self.time + travel_time > self.max_time:
                break

            self.connections.append(next_station)
            self.time += travel_time
            current_station = next_station

        return self.connections

# data = LoadData('files/ConnectiesHolland.csv', 'files/StationsHolland.csv')
# all_connections = data.connections
#
# trajectory = Trajectories(all_connections, 120)
# print(trajectory.add_trajectory())