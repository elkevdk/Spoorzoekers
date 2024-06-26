import argparse
from classes.loading_data import LoadData
from classes.score_distribution import ScoreDistribution
from classes.hillclimber_score import HillClimberScore
from algorithms.base import Base
from algorithms.random_R import Random_R
from algorithms.random_NR import Random_NR
from algorithms.best_score import Score_Optimizer
from algorithms.greedy import Greedy
from algorithms.hillclimber import HillClimber
from output.visualize import TrainNetwork
from output.visualize2 import PlotTrains
import os

def main():

    # construct command line arguments
    parser = argparse.ArgumentParser(description='Run train network optimization algorithms.')
    parser.add_argument('--algorithm', choices=['random_r', 'random_nr', 'score_optimizer', 'greedy', 'hill_climber', 'score_distribution'], required=True, help='The algorithm to run.')
    parser.add_argument('--region', choices=['Holland', 'Nederland'], required=True, help='The region to run the algorithm on.')
    parser.add_argument('--runs', type=int, default=1, help='Number of runs for the hill climber and score distribution algorithms.')
    parser.add_argument('--remove_counts', type=int, nargs='+', default=[1, 2, 3, 4], help='Number of removals for the hill climber score distribution.')
    parser.add_argument('--max_trajectories', type=int, default=7, help='Max number of trajectories.')
    parser.add_argument('--max_time', type=int, default=120, help='Max time for a trajectory.')

    args = parser.parse_args()

    # create the output folder if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # load data based on region
    if args.region == 'Holland':
        data = LoadData('data/ConnectiesHolland.csv', 'data/StationsHolland.csv')
    else:
        data = LoadData('data/ConnectiesNationaal.csv', 'data/StationsNationaal.csv')

    all_connections = data.connections
    all_stations = data.stations

    if args.algorithm == 'random_r':
        random_r = Random_R(args.max_trajectories, all_connections, args.max_time)
        random_r.add_trajectory()
        random_r_results = Base(random_r.all_trajectories, random_r.trajectory_count, all_connections)
        random_r_results.calculate_score()
        random_r_results.to_csv(f'output/{args.region}/output_r.csv')

    elif args.algorithm == 'random_nr':
        random_nr = Random_NR(args.max_trajectories, all_connections, args.max_time)
        random_nr.add_trajectory()
        random_nr_results = Base(random_nr.all_trajectories, random_nr.trajectory_count, all_connections)
        random_nr_results.calculate_score()
        random_nr_results.to_csv(f'output/{args.region}/output_nr.csv')

    elif args.algorithm == 'score_optimizer':
        score_optimizer = Score_Optimizer(args.max_trajectories, all_connections, args.max_time)
        score_optimizer.add_trajectory()
        score_optimizer_results = Base(score_optimizer.all_trajectories, score_optimizer.trajectory_count, all_connections)
        score_optimizer_results.calculate_score()
        score_optimizer_results.to_csv(f'output/{args.region}/output_so.csv')

    elif args.algorithm == 'greedy':
        greedy = Greedy(args.max_trajectories, all_connections, args.max_time)
        greedy.add_trajectory()
        greedy_results = Base(greedy.all_trajectories, greedy.trajectory_count, all_connections)
        greedy_results.calculate_score()
        greedy_results.to_csv(f'output/{args.region}/output_greedy.csv')

    elif args.algorithm == 'hill_climber':
        hill_climber = HillClimber(args.max_trajectories, all_connections, args.max_time)
        final_trajectories, final_score = hill_climber.run()
        hill_climber_results = Base(final_trajectories, hill_climber.trajectory_count, all_connections)
        hill_climber_results.to_csv(f'output/{args.region}/output_hill_climber.csv')

    elif args.algorithm == 'score_distribution':
        score = HillClimberScore([args.runs], args.remove_counts, all_connections, 100, args.max_trajectories, args.max_time)
        score.run_distributions()

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

    # Calculate and plot score distribution
    # amount_runs = [500, 1000]
    # remove_counts = [1, 2, 3, 4]
    # score = HillClimberScore(amount_runs, remove_counts, all_connections, 100, 7, 120)
    # score.run_distributions()

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
