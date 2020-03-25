import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from prepare_data import prepare_data
from util_func import timeseries_train_test_split, plotModelResults, plotCoefficients
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate

import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")


def linear_regression(X_train, X_test, y_train, y_test):
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
   # The coefficients
   print('Coefficients: \n', lr.coef_)
   # The mean squared error
   print("Mean squared error: %.2f"
         % mean_squared_error(y_test, y_predict))
   # Explained variance score: 1 is perfect prediction
   print('Variance score: %.2f' % r2_score(y_test, y_predict))
   plt.figure()
   plt.plot(range(len(y_predict)), y_predict, 'b', label="predict")
   plt.plot(range(len(y_predict)), y_test, 'r', label='truth')
   plt.legend(loc='upper right')
   #plt.xlabel('the number of ')
   plt.ylabel('value of PK stage')
   plt.show()


def logistic_regression(X, y, X_train, X_test, y_train, y_test):
   logistic_regression_TS = LogisticRegression(random_state=0, max_iter=1000)
   logistic_regression_TS.fit(X_train, y_train.values.ravel())
   y_pred = logistic_regression_TS.predict(X_test)
   print("Train-Score-logistic_regression: %.4f, Test-Accuracy-logistic_regression: %.4f" % (
   logistic_regression_TS.score(X_train, y_train), logistic_regression_TS.score(X_test, y_test)))
   from sklearn.metrics import confusion_matrix
   confusion_matrix = confusion_matrix(y_test, y_pred)
   print("Logistic Regression:", confusion_matrix)
   target_names = ['1.0', '2.0', '3.0', '4.0', '5.0']
   print("Logistic Regression:", classification_report(y_test, y_pred, target_names=target_names))
   cv_score_lr = cross_val_score(logistic_regression_TS, X, y.values.ravel(), cv=5, n_jobs=-1)
   cross_validate_lr = cross_validate(logistic_regression_TS, X, y.values.ravel(), cv=5, n_jobs=-1, return_train_score=True)
   print('cv score Logistic Regression:{}'.format((cv_score_lr, cv_score_lr.mean())))
   print("Training Accuracy Logistic Regression: %0.2f (+/- %0.2f)" % (cross_validate_lr['train_score'].mean(), cross_validate_lr['train_score'].std() * 2))
   print("Test Accuracy Logistic Regression: %0.2f (+/- %0.2f)" % (cross_validate_lr['test_score'].mean(), cross_validate_lr['test_score'].std() * 2))


def random_forest(X, y, X_train, X_test, y_train, y_test):
   random_forest_TS = RandomForestClassifier(n_estimators=100, random_state=0, n_jobs=-1)
   random_forest_TS.fit(X_train, y_train.values.ravel())
   print("Train-Score-random_forest: %.4f, Test-Accuracy-rfc: %.4f" % (random_forest_TS.score(X_train, y_train), random_forest_TS.score(X_test, y_test)))
   cv_score_rfc = cross_val_score(random_forest_TS, X, y.values.ravel(), cv=5, n_jobs=-1)
   cross_validate_rfc = cross_validate(random_forest_TS, X, y.values.ravel(), cv=5, n_jobs=-1, return_train_score=True)
   print('cv score RF:{}'.format((cv_score_rfc, cv_score_rfc.mean())))
   print("Training Accuracy RF: %0.2f (+/- %0.2f)" % (cross_validate_rfc['train_score'].mean(), cross_validate_rfc['train_score'].std() * 2))
   print("Test Accuracy RF: %0.2f (+/- %0.2f)" % (cross_validate_rfc['test_score'].mean(), cross_validate_rfc['test_score'].std() * 2))


def XGBoost(X, y, X_train, X_test, y_train, y_test):
   xgboost_TS = XGBClassifier(n_jobs=-1, seed=0)
   xgboost_TS.fit(X_train, y_train.values.ravel())
   print("Train-Score-xgboost: %.2f, Test-Accuracy-xgb: %.2f" % (xgboost_TS.score(X_train, y_train),
                                                             xgboost_TS.score(X_test, y_test)))
   cv_score_xgb = cross_val_score(xgboost_TS, X, y.values.ravel(), cv=5, n_jobs=-1)
   cross_validate_xgb = cross_validate(xgboost_TS, X, y.values.ravel(), cv=5, n_jobs=-1, return_train_score=True)
   print('cv score XGB:{}'.format((cv_score_xgb, cv_score_xgb.mean())))
   print("Training Accuracy XGB: %0.2f (+/- %0.2f)" % (cross_validate_xgb['train_score'].mean(), cross_validate_xgb['train_score'].std() * 2))
   print("Test Accuracy XGB: %0.2f (+/- %0.2f)" % (cross_validate_xgb['test_score'].mean(), cross_validate_xgb['test_score'].std() * 2))



if __name__ == '__main__':
   X,y = prepare_data(visit_time_thres=4)
   print("y type(y)", y, type(y))
   print("y.dtypes", y.dtypes)


   X_train, X_test, y_train, y_test = timeseries_train_test_split(X, y, 0.2)

   #logistic_regression(X, y, X_train, X_test, y_train, y_test)
   """
   cv score Logistic Regression:(array([0.64539007, 0.71785714, 0.70967742, 0.76702509, 0.75812274]), 0.7196144932844025)
   Training Accuracy Logistic Regression: 1.00 (+/- 0.00)
   Test Accuracy Logistic Regression: 0.72 (+/- 0.09)
   """
   #random_forest(X, y, X_train, X_test, y_train, y_test)
   """
   cv score RF:(array([0.57446809, 0.79285714, 0.78853047, 0.80645161, 0.79061372]), 0.750584205045625)
   Training Accuracy RF: 1.00 (+/- 0.00)
   Test Accuracy RF: 0.75 (+/- 0.18)
   """
   #XGBoost(X, y, X_train, X_test, y_train, y_test)
   """
   cv score XGB:(array([0.37943262, 0.79285714, 0.78494624, 0.81362007, 0.80144404]), 0.714460023707129)
   Training Accuracy XGB: 0.98 (+/- 0.01)
   Test Accuracy XGB: 0.71 (+/- 0.34)
   """
   linear_regression(X_train, X_test, y_train, y_test)


