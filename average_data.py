import pandas as pd

east_west = pd.read_csv("east-west.csv", index_col=0, skiprows=1, nrows=24)
west_east = pd.read_csv("west-east.csv", index_col=0, skiprows=1, nrows=24)
north_south = pd.read_csv("north-south.csv", index_col=0, skiprows=1, nrows=24)
south_north = pd.read_csv("south-north.csv", index_col=0, skiprows=1, nrows=24)

all_data = pd.concat([east_west, west_east, north_south, south_north], 1)

average_data = pd.DataFrame(data=[all_data[col].mean(1) for col in east_west.columns], index=east_west.columns)

"""for col in east_west.columns:
    print(col)
    print(all_data[col].mean(1))"""