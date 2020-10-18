import warnings
import numpy as np
import pandas as pd
import datetime as dt
import preprocessing as pp
from forecast import predict

warnings.filterwarnings("ignore")
series = pp.get_total()


def mean(dataset):
    average = sum(dataset) / len(dataset)
    return average


def model(date, time):
    aug30 = dt.date(2020, 8, 30)
    delta = date - aug30
    hours = (delta.days - 1) * 24 + time.hour + 1
    history = predict(hours)

    # predictionsdf = pd.DataFrame(predictions)
    # total_data = series.append(predictionsdf)
    average = mean(history)
    target = history[-1]
    percent = 100 * (target / average)

    upper = np.percentile(np.ndarray(history), 65)
    lower = np.percentile(np.ndarray(history), 35)

    if target < lower:
        print("Traffic levels in Atlanta will be low, about %d percent of the average" % percent)
    elif target > upper:
        print("Traffic levels in Atlanta will be high, about %d percent of the average" % percent)
    else:
        print("Traffic levels in Atlanta will be moderate, about %d percent of the average" % percent)


date = dt.date(2020, 8, 31)
time = dt.time(1)
model(date, time)