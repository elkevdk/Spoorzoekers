from algorithms.hillclimber import HillClimber
import matplotlib.pyplot as plt

class HillClimberScore():
    """
    Class that runs multiple hill-climbing experiments and generates score distributions.

    Parameters
    ----------
    amount_runs : list of int
        List of the number of runs for each experiment.
    remove_counts : list of int
        List of the number of trajectories to remove in each experiment.
    all_connections : dict
        Dictionary containing all possible connections between stations and their durations.
    iterations : int
        Number of iterations for each hill climber run.
    trajectories : dict
        Dictionary to store trajectories.
    time : int
        Maximum time a trajectory is allowed to take.
    region : str
        Region name used for saving the output files.

    Attributes
    ----------
    amount_runs : list of int
        List of the number of runs for each experiment.
    remove_counts : list of int
        List of the number of trajectories to remove in each experiment.
    all_connections : dict
        Dictionary containing all possible connections between stations and their durations.
    iterations : int
        Number of iterations for each hill climber run.
    trajectories : dict
        Dictionary to store trajectories.
    time : int
        Maximum time a trajectory is allowed to take.
    region : str
        Region name used for saving the output files.

    Methods
    -------
    run_distributions()
        Runs hill climber experiments and generates score distributions as histograms.
    """
    def __init__(self, amount_runs, remove_counts, all_connections, iterations, trajectories, time, region):
        self.amount_runs = amount_runs
        self.remove_counts = remove_counts
        self.all_connections = all_connections
        self.iterations = iterations
        self.trajectories = trajectories
        self.time = time
        self.region = region

    def run_distributions(self):
        """
        For each combination of runs and remove_counts, this method runs the hill-climbing
        optimization for the specified number of iterations, collects the final scores,
        and plots a histogram of the score distribution. The histogram is saved to a file in the output folder.
        """
        scores = []
        for runs in self.amount_runs:
            for count in self.remove_counts:
                for i in range(self.iterations):
                    hill_climber = HillClimber(self.trajectories, self.all_connections, self.time, iterations=runs, remove_count=count)
                    final_trajectories, final_score = hill_climber.run()
                    scores.append(final_score)

                    if i % 10 == 0 and i != 0:
                        print(f"Iteration {i}")

                # plot and save the histogram
                plt.figure(figsize=(10, 6))
                plt.hist(scores, bins=20, edgecolor='black')
                plt.title(f'Score Distribution Hill Climber, Holland. Runs: {runs} Trajectories Removed: {count}')
                plt.xlabel('Score')
                plt.ylabel('Frequency')
                plt.savefig(f'output/{self.region}/score_distribution_hillclimber_{runs}_{count}.png')
