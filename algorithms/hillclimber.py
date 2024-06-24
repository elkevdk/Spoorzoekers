from algorithms.random_R import Random_R

class Hillclimber(Random_R):
    def __init__(self, max_trajectories, all_connections, max_time, step_size):
        super().__init__(max_trajectories, all_connections, max_time)
        self.step_size = step_size
        self.current_solution = None
        self.current_value = None

    def step(iterations):
        for i in range(iterations):
