import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from loading_data import LoadData

# Load data
data_loader = LoadData('files/ConnectiesHolland.csv', 'files/StationsHolland.csv')

# Extract connections and stations
connections = data_loader.connections
stations = data_loader.stations

# Create a graph
G = nx.Graph()

# Add nodes with position attributes
for station_id, (x, y) in stations.items():
    G.add_node(station_id, pos=(x, y), name=station_id)

# Add edges with travel time as weights
for station1, neighbors in connections.items():
    for station2, travel_time in neighbors.items():
        G.add_edge(station1, station2, weight=travel_time)

# Get the positions of the nodes
pos = nx.get_node_attributes(G, 'pos')

# Plot the graph
plt.figure(figsize=(12, 8))

# Adjust node label positions
label_pos = {node: (x, y + 0.02) for node, (x, y) in pos.items()}  # Adjust the y-coordinate as needed

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=50, node_color='blue')

# Draw edges
nx.draw_networkx_edges(G, pos)

# Add labels to the adjusted positions
labels = nx.get_node_attributes(G, 'name')  # Retrieve node names
nx.draw_networkx_labels(G, label_pos, labels, font_size=8)

# Show the plot
plt.title("Trainstations and connections in Holland")
plt.xlabel("X-coördinaten")
plt.ylabel("Y-coördinaten")
plt.grid(True)
plt.show()
