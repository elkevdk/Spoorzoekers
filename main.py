from loading_data import LoadData
from visualize import TrainNetwork
from experiment_class import Experiment

def main():
    data = LoadData('files/ConnectiesHolland.csv', 'files/StationsHolland.csv')
    all_connections = data.connections
    my_experiment = Experiment(7, all_connections)
    print(my_experiment.run())
    plotter = TrainNetwork('files/ConnectiesHolland.csv', 'files/StationsHolland.csv')
    plotter.create_graph()
    plotter.plot_graph()

if __name__ == "__main__":
    main()
