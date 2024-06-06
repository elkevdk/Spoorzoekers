import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from loading_data import LoadData

class TrainNetwork:
    def __init__(self, connections_file, stations_file):
        # Load data
        self.data_loader = LoadData(connections_file, stations_file)
        self.connections = self.data_loader.connections
        self.stations = self.data_loader.stations
        self.graph = None

    def create_graph(self):
        # Create a graph
        self.graph = nx.Graph()

        # Add nodes with position attributes
        for station_id, (x, y) in self.stations.items():
            self.graph.add_node(station_id, pos=(x, y), name=station_id)

        # Add edges with travel time as weights
        for station1, neighbors in self.connections.items():
            for station2, travel_time in neighbors.items():
                self.graph.add_edge(station1, station2, weight=travel_time)

    def plot_graph(self, node_size=50, font_size=8, label_offset=0.02):
        if self.graph is None:
            raise ValueError("Graph not created. Call create_graph() first.")

        # Get the positions of the nodes
        pos = nx.get_node_attributes(self.graph, 'pos')

        # Plot the graph
        plt.figure(figsize=(8, 8))

        # Adjust node label positions
        label_pos = {node: (x, y + label_offset) for node, (x, y) in pos.items()}  # Adjust the y-coordinate as needed

        # Draw nodes
        nx.draw_networkx_nodes(self.graph, pos, node_size=node_size, node_color='blue')

        # Draw edges
        nx.draw_networkx_edges(self.graph, pos)

        # Add labels to the adjusted positions
        labels = nx.get_node_attributes(self.graph, 'name')  # Retrieve node names
        nx.draw_networkx_labels(self.graph, label_pos, labels, font_size=font_size)

        # Show the plot
        plt.title("Trainstations and Connections in Holland")
        plt.xlabel("X-coördinaten")
        plt.ylabel("Y-coördinaten")
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    plotter = TrainNetwork('files/ConnectiesHolland.csv', 'files/StationsHolland.csv')
    plotter.create_graph()
    plotter.plot_graph()
