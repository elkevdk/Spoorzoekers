# RailNL

This README provides some background information about our implementation of the RailNL case.

# Assignment
Project Assignment: Optimizing Intercity Train Lining System

Goal: Develop a heuristic in Python to generate an optimal train lining system for intercity trains. The goal is to maximize the overall quality of the train lining system based on the given objective function.

The quality K of the train lining system is defined by:
K=p×10000−(T×100+Min)
where:
- p is the fraction of the used connections.
- T is the number of used pathways.
- Min is the total time in minutes of all used pathways.

Conditions:
Each pathway has a maximum time length.
The train lining system has a maximum number of pathways.
Task: Create a heuristic algorithm in Python that maximizes the objective function 𝐾 while adhering to the given conditions.

# Structure
This github contains four folders: algorithms, classes, data and output. Inside the 'data' folder, all csv files are stored.

# Testing
To run the code and test the different algorithms, please open your terminal and take note of the following commands.

'--algorithm' determines what algorithm should be run, with a choice of:

- 'random_r': baseline algorithm, where a train is able to go back to the station that it came from
- 'random_nr': applies a simple heuristic where a train is not able to return to the station it came from unless no other stations are available.
- 'greedy': chooses the shortest connection available at every step where a next station must be selected.
-'hill_climber': randomly removes certain stations from the trajectory and replaces them with different ones.

'--region': determines which region to analyse, either 'Holland' or 'Nederland'

'--runs': (optional) determines the number of runs for the hill climber. Default is set to 1.

'--remove_counts': (optional) determines the number of stations to remove from the trajectory for every step in the hill climber algorithm. 

'--max_trajectories': (optional) determines the maximum number of trajectories, default is 7. Please set them to 22 for region 'Nederland'.

'--max_time': (optional) maximum duration of a trajectory which is set to 120 by default.

Example command line:

"python main.py --algorithm greedy --region Nederland --max_trajectories 20 --max_time 180"

# Authors
- Elke van der Kooij
- Mila Vogels
- Marinne van Willigenburg

# Acknowledgements
We want to thank the minor AI for all the new things we learned. We also want to thank Jacob and Nina for helping us during the progress of this assignment.
