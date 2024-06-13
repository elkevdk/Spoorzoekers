from classes.loading_data import LoadData
from output.visualize import TrainNetwork
from algorithms.base import Base
from algorithms.random_R import Random_R
from algorithms.random_NR import Random_NR
from classes.score_distribution import ScoreDistribution
import os

def main():
    data = LoadData('data/ConnectiesHolland.csv', 'data/StationsHolland.csv')
    all_connections = data.connections

    # random return
    random_r = Random_R(7, all_connections, 120)
    random_r_results = Base(random_r.all_trajectories, random_r.trajectory_count, all_connections)

    # random no return
    random_nr = Random_NR(7, all_connections, 120)
    random_nr_results = Base(random_nr.all_trajectories, random_nr.trajectory_count, all_connections)

    # run experiment and calculate score
    random_r.add_trajectory()
    random_r_results.calculate_score()

    random_nr.add_trajectory()
    random_nr_results.calculate_score()

    # create the output folder if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # save results to csv
    random_r_results.to_csv('output/output_r.csv')
    random_nr_results.to_csv('output/output_nr.csv')

    # calculate and plot score distribution
    ScoreDistribution(10000, Random_R, all_connections, 'output/score_distribution_r.png', 'Score Distribution Random Return', 7, all_connections, 120)
    ScoreDistribution(10000, Random_NR, all_connections, 'output/score_distribution_nr.png', 'Score Distribution Random No Return', 7, all_connections, 120)

    # plot the trajectories
    plotter = TrainNetwork('data/ConnectiesHolland.csv', 'data/StationsHolland.csv')
    plotter.create_graph()
    plotter.plot_graph()

if __name__ == "__main__":
    main()
