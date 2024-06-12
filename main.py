from classes.loading_data import LoadData
from output.visualize import TrainNetwork
from algorithms.base import Base
from algorithms.random_R import Random_R
from algorithms.random_NR import Random_NR
import os
import matplotlib.pyplot as plt

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

    score_distribution_r = []
    for i in range(10000):
        random_r = Random_R(7, all_connections, 120)
        random_r_results = Base(random_r.all_trajectories, random_r.trajectory_count, all_connections)

        random_r.add_trajectory()
        score_distribution_r.append(random_r_results.calculate_score())

    score_distribution_nr = []
    for i in range(10000):
        random_nr = Random_NR(7, all_connections, 120)
        random_nr_results = Base(random_nr.all_trajectories, random_nr.trajectory_count, all_connections)

        random_nr.add_trajectory()
        score_distribution_nr.append(random_nr_results.calculate_score())

    # function to plot the score distribution as a histogram
    def plot_score(score_distribution, file_name, title):
        plt.figure(figsize=(10, 6))
        plt.hist(score_distribution, bins=20, edgecolor='black')
        plt.title(title)
        plt.xlabel('Score')
        plt.ylabel('Frequency')
        plt.savefig(file_name)

    plot_score(score_distribution_r, 'output/score_distribution_r.png', 'Score Distribution Random Return')
    plot_score(score_distribution_nr, 'output/score_distribution_nr.png', 'Score Distribution Random No Return')

    # plot the trajectories
    plotter = TrainNetwork('data/ConnectiesHolland.csv', 'data/StationsHolland.csv')
    plotter.create_graph()
    plotter.plot_graph()

if __name__ == "__main__":
    main()
