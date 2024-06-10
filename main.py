from loading_data import LoadData
from visualize import TrainNetwork
from base import Random
import os

def main():
    data = LoadData('files/ConnectiesHolland.csv', 'files/StationsHolland.csv')
    all_connections = data.connections
    random = Random(7, all_connections, 120)

    # run experiment and calculate score
    random.add_trajectory()
    random.calculate_score()

    # create the output folder if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # save results to csv
    random.to_csv('output/ouput.csv')

    # plot the trajectories
    plotter = TrainNetwork('files/ConnectiesHolland.csv', 'files/StationsHolland.csv')
    plotter.create_graph()
    plotter.plot_graph()

if __name__ == "__main__":
    main()
