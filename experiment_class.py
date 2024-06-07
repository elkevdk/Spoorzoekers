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
