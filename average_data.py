import numpy as np

east_west = np.genfromtxt("east-west.csv", delimiter=",", filling_values=5, max_rows=26)
west_east = np.genfromtxt("west-east.csv", delimiter=",", filling_values=5, max_rows=26)
north_south = np.genfromtxt("north-south.csv", delimiter=",", filling_values=5, max_rows=26)
south_north = np.genfromtxt("south-north.csv", delimiter=",", filling_values=5, max_rows=26)

average_data = np.zeros(east_west.shape)

average_data = east_west + north_south + south_north + west_east
average_data /= 4