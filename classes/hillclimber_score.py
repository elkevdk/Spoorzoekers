from algorithms.hillclimber import HillClimber
import matplotlib.pyplot as plt

class HillClimberScore():
    def __init__(self, amount_runs, remove_counts, all_connections, iterations, trajectories, time, region):
        self.amount_runs = amount_runs
        self.remove_counts = remove_counts
        self.all_connections = all_connections
        self.iterations = iterations
        self.trajectories = trajectories
        self.time = time
        self.region = region

    def run_distributions(self):
        scores = []
        for runs in self.amount_runs:
            for count in self.remove_counts:
                for i in range(self.iterations):
                    hill_climber = HillClimber(self.trajectories, self.all_connections, self.time, iterations=runs, remove_count=count)
                    final_trajectories, final_score = hill_climber.run()
                    scores.append(final_score)

                    if i % 10 == 0 and i != 0:
                        print(f"Iteration {i}")

                plt.figure(figsize=(10, 6))
                plt.hist(scores, bins=20, edgecolor='black')
                plt.title(f'Score Distribution Hill Climber, Holland. Runs: {runs} Trajectories Removed: {count}')
                plt.xlabel('Score')
                plt.ylabel('Frequency')
                plt.savefig(f'output/{self.region}/score_distribution_hillclimber_{runs}_{count}.png')
