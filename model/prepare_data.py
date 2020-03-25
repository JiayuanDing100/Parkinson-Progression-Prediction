import pandas as pd
from util_func import read_csv_file, patients_selection,\
   patients_selection_by_visit_times, get_samples_by_patient_no,\
   sort_by_VISIT_ID, lagged_dataframe, timeseries_train_test_split,\
   plotModelResults, plotCoefficients

import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")


def get_original_data(file_path, visit_time_thres):
   df = read_csv_file(file_path)
   df.drop(columns=['Unnamed: 0'], inplace=True)
   df.drop(columns=['INFODT_date', 'INFODT', 'EVENT_ID'], inplace=True)
   patients_lst, df_threshold4 = patients_selection(df, threshold=visit_time_thres)
   return (patients_lst, df_threshold4)


def get_one_visit_all_possible_samples(one_visit_all_paients, one_visit_df, lag_predict, lags):
   """
   iterate each patient no and get a dataFrame containing all visits of this patient,
   sort the dataFrame by VISIT_ID
   form input dataset
   """
   data_TS_total = pd.DataFrame()

   for patient_no in one_visit_all_paients:
      data_TS = pd.DataFrame()

      # retrieve data frame with a specific patient no from one_visit_df
      patient_data_TS = get_samples_by_patient_no(one_visit_df, patient_no)
      patient_data_TS.drop(columns=['PATNO'], inplace=True)
      # sort df by visit id in order to form time series data
      sort_patient_data_TS = sort_by_VISIT_ID(patient_data_TS)

      # form time serires data (3 visit times)
      data_TS = lagged_dataframe(sort_patient_data_TS, predict_t=lag_predict ,lags=lags) #[8 rows x 1122 columns]
      # add true label to this df
      data_TS['y'] = sort_patient_data_TS['NHY']
      data_TS_total = pd.concat([data_TS_total, data_TS], axis=0)

   print("data_TS_total:", data_TS_total.shape)
   y = data_TS_total.dropna().y
   X = data_TS_total.dropna().drop(['y'], axis=1)
   return (X, y)  # None value has been removed from returned df


def prepare_data(visit_time_thres):
   """
   1. Choose patients with more than 4 total visit times
   """
   patients_lst, df_threshold4 = get_original_data("../data/selected_features.csv", visit_time_thres)  # totally 522 patients
   print("patients_lst:", len(patients_lst), df_threshold4.shape)

   """
   2. get a dataFrame where patients have specific total visit times
   and get all patient no with specific visit time, organize input 
   samples for each patients. and concatenate pds of all patients. 
   """
   X = pd.DataFrame()
   y = pd.DataFrame()
   for i in range(4, 9):
      patients_visits_lst, df_visits = patients_selection_by_visit_times(df_threshold4, i)
      X_tmp, y_tmp = get_one_visit_all_possible_samples(patients_visits_lst, df_visits, lag_predict=1, lags=3)
      print("X_tmp, y_tmp:", X_tmp.shape, y_tmp.shape)
      X = pd.concat([X, X_tmp], axis=0)
      y = pd.concat([y, y_tmp], axis=0)

   print("X, y:", X.shape, y.shape)
   return (X,y)


