import warnings
import numpy as np
import pandas as pd
import datetime as dt
import preprocessing as pp
from forecast import predict

warnings.filterwarnings("ignore")
series = pp.get_total()

def mean(dataset):
    average = dataset.sum() / dataset.size
    return average

def model(date, time):
    aug30 = dt.date(2020, 8, 30)
    delta = date - aug30
    hours = (delta.days - 1) * 24 + time.hour + 1
    predictions = predict(hours)

    predictionsdf = pd.DataFrame(predictions)
    total_data = series.append(predictionsdf)
    average = mean(total_data)
    target = predictions[hours - 1]
    percent = (target / average)

    upper = np.percentile(total_data, 65)
    lower = np.percentile(total_data, 35)

    if target < lower:
        print("Traffic levels in Atlanta will be low, about %.2f times the average" % percent)
    elif target > upper:
        print("Traffic levels in Atlanta will be high, about %.2f times the average" % percent)
    else:
        print("Traffic levels in Atlanta will be moderate, about %.2f times the average" % percent)
