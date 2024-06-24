from algorithms.random_NR import Random_NR
from algorithms.base import Base
from copy import deepcopy

class Score_Optimizer(Random_NR, Base):

    def select_next_station(self, possible_connections):
        best_score = -float('inf')
        best_connection = None

        # copy the trajectories
        original_trajectories = self.all_trajectories.copy()

        for connection in possible_connections:
            # copy the current trajectory
            current_trajectory = self.connections[:]
            # add the new connection to the current trajectory
            current_trajectory.append(connection)
            #
            self.all_trajectories[f"train_{self.trajectory_count + 1}"] = current_trajectory
    
            # calculate score
            score = self.calculate_intermediate_score()
            # update best score and corresponding connection if the current score is higher
            if score > best_score:
                best_score = score
                best_connection = connection

            # restore the original trajectories
            self.all_trajectories = deepcopy(original_trajectories)

        return best_connection
