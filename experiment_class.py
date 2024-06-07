from trajectory import Trajectories
from loading_data import LoadData

class Experiment():
    def __init__(self, max_trajectories, all_connections):
        self.max_trajectories = max_trajectories
        self.all_trajectories = {}
        self.all_connections = all_connections

    def run(self):
        for i in range(0, self.max_trajectories):
            trajectory = Trajectories(self.all_connections, 120)
            self.all_trajectories[f"train_{i + 1}"] = trajectory.add_trajectory()

        return self.all_trajectories

    def to_csv(self, file_path):
        with open(experiment_path, "w", newline="") as output_file:
            csv_writer = csv.writer(output_file)

            # write header
            csv_writer.writerow(["Train", "Stations"])

            for train, stations in self.all_trajectories.items():
                csv_writer.writerow((train, stations))

    def calculate_score(self):
        # TODO: implement
        p =
        k =
        minutes = 0
        for trajectory in self.all_trajectories():

        return 1000


data = LoadData('files/ConnectiesHolland.csv', 'files/StationsHolland.csv')
all_connections = data.connections
my_experiment = Experiment(7, all_connections)
print(my_experiment.run())
# my_experiment.make_pairs()
