from algorithms.random_NR import Random_NR
from algorithms.base import Base

class Score_Optimizer(Random_NR):

    def select_next_station(self, possible_connections):
        possible_connections_scores = []

        for connection in possible_connections:
            current_trajectory = self.connections[:]
            current_trajectory.append(connection)
            score = self.calculate_p_for_trajectory(current_trajectory)
            print(score)
            possible_connections_scores.append(score)

        best_connection_index = possible_connections_scores.index(max(possible_connections_scores))
        print(max(possible_connections))
        return possible_connections[best_connection_index]
