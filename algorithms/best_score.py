from algorithms.random_R import Random_R
from algorithms.base import Base

class Score_Optimizer(Random_R):

    def select_next_station(self, possible_connections):
        possible_connections_scores = []

        for connection in possible_connections:
            current_trajectory = self.connections[:]
            print("cj", current_trajectory)
            current_trajectory.append(connection)
            print("possible_connections", possible_connections)
            print("connection", connection)
            score = self.calculate_score_for_trajectory(current_trajectory)
            print("score", score)
            possible_connections_scores.append(score)

        best_connection_index = possible_connections_scores.index(max(possible_connections_scores))
        return possible_connections[best_connection_index]
