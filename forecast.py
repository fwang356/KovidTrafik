from statsmodels.tsa.arima_model import ARIMA, ARIMAResults
import preprocessing as pp
from arima import difference, inverse_difference


def predict(hours):
    series = pp.get_total()
    X = series.values.astype('float32')
    history = [x for x in X]
    hours_in_week = 168

    model_fit = ARIMAResults.load('model.pkl')

    predictions = list()

    yhat = model_fit.forecast()[0]
    yhat = inverse_difference(history, yhat, hours_in_week)
    predictions.append(yhat)
    history.append(yhat)

    for i in range(1, hours):
        hours_in_week = 168
        diff = difference(history, hours_in_week)

        model = ARIMA(diff, order=(3, 1, 1))
        model_fit = model.fit(trend='nc', disp=0)
        yhat = model_fit.forecast()[0]
        yhat = inverse_difference(history, yhat, hours_in_week)
        history.append(yhat)
        predictions.append(yhat)

    return history
