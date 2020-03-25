import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from prepare_data import prepare_data
from util_func import timeseries_train_test_split, plotModelResults, plotCoefficients


import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

X,y = prepare_data(visit_time_thres=4)

X_train, X_test, y_train, y_test = timeseries_train_test_split(X, y, 0.2)


logreg_TS = LogisticRegression(multi_class='multinomial',solver='newton-cg',random_state=0,max_iter=500)
logreg_TS.fit(X_train, y_train.values.ravel())

#### Random Forest
rfc_TS = RandomForestClassifier(n_estimators=100, random_state=0,n_jobs=-1)
rfc_TS.fit(X_train, y_train.values.ravel())

#### XGBoost
from xgboost import XGBClassifier
xgb_TS = XGBClassifier(n_jobs=-1,seed=0)
xgb_TS.fit(X_train, y_train.values.ravel())


print("Train-Score-logreg: %.4f, Test-Accuracy-logreg: %.4f" % (logreg_TS.score(X_train, y_train), logreg_TS.score(X_test, y_test)))
print("Train-Score-rfc: %.4f, Test-Accuracy-rfc: %.4f" % (rfc_TS.score(X_train, y_train), rfc_TS.score(X_test, y_test)))
print("Train-Score-xgb: %.2f, Test-Accuracy-xgb: %.2f" % (xgb_TS.score(X_train, y_train),
                                                          xgb_TS.score(X_test, y_test)))
"""
# linear regression
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # transform your data such that its distribution will have a mean value 0 and standard deviation of 1.
X_test_scaled = scaler.transform(X_test)

lr = LinearRegression()
lr.fit(X_train_scaled, y_train)
y_predict = lr.predict(X_test_scaled)

print("y_test:", y_test)
print("y_predict:", y_predict)

#plotModelResults(lr, X_train=X_train_scaled, X_test=X_test_scaled, y_train=y_train, y_test=y_test,
#                    plot_intervals=True, plot_anomalies=False)
#plotCoefficients(lr, X_train=X_train)

"""
