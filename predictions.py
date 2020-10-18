from statsmodels.tsa.arima_model import ARIMAResults
import preprocessing as pp
from arima import inverse_difference

series = pp.get_data()
hours_in_week = 168
model_fit = ARIMAResults.load('model.pkl')
yhat = (model_fit.forecast()[0])
yhat = inverse_difference(series.values, yhat, hours_in_week)
print("Predicted: %d" % yhat)
validate = pp.get_validate()
print(validate[0])