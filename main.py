from classes.loading_data import LoadData
from output.visualize import TrainNetwork
from output.visualize2 import PlotTrains
from algorithms.base import Base
from algorithms.random_R import Random_R
from algorithms.random_NR import Random_NR
from algorithms.best_score import Score_Optimizer
from classes.score_distribution import ScoreDistribution
from algorithms.greedy import Greedy
from algorithms.hillclimber import HillClimber
import matplotlib.pyplot as plt
import os

def main():
    # create the output folder if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # ===data for Noord-Holland===
    data = LoadData('data/ConnectiesHolland.csv', 'data/StationsHolland.csv')
    all_connections = data.connections
    all_stations = data.stations

    # # random return algorithm
    # random_r = Random_R(7, all_connections, 120)
    # random_r.add_trajectory()
    # random_r_results = Base(random_r.all_trajectories, random_r.trajectory_count, all_connections)
    # random_r_results.calculate_score()
    #
    # # random no return algorithm
    # random_nr = Random_NR(7, all_connections, 120)
    # random_nr.add_trajectory()
    # random_nr_results = Base(random_nr.all_trajectories, random_nr.trajectory_count, all_connections)
    # random_nr_results.calculate_score()
    #
    # # score_optimizer algorithm
    # score_optimizer = Score_Optimizer(7, all_connections, 120)
    # score_optimizer.add_trajectory()
    # score_optimizer_results = Base(score_optimizer.all_trajectories, score_optimizer.trajectory_count, all_connections)
    # score_optimizer_results.calculate_score()
    #
    # # greedy algorithm
    # greedy = Greedy(7, all_connections, 120)
    # greedy.add_trajectory()
    # greedy_results = Base(greedy.all_trajectories, greedy.trajectory_count, all_connections)
    #
    # # calculate the score
    # score = greedy_results.calculate_score()

    # save results to csv
    # random_r_results.to_csv('output/Holland/output_r.csv')
    # random_nr_results.to_csv('output/Holland/output_nr.csv')
    # score_optimizer_results.to_csv('output/Holland/output_so.csv')
    # greedy_results.to_csv('output/Holland/output_greedy.csv')

    # hill climber algorithm
    # hill_climber = HillClimber(20, all_connections, 180)
    # final_trajectories, final_score = hill_climber.run()
    #
    # # Save results to csv
    # hill_climber_results = Base(final_trajectories, hill_climber.trajectory_count, all_connections)
    # hill_climber_results.to_csv('output/Holland/output_hill_climber.csv')

    amount_runs = [250, 500, 750, 1000]
    remove_counts = [1, 2, 3, 4]
    scores = []
    for runs in amount_runs:
        for count in remove_counts:
            for i in range(10000):
                hill_climber = HillClimber(7, all_connections, 120, iterations=runs, remove_count=count)
                final_trajectories, final_score = hill_climber.run()
                scores.append(final_score)

                if i % 100 == 0 and i != 0:
                    print(f"Iteration {i}")

            plt.figure(figsize=(10, 6))
            plt.hist(scores, bins=20, edgecolor='black')
            plt.title(f'Score Distribution Hill Climber, Holland. Runs: {runs} Trajectories Removed: {count}')
            plt.xlabel('Score')
            plt.ylabel('Frequency')
            plt.savefig(f'output/Holland/score_distribution_hillclimber_{runs}_{count}.png')

    # # Calculate and plot score distribution
    # ScoreDistribution(100, HillClimber, all_connections, 'output/Holland/score_distribution_hill_climber.png', 'Score Distribution Hill Climber, Holland', 20, all_connections, 180)

    # calculate and plot score distribution
    # ScoreDistribution(20000, Random_R, all_connections, 'output/Holland/score_distribution_r.png', 'Score Distribution Random Return', 7, all_connections, 120)
    # ScoreDistribution(20000, Random_NR, all_connections, 'output/Holland/score_distribution_nr.png', 'Score Distribution Random No Return', 7, all_connections, 120)
    # ScoreDistribution(20000, Score_Optimizer, all_connections, 'output/Holland/score_distribution_so.png', 'Score Distribution Optimizer', 7, all_connections, 120)
    # ScoreDistribution(20000, Greedy, all_connections, 'output/Holland/score_distribution_greedy.png', 'Score Distribution Greedy', 7, all_connections, 120)
    #
    # # plot all trajectories
    # plotter = TrainNetwork('data/ConnectiesHolland.csv', 'data/StationsHolland.csv')
    # plotter.create_graph()
    # plotter.plot_graph()
    #
    # # plot covered connections
    # graph_holland = PlotTrains('data/ConnectiesHolland.csv', 'data/StationsHolland.csv')
    # graph_holland.plot_trajectories(random_r.all_trajectories, "Random Return")
    # graph_holland.plot_trajectories(random_nr.all_trajectories, "Random No Return")
    # graph_holland.plot_trajectories(greedy.all_trajectories, "Greedy")
    # graph_holland.plot_trajectories(score_optimizer.all_trajectories, "Score Optimizer")

    # # # ===data for Nederland===
    # data = LoadData('data/ConnectiesNationaal.csv', 'data/StationsNationaal.csv')
    # all_connections = data.connections
    #
    # # random return algorithm
    # random_r = Random_R(20, all_connections, 180)
    # random_r.add_trajectory()
    # random_r_results = Base(random_r.all_trajectories, random_r.trajectory_count, all_connections)
    # random_r_results.calculate_score()
    #
    # # random no return algorithm
    # random_nr = Random_NR(20, all_connections, 180)
    # random_nr.add_trajectory()
    # random_nr_results = Base(random_nr.all_trajectories, random_nr.trajectory_count, all_connections)
    # random_nr_results.calculate_score()
    #
    # # score_optimizer algorithm
    # score_optimizer = Score_Optimizer(20, all_connections, 180)
    # score_optimizer.add_trajectory()
    # score_optimizer_results = Base(score_optimizer.all_trajectories, score_optimizer.trajectory_count, all_connections)
    # score_optimizer_results.calculate_score()
    #
    # # greedy algorithm
    # greedy = Greedy(20, all_connections, 180)
    # greedy.add_trajectory()
    # greedy_results = Base(greedy.all_trajectories, greedy.trajectory_count, all_connections)
    #
    # # calculate the score
    # greedy.add_trajectory()
    # greedy_results.calculate_score()
    #
    # # # save results to csv
    # # random_r_results.to_csv('output/Nederland/NL_output_r.csv')
    # # random_nr_results.to_csv('output/Nederland/NL_output_nr.csv')
    # # score_optimizer_results.to_csv('output/Nederland/NL_output_so.csv')
    # # greedy_results.to_csv('output/Nederland/NL_output_greedy.csv')
    #
    # # calculate and plot score distribution
    # ScoreDistribution(20000, Random_R, all_connections, 'output/Nederland/NL_score_distribution_r.png', 'Score Distribution Random Return, Netherlands', 20, all_connections, 180)
    # ScoreDistribution(20000, Random_NR, all_connections, 'output/Nederland/NL_score_distribution_nr.png', 'Score Distribution Random No Return, Netherlands', 20, all_connections, 180)
    # ScoreDistribution(20000, Score_Optimizer, all_connections, 'output/Nederland/NL_score_distribution_so.png', 'Score Distribution Optimizer, Netherlands', 20, all_connections, 180)
    # ScoreDistribution(20000, Greedy, all_connections, 'output/Nederland/NL_score_distribution_greedy.png', 'Score Distribution Greedy, Netherlands', 20, all_connections, 180)
    #
    # # plot all trajectories
    # plotter = TrainNetwork('data/ConnectiesNationaal.csv', 'data/StationsNationaal.csv')
    # plotter.create_graph()
    # plotter.plot_graph()
    #
    # # plot covered connections
    # graph_NL = PlotTrains('data/ConnectiesNationaal.csv', 'data/StationsNationaal.csv')
    # graph_NL.plot_trajectories(random_r.all_trajectories, "Random Return")
    # graph_NL.plot_trajectories(random_nr.all_trajectories, "Random No Return")
    # graph_NL.plot_trajectories(greedy.all_trajectories, "Greedy")
    # graph_NL.plot_trajectories(score_optimizer.all_trajectories, "Score Optimizer")

if __name__ == "__main__":
    main()
