import argparse
from classes.loading_data import LoadData
from classes.score_distribution import ScoreDistribution
from classes.hillclimber_score import HillClimberScore
from algorithms.base import Base
from algorithms.random_R import Random_R
from algorithms.random_NR import Random_NR
from algorithms.greedy import Greedy
from algorithms.hillclimber import HillClimber
from output.visualize import TrainNetwork
from output.visualize2 import PlotTrains
import os

def main():

    # construct command line arguments
    parser = argparse.ArgumentParser(description='Run train network optimization algorithms.')
    parser.add_argument('--algorithm', choices=['random_r', 'random_nr', 'greedy', 'hill_climber'], required=True, help='The algorithm to run.')
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

    # execute specified algorithm and save results
    if args.algorithm == 'random_r':
        random_r = Random_R(args.max_trajectories, all_connections, args.max_time)
        random_r.add_trajectory()
        random_r_results = Base(random_r.all_trajectories, random_r.trajectory_count, all_connections)
        random_r_results.calculate_score()
        random_r_results.to_csv(f'output/{args.region}/output_r.csv')

        # return score distribution
        ScoreDistribution(10000, Random_R, f'output/{args.region}score_distribution_r.png', f'Score Distribution Random Return, {args.region}', args.max_trajectories, all_connections, args.max_time)

    elif args.algorithm == 'random_nr':
        random_nr = Random_NR(args.max_trajectories, all_connections, args.max_time)
        random_nr.add_trajectory()
        random_nr_results = Base(random_nr.all_trajectories, random_nr.trajectory_count, all_connections)
        random_nr_results.calculate_score()
        random_nr_results.to_csv(f'output/{args.region}/output_nr.csv')

        # return score distribution
        ScoreDistribution(10000, Random_NR, f'output/{args.region}score_distribution_nr.png', f'Score Distribution Random No Return, {args.region}', args.max_trajectories, all_connections, args.max_time)

    elif args.algorithm == 'greedy':
        greedy = Greedy(args.max_trajectories, all_connections, args.max_time)
        greedy.add_trajectory()
        greedy_results = Base(greedy.all_trajectories, greedy.trajectory_count, all_connections)
        greedy_results.calculate_score()
        greedy_results.to_csv(f'output/{args.region}/output_greedy.csv')

        # return score distribution
        ScoreDistribution(10000, Greedy, f'output/{args.region}score_distribution_greedy.png', f'Score Distribution Greedy, {args.region}', args.max_trajectories, all_connections, args.max_time)

    elif args.algorithm == 'hill_climber':
        hill_climber = HillClimber(args.max_trajectories, all_connections, args.max_time, 1000, 1)
        hill_climber.run()
        hillclimber_results = Base(hill_climber.all_trajectories, hill_climber.trajectory_count, all_connections)
        hillclimber_results.to_csv(f'output/{args.region}/output_hillclimber_1_1000.csv')

        # return score distribution
        score = HillClimberScore([args.runs], args.remove_counts, all_connections, 10000, args.max_trajectories, args.max_time, args.region)
        score.run_distributions()

if __name__ == "__main__":
    main()
