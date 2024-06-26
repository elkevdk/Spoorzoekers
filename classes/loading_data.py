import pandas as pd

class LoadData():
    """
    Loads and manages data bout connections and stations from CSV files.
    Reads data about the distances between stations and the coordinates of each
    station which are the connection ddata and station data, respectively, stored
    in dictionary structures.

    Attributes:
    connections (dict): cotains stations as keys and dictionaries of the connections
                        between stations as values.
    stations (dict): contains station IDs for keys and tuples of coordinates (x,y)
                     as values.

    Methods:
    __init__(connection_file, station_file):
        Initializes the LoadData class by loading connection and station data from the provided files.
    load_connections(file):
        Loads connection data from a CSV file into a dictionary.
    load_stations(file):
        Loads station data from a CSV file into a dictionary.
    """
    def __init__(self, connection_file, station_file):
        self.connections = self.load_connections(connection_file)
        self.stations = self.load_stations(station_file)

    def load_connections(self, file):
        connections = {}
        df = pd.read_csv(file)

        # loop over DataFrame rows
        for index, row in df.iterrows():
            # ensure station1 is a key in connections
            if row[0] not in connections:
                connections[row[0]] = {}
            # add station2 and the distance to station1's connections
            connections[row[0]][row[1]] = int(float(row[2]))

            # ensure station2 is a key in connections
            if row[1] not in connections:
                connections[row[1]] = {}
            # add station1 and the distance to station2's connections
            connections[row[1]][row[0]] = int(float(row[2]))

        return connections

    def load_stations(self, file):
        df = pd.read_csv(file)
        stations = {}

        # loop over the DataFrame rows
        for index, row in df.iterrows():
            station_id = row[0]
            x = float(row[2])
            y = float(row[1])

            # add the station to the dictionary
            stations[station_id] = (x, y)

        return stations
