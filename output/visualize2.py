import matplotlib.pyplot as plt
from classes.loading_data import LoadData

class PlotTrains():
    """
    A class to plot train trajectories on a map of stations and connections.

    Parameters
    ----------
    connections_file : str
        The file path to the connections data.
    stations_file : str
        The file path to the stations data.

    Attributes
    ----------
    data_loader : LoadData
        An instance of the LoadData class to load connections and stations data.
    connections : dict
        Dictionary containing all possible connections between stations and their durations.
    stations : dict
        Dictionary containing station names and their coordinates.

    Methods
    -------
    plot_trajectories():
        Plots the train trajectories on a map with stations and connections.
    """
    def __init__(self, connections_file, stations_file):
        self.data_loader = LoadData(connections_file, stations_file)
        self.connections = self.data_loader.connections
        self.stations = self.data_loader.stations

    def plot_trajectories(self, trajectories=None, title='', node_size=50, font_size=8, label_offset=0.02):
        colors = [
            'red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'lime', 'pink',
            'brown', 'gray', 'olive', 'navy', 'teal', 'maroon', 'violet', 'gold', 'coral', 'turquoise'
        ]
        color_cycle = iter(colors)

        # highlight trajectories
        if trajectories:
            # create figure and axis
            plt.figure(figsize=(8, 8))
            ax = plt.gca()

            # draw connections
            for station1, neighbors in self.connections.items():
                for station2, travel_time in neighbors.items():
                    x1, y1 = self.stations[station1]
                    x2, y2 = self.stations[station2]
                    ax.plot([x1, x2], [y1, y2], linestyle=':', color='black', alpha=0.5)

            station_labels = {}
            for i, (station, (x, y)) in enumerate(self.stations.items(), start=1):
                ax.text(x, y, str(i), fontsize=font_size, color='black', fontweight='bold', ha='center', va='bottom')
                station_labels[station] = i

            # plot trajectories one by one
            for trajectory_name, trajectory in list(trajectories.items())[:-1]:
                x_values = []
                y_values = []
                for i, station in enumerate(trajectory):
                    x, y = self.stations[station]
                    x_values.append(x)
                    y_values.append(y)

                ax.plot(x_values, y_values, marker='o', markersize=3, linestyle='-', color=next(color_cycle), alpha=0.8, label=trajectory_name)
                plt.draw()
                plt.pause(1.5)

            # add a separate legend for station names and numbers
            station_legend_labels = [f"{number}: {station}" for station, number in station_labels.items()]
            station_legend = plt.legend(station_legend_labels, title="Stations", loc='upper right', bbox_to_anchor=(1, 0.5), fontsize=font_size)
            ax.add_artist(station_legend)

            ax.set_title(f"Train Network {title}")
            ax.set_xlabel("X-coordinates")
            ax.set_ylabel("Y-coordinates")
            ax.grid(True)

            # final legend
            ax.legend(loc='upper left', title="Trains", bbox_to_anchor=(1, 1))

            plt.tight_layout()
            plt.show()
