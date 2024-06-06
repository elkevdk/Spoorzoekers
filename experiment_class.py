from trajectory import Trajectories
from loading_data import LoadData

class Experiment():
    def __init__(self, max_trajectories, all_connections):
        self.max_trajectories = max_trajectories
        self.all_trajectories = {}
        self.all_connections = all_connections

    def make_pairs(self):
        connection_pairs = set()
        for start_station, connections in self.all_connections.items():
            station_names = list(connections.keys())

            for i in range(len(station_names)):
                # use frozenset inside set
                connection_pairs.add(frozenset((start_station, station_names[i])))

        print(connection_pairs)

    def run(self):
        for i in range(0, self.max_trajectories):
            trajectory = Trajectories(self.all_connections, 120)
            self.all_trajectories[f"train_{i + 1}"] = trajectory.add_trajectory()

        return self.all_trajectories

    # def generate_output(self):
    #     output = ""
    #     for i, route in enumerate(self.routes, 1):
    #         output += f"train_{i},{route}\n"
    #
    #     score = self.calculate_score()
    #     output += f"score,{score}"
    #
    #     return output
    #
    # def calculate_score(self):
    #     p =
    #     k =

data = LoadData('files/ConnectiesHolland.csv', 'files/StationsHolland.csv')
all_connections = data.connections
my_experiment = Experiment(7, all_connections)
print(my_experiment.run())
# my_experiment.make_pairs()
