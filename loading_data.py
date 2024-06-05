import pandas as pd

class LoadData:
    def __init__(self, connection_file, station_file):
        self.connections, self.connection_total, self.startstation = self.load_connections(connection_file)
        self.stations = self.load_stations(station_file)

    def load_connections(self, file):
        connections = {}
        startstation = []

        df = pd.read_csv(file)

        # Iterate through the DataFrame rows
        for index, row in df.iterrows():
            if row[0] not in connections:
                connections[row[0]] = {}
            connections[row[0]][row[1]] = int(float(row[2]))

            if row[1] not in connections:
                connections[row[1]] = {}
            connections[row[1]][row[0]] = int(float(row[2]))

        # Calculate the total number of connections
        connection_total = len(df)

        # Identify start stations
        for key, value in connections.items():
            if len(value) == 1:
                startstation.append(key)

        return connections, connection_total, startstation

    def load_stations(self, file):
        df = pd.read_csv(file)

        # Create a dictionary of stations
        stations = {row[0]: (float(row[2]), float(row[1])) for index, row in df.iterrows()}

        return stations
