import numpy as np
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
import pandas as pd

dataset = pd.read_csv("../../Data/Purchase Data/Hinjewadi_buy.csv")

rent = dataset.pop("Price")

hinjewadi_purchase = RandomForestRegressor(n_estimators=300, max_depth=10, random_state=10, max_features='log2', min_samples_split=5, min_samples_leaf=1, bootstrap=True)

hinjewadi_purchase.fit(dataset.drop(["Furnishing"],axis = 1),rent)

test = pd.read_csv("../../Data/Rent Data/test.csv")

# print(hinjewadi_purchase.predict(test))

# dataset = pd.read_csv("Hinjewadi_buy.csv")
#
# rent = dataset.pop("Price")
#
# X_train,X_test,y_train, y_test = train_test_split(dataset.drop(["Furnishing"],axis=1),rent,test_size=0.2,random_state=10)
#
# rf_regressor = RandomForestRegressor()
#
# param_dist = {
#     'n_estimators': [int(x) for x in np.linspace(start=300, stop=600, num=10)],
#     'max_features': ['log2','sqrt'],
#     'max_depth': [int(x) for x in np.linspace(5, 50, num=10)],
#     'min_samples_split': [5,6,7],
#     'min_samples_leaf': [1],
#     'bootstrap': [True]
# }
#
# random_search = RandomizedSearchCV(
#     rf_regressor,
#     param_distributions=param_dist,
#     n_iter=100,
#     cv=5,
#     scoring='neg_mean_absolute_error',
#     random_state=42,
#     verbose = 2
# )
#
# random_search.fit(X_train, y_train)
#
# print("Best Parameters: ", random_search.best_params_)
# print("Best Negative Mean Absolute Error: ", random_search.best_score_)
#
# y_pred = random_search.best_estimator_.predict(X_test)
#
# mse = mean_squared_error(y_test, y_pred)
# mae = mean_absolute_error(y_test,y_pred)
# mape = mean_absolute_percentage_error(y_test,y_pred)
# print("Mean Squared Error on Test Set: ", mse)
# print("Mean absolute error:",mae)
# print("MAPE:",mape)