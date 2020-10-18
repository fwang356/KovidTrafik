import pandas as pd
from datetime import datetime

def get_data():
    east_west = pd.read_csv("east-west.csv", index_col=0, skiprows=1, nrows=24)
    west_east = pd.read_csv("west-east.csv", index_col=0, skiprows=1, nrows=24)
    north_south = pd.read_csv("north-south.csv", index_col=0, skiprows=1, nrows=24)
    south_north = pd.read_csv("south_north.csv", index_col=0, skiprows=1, nrows=24)

    all_data = pd.concat([east_west, west_east, north_south, south_north], 1)

    average_data = pd.DataFrame(data=[all_data[col].mean(1) for col in east_west.columns], index=east_west.columns).stack()

    average_data.index = [datetime.strptime(" ".join(i).strip(), "%m/%d/%Y %H:%M:%S") for i in average_data.index]

    training_data = average_data['01/01/2020 00:00:00':'08/01/2020 00:00:00']

    return training_data

def get_validate():
    east_west = pd.read_csv("east-west.csv", index_col=0, skiprows=1, nrows=24)
    west_east = pd.read_csv("west-east.csv", index_col=0, skiprows=1, nrows=24)
    north_south = pd.read_csv("north-south.csv", index_col=0, skiprows=1, nrows=24)
    south_north = pd.read_csv("south_north.csv", index_col=0, skiprows=1, nrows=24)

    all_data = pd.concat([east_west, west_east, north_south, south_north], 1)

    average_data = pd.DataFrame(data=[all_data[col].mean(1) for col in east_west.columns],
                                index=east_west.columns).stack()

    average_data.index = [datetime.strptime(" ".join(i).strip(), "%m/%d/%Y %H:%M:%S") for i in average_data.index]

    validate_data = average_data['08/01/2020 00:00:00':]

    return validate_data

def get_total():
    east_west = pd.read_csv("east-west.csv", index_col=0, skiprows=1, nrows=24)
    west_east = pd.read_csv("west-east.csv", index_col=0, skiprows=1, nrows=24)
    north_south = pd.read_csv("north-south.csv", index_col=0, skiprows=1, nrows=24)
    south_north = pd.read_csv("south_north.csv", index_col=0, skiprows=1, nrows=24)

    all_data = pd.concat([east_west, west_east, north_south, south_north], 1)

    average_data = pd.DataFrame(data=[all_data[col].mean(1) for col in east_west.columns],
                                index=east_west.columns).stack()

    average_data.index = [datetime.strptime(" ".join(i).strip(), "%m/%d/%Y %H:%M:%S") for i in average_data.index]

    return average_data
