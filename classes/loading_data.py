import pandas as pd

class LoadData():
    def __init__(self, connection_file, station_file):
        self.connections = self.load_connections(connection_file)
        self.stations = self.load_stations(station_file)

    def load_connections(self, file):
        connections = {}
        df = pd.read_csv(file)

        # Iterate through the DataFrame rows
        for index, row in df.iterrows():
            if row[0] not in connections:
                connections[row[0]] = {}
            connections[row[0]][row[1]] = int(float(row[2]))

            if row[1] not in connections:
                connections[row[1]] = {}
            connections[row[1]][row[0]] = int(float(row[2]))

        return connections

    def load_stations(self, file):
        df = pd.read_csv(file)
        stations = {}

        # Iterate through the DataFrame rows
        for index, row in df.iterrows():
            station_id = row[0]
            x = float(row[2])
            y = float(row[1])

            # Add the station to the dictionary
            stations[station_id] = (x, y)

        return stations
