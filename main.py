from classes.loading_data import LoadData
from output.visualize import TrainNetwork
from algorithms.base import Base
from algorithms.random_R import Random_R
from algorithms.random_NR import Random_NR
from algorithms.best_score import Score_Optimizer
from classes.score_distribution import ScoreDistribution
from algorithms.greedy import Greedy
import os

def main():
    # create the output folder if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')
    #
    # # data for Noord-Holland
    # data = LoadData('data/ConnectiesHolland.csv', 'data/StationsHolland.csv')
    # all_connections = data.connections
    # all_stations = data.stations
    #
    # # random return
    # random_r = Random_R(7, all_connections, 120)
    # random_r_results = Base(random_r.all_trajectories, random_r.trajectory_count, all_connections)
    #
    # # random no return
    # random_nr = Random_NR(7, all_connections, 120)
    # random_nr_results = Base(random_nr.all_trajectories, random_nr.trajectory_count, all_connections)
    #
    # # score Score_Optimizer
    # score_optimizer = Score_Optimizer(7, all_connections, 120)
    # score_optimizer_results = Base(score_optimizer.all_trajectories, score_optimizer.trajectory_count, all_connections)
    #
    # # run experiment and calculate score
    # random_r.add_trajectory()
    # random_r_results.calculate_score()
    #
    # random_nr.add_trajectory()
    # random_nr_results.calculate_score()
    #
    # # Greedy algorithm
    # greedy = Greedy(7, all_connections, 120)
    # greedy.add_trajectory()
    # greedy_results = Base(greedy.all_trajectories, greedy.trajectory_count, all_connections)
    #
    # # Calculate the score
    # score = greedy_results.calculate_score()
    #
    # score_optimizer.add_trajectory()
    # score_optimizer_results.calculate_score()
    #
    # # save results to csv
    # random_r_results.to_csv('output/output_r.csv')
    # random_nr_results.to_csv('output/output_nr.csv')
    # score_optimizer_results.to_csv('output/output_so.csv')
    #
    # greedy_results.to_csv('output/output_greedy.csv')
    #
    # # calculate and plot score distribution
    # ScoreDistribution(20000, Random_R, all_connections, 'output/score_distribution_r.png', 'Score Distribution Random Return', 7, all_connections, 120)
    # ScoreDistribution(20000, Random_NR, all_connections, 'output/score_distribution_nr.png', 'Score Distribution Random No Return', 7, all_connections, 120)
    # ScoreDistribution(20000, Score_Optimizer, all_connections, 'output/score_distribution_so.png', 'Score Distribution Optimizer', 7, all_connections, 120)
    # ScoreDistribution(20000, Greedy, all_connections, 'output/score_distribution_greedy.png', 'Score Distribution Greedy', 7, all_connections, 120)
    # # plot the trajectories
    # plotter = TrainNetwork('data/ConnectiesHolland.csv', 'data/StationsHolland.csv')
    # plotter.create_graph()
    # plotter.plot_graph()

    # data for Nederland
    data = LoadData('data/ConnectiesNationaal.csv', 'data/StationsNationaal.csv')
    all_connections = data.connections

    # random return
    random_r = Random_R(20, all_connections, 180)
    random_r_results = Base(random_r.all_trajectories, random_r.trajectory_count, all_connections)

    # random no return
    random_nr = Random_NR(20, all_connections, 180)
    random_nr_results = Base(random_nr.all_trajectories, random_nr.trajectory_count, all_connections)

    # score Score_Optimizer
    score_optimizer = Score_Optimizer(20, all_connections, 180)
    score_optimizer_results = Base(score_optimizer.all_trajectories, score_optimizer.trajectory_count, all_connections)

    # run experiment and calculate score
    random_r.add_trajectory()
    random_r_results.calculate_score()

    random_nr.add_trajectory()
    random_nr_results.calculate_score()

    score_optimizer.add_trajectory()
    score_optimizer_results.calculate_score()

    # Greedy algorithm
    greedy = Greedy(7, all_connections, 120)
    greedy.add_trajectory()
    greedy_results = Base(greedy.all_trajectories, greedy.trajectory_count, all_connections)
    score = greedy_results.calculate_score()

    # save results to csv
    random_r_results.to_csv('output/NL_output_r.csv')
    random_nr_results.to_csv('output/NL_output_nr.csv')
    score_optimizer_results.to_csv('output/output_so.csv')
    greedy_results.to_csv('output/output_greedy.csv')

    # calculate and plot score distribution
    ScoreDistribution(20000, Random_R, all_connections, 'output/NL_score_distribution_r.png', 'Score Distribution Random Return, Netherlands', 20, all_connections, 180)
    ScoreDistribution(20000, Random_NR, all_connections, 'output/NL_score_distribution_nr.png', 'Score Distribution Random No Return, Netherlands', 20, all_connections, 180)
    ScoreDistribution(20000, Score_Optimizer, all_connections, 'output/score_distribution_so.png', 'Score Distribution Optimizer, Netherlands', 20, all_connections, 180)
    ScoreDistribution(20000, Greedy, all_connections, 'output/score_distribution_greedy.png', 'Score Distribution Greedy, Netherlands', 20, all_connections, 180)

    # plot the trajectories
    plotter = TrainNetwork('data/ConnectiesNationaal.csv', 'data/StationsNationaal.csv')
    plotter.create_graph()
    plotter.plot_graph()

if __name__ == "__main__":
    main()
