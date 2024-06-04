import pandas as pd

class Station:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def location(self):
        location = [self.x, self.y]


df_stations = pd.read_csv('StationsHolland.csv')
