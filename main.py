from loading_data import LoadData
from visualize import TrainNetwork
from experiment_class import Experiment
import os

def main():
    data = LoadData('files/ConnectiesHolland.csv', 'files/StationsHolland.csv')
    all_connections = data.connections
    my_experiment = Experiment(7, all_connections)

    # run experiment and print results
    print(my_experiment.run())

    # create the folder output if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # save results to csv
    my_experiment.to_csv('output/trajectories.csv')

    # plot the trajectories
    plotter = TrainNetwork('files/ConnectiesHolland.csv', 'files/StationsHolland.csv')
    plotter.create_graph()
    plotter.plot_graph()

if __name__ == "__main__":
    main()
