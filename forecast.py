from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA, ARIMAResults
from sklearn.metrics import mean_squared_error
import preprocessing as pp
from arima import difference, inverse_difference

def predict(hours):
    series = pp.get_data()
    X = series.values
    history = [x for x in X]
    hours_in_week = 168
    validation = pp.get_validate()
    y = validation.values

    model_fit = ARIMAResults.load('model.pkl')

    predictions = list()
    yhat = model_fit.forecast()[0]
    yhat = inverse_difference(history, yhat, hours_in_week)
    predictions.append(yhat)
    history.append(yhat[0])

    for i in range(1, hours):
        diff = difference(history, hours_in_week)

        model = ARIMA(diff, order=(3,1,1))
        model_fit = model.fit(trend='nc', disp=0)
        yhat = model_fit.forecast()[0]
        yhat = inverse_difference(history, yhat, hours_in_week)
        history.append(yhat[0])
        predictions.append(yhat)

    return predictions
