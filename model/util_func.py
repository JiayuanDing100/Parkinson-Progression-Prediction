import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

"""
features = ['PATNO', 'EVENT_ID', 'INFODT', 'INFODT_date', 'NP1COG', 'NP1HALL', 'NP1DPRS', 'NP1ANXS', 'NP1APAT', 'NP1DDS', 'NP2SPCH', 'NP2SALV', 'NP2SWAL', 'NP2EAT', 'NP2DRES', 'NP2HYGN', 'NP2HWRT', 'NP2HOBB', 'NP2TURN', 'NP2TRMR', 'NP2RISE', 'NP2WALK', 'NP2FREZ', 'NP3SPCH', 'NP3FACXP', 'NP3RIGN', 'NP3RIGRU', 'NP3RIGLU', 'PN3RIGRL', 'NP3RIGLL', 'NP3FTAPR', 'NP3FTAPL', 'NP3HMOVR', 'NP3HMOVL', 'NP3PRSPR', 'NP3PRSPL', 'NP3TTAPR', 'NP3TTAPL', 'NP3LGAGR', 'NP3LGAGL', 'NP3RISNG', 'NP3GAIT', 'NP3FRZGT', 'NP3PSTBL', 'NP3POSTR', 'NP3BRADY', 'NP3PTRMR', 'NP3PTRML', 'NP3KTRMR', 'NP3KTRML', 'NP3RTARU', 'NP3RTALU', 'NP3RTARL', 'NP3RTALL', 'NP3RTALJ', 'NP3RTCON', 'DYSKPRES', 'ON_OFF_DOSE', 'PD_MED_USE', 'NP4WDYSK', 'NP4DYSKI', 'NP4OFF', 'NP4FLCTI', 'NP4FLCTX', 'NP4DYSTN', 'NHY', 'MSEADLG', 'PDMEDYN', 'ONLDOPA', 'ONDOPAG', 'ONOTHER', 'FULNUPDR', 'PDSURG', 'PDSURGTP', 'MSRARSP', 'MSLARSP', 'MSRLRSP', 'MSLLRSP', 'COFNRRSP', 'COFNLRSP', 'COHSRRSP', 'COHSLRSP', 'SENRARSP', 'SENLARSP', 'SENRLRSP', 'SENLLRSP', 'RFLRARSP', 'RFLLARSP', 'RFLRLRSP', 'RFLLLRSP', 'PLRRRSP', 'PLRLRSP', 'CN1RSP', 'CN2RSP', 'CN346RSP', 'CN5RSP', 'CN7RSP', 'CN8RSP', 'CN910RSP', 'CN11RSP', 'CN12RSP', 'SYSSUP', 'DIASUP', 'HRSUP', 'SYSSTND', 'DIASTND', 'HRSTND', 'CSFSPNRT', 'SMPDSCRD', 'RBCRSLT', 'WBCRSLT', 'TOPRRSLT', 'TGLCRSLT', 'DFSTROKE', 'DFRSKFCT', 'DFPRESNT', 'DFRPROG', 'DFSTATIC', 'DFHEMPRK', 'DFAGESX', 'DFOTHCRS', 'DFRTREMP', 'DFRTREMA', 'DFPATREM', 'DFOTHTRM', 'DFRIGIDP', 'DFRIGIDA', 'DFAXRIG', 'DFUNIRIG', 'DFTONE', 'DFOTHRIG', 'DFBRADYP', 'DFBRADYA', 'DFAKINES', 'DFBRPLUS', 'DFOTHABR', 'DFPGDIST', 'DFGAIT', 'DFFREEZ', 'DFFALLS', 'DFOTHPG', 'DFPSYCH', 'DFCOGNIT', 'DFDYSTON', 'DFCHOREA', 'DFMYOCLO', 'DFOTHHYP', 'DFHEMTRO', 'DFPSHYPO', 'DFSEXDYS', 'DFURDYS', 'DFBWLDYS', 'DFOCULO', 'DFEYELID', 'DFNEURAB', 'DFRAPSPE', 'DFBULBAR', 'DFATYP', 'PRIMDIAG', 'PSLVL2', 'DIAGNOSIS', 'TESTNAME', 'TESTVALUE', 'ESS1', 'ESS2', 'ESS3', 'ESS4', 'ESS5', 'ESS6', 'ESS7', 'ESS8', 'LNS_TOTRAW', 'AGE_ASSESS_LNS', 'DVS_LNS', 'DRMVIVID', 'DRMAGRAC', 'DRMNOCTB', 'SLPLMBMV', 'SLPINJUR', 'DRMVERBL', 'DRMFIGHT', 'DRMUMV', 'DRMOBJFL', 'MVAWAKEN', 'DRMREMEM', 'SLPDSTRB', 'STROKE', 'HETRA', 'PARKISM', 'RLS', 'NARCLPSY', 'DEPRS', 'EPILEPSY', 'BRNINFM', 'SCAU1', 'SCAU2', 'SCAU3', 'SCAU4', 'SCAU5', 'SCAU6', 'SCAU7', 'SCAU8', 'SCAU9', 'SCAU10', 'SCAU11', 'SCAU12', 'SCAU13', 'SCAU14', 'SCAU15', 'SCAU16', 'SCAU17', 'SCAU18', 'SCAU19', 'SCAU20', 'SCAU21', 'SCAU26B', 'SCAU26C', 'SCAU26D', 'COGDECLN', 'FNCDTCOG', 'COGSTATE', 'COGDXCL', 'RVWNPSY', 'HVLTRT1', 'HVLTRT2', 'HVLTRT3', 'HVLTRDLY', 'HVLTREC', 'HVLTFPRL', 'HVLTFPUN', 'HVLTVRSN', 'DVT_TOTAL_RECALL', 'DVT_DELAYED_RECALL', 'DVT_RETENTION', 'DVT_RECOG_DISC_INDEX', 'MCAALTTM', 'MCACUBE', 'MCACLCKC', 'MCACLCKN', 'MCACLCKH', 'MCALION', 'MCARHINO', 'MCACAMEL', 'MCAFDS', 'MCABDS', 'MCAVIGIL', 'MCASER7', 'MCASNTNC', 'MCAVFNUM', 'MCAVF', 'MCAABSTR', 'MCAREC1', 'MCAREC2', 'MCAREC3', 'MCAREC4', 'MCAREC5', 'MCATOT', 'GDSSATIS', 'GDSDROPD', 'GDSEMPTY', 'GDSBORED', 'GDSGSPIR', 'GDSAFRAD', 'GDSHAPPY', 'GDSHLPLS', 'GDSHOME', 'GDSMEMRY', 'GDSALIVE', 'GDSWRTLS', 'GDSENRGY', 'GDSHOPLS', 'GDSBETER', 'SDMTOTAL', 'SDMTVRSN', 'DVSD_SDM', 'DVT_SDM', 'STAIAD1', 'STAIAD2', 'STAIAD3', 'STAIAD4', 'STAIAD5', 'STAIAD6', 'STAIAD7', 'STAIAD8', 'STAIAD9', 'STAIAD10', 'STAIAD11', 'STAIAD12', 'STAIAD13', 'STAIAD14', 'STAIAD15', 'STAIAD16', 'STAIAD17', 'STAIAD18', 'STAIAD19', 'STAIAD20', 'STAIAD21', 'STAIAD22', 'STAIAD23', 'STAIAD24', 'STAIAD25', 'STAIAD26', 'STAIAD27', 'STAIAD28', 'STAIAD29', 'STAIAD30', 'STAIAD31', 'STAIAD32', 'STAIAD33', 'STAIAD34', 'STAIAD35', 'STAIAD36', 'STAIAD37', 'STAIAD38', 'STAIAD39', 'STAIAD40', 'JLO_TOTRAW', 'JLO_TOTCALC', 'AGE_ASSESS_JLO', 'DVS_JLO_MSSA', 'DVS_JLO_MSSAE', 'PTINBOTH', 'TMGAMBLE', 'CNTRLGMB', 'TMSEX', 'CNTRLSEX', 'TMBUY', 'CNTRLBUY', 'TMEAT', 'CNTRLEAT', 'TMTORACT', 'TMTMTACT', 'TMTRWD', 'BIRTHDT', 'GENDER', 'P3GRP', 'CURRENT_APPRDX', 'APPRDX', 'MHROW_1', 'MHROW_2', 'MHROW_3', 'MHROW_4', 'MHROW_5', 'MHROW_6', 'MHROW_7', 'MHROW_8', 'MHROW_9', 'MHROW_10', 'MHROW_11', 'MHROW_12', 'MHROW_13', 'ABNORM', 'PESEQ_1', 'PESEQ_2', 'PESEQ_3', 'PESEQ_4', 'PESEQ_5', 'PESEQ_6', 'PESEQ_7', 'PESEQ_8', 'PESEQ_9', 'PESEQ_10', 'PESEQ_11', 'PESEQ_12', 'PESEQ_13', 'DXTREMOR', 'DXRIGID', 'DXBRADY', 'DXPOSINS', 'DXOTHSX', 'DOMSIDE', 'num_visits', 'VISIT_ID', 'visitsdiff_days', 'lastDate_diff_days', 'PDDXDT_diff_days', 'PDMEDT_diff_days', 'PDSURGDT_diff_days']
"""

def read_csv_file(file_path):
   df = pd.read_csv(file_path)
   return df


def get_samples_by_patient_no(df, patient_no):
    """
    input: a dataframe and specific patient number
    return: a dataframe containing all samples of this patient number
    """
    df_cp = pd.DataFrame(df.copy())
    df_resp = df_cp[df_cp["PATNO"] == patient_no]
    return df_resp

def sort_by_VISIT_ID(df):
    """
    :param df: a dataframe with all visits of one patients
    :return: a dataframe sorting by VISIT_ID (1, 2, 3, 4,...)
    """
    df_cp = pd.DataFrame(df.copy())
    df_cp.set_index("VISIT_ID", drop=False, inplace=True)
    print(df_cp)  # 374 features
    # print(df_patient_no.sort_index(axis=0))
    print(df_cp.sort_index(axis=0))
    return df_cp.sort_index(axis=0)

def patients_selection_by_visit_times(df, visit_times):
    '''return a dataframe containing only the patients with number of visits == visit_times'''
    if 'PATNO' in df.columns:
        visits_number_by_pat = df.groupby('PATNO').size().sort_values(ascending=False)
        #print("(patients_selection_by_visit_times) visits_number_by_pat:", visits_number_by_pat)
        mask_sel = visits_number_by_pat == visit_times
        patients_sel = list(mask_sel[mask_sel.values == True].index)
        #print("Meet the requirement of number of visit times:", len(patients_sel))
        df = df.loc[df['PATNO'].isin(patients_sel), :]
        df = df.sort_values('PATNO')
        return (patients_sel, df)
    else:
        return 0

def patients_selection(df, threshold=6):
    '''return a dataframe containing only the patients with number of visits >= threshold'''
    if 'PATNO' in df.columns:
        visits_number_by_pat=df.groupby('PATNO').size().sort_values(ascending=False)
        print("visits_number_by_pat:", visits_number_by_pat)
        mask_sel=visits_number_by_pat>=threshold
        patients_sel=list(mask_sel[mask_sel.values==True].index)
        print("Meet the requirement of number of visit times:", len(patients_sel),patients_sel)
        df=df.loc[df['PATNO'].isin(patients_sel),:] # return all patients in patients_sel with all columns, loc[row, column]
        df=df.sort_values('PATNO')
        #print("df.loc", df.loc[df['PATNO'].isin(patients_sel),'num_visits'])
        return (patients_sel, df)
    else:
        return 0

def lag(df, n):
   new_columns = ["{}_Lag{:02d}".format(variable, n) for variable in df.columns]
   new_df = df.shift(n)
   new_df.columns = new_columns
   return new_df

def lagged_dataframe(df, predict_t=1 ,lags=3):  # lags : means input time period, by default, 3 visit times, predict_t =1, predict next visit
   data_frames = []
   data_frames.extend([lag(df, i) for i in range(predict_t, lags + predict_t)])
   return pd.concat(data_frames, axis=1)

def timeseries_train_test_split(X, y, test_size):
   """
       Perform train-test split with respect to time series structure
   """
   # get the index after which test set starts
   test_index = int(len(X) * (1 - test_size))

   X_train = X.iloc[:test_index]
   print("X_train in spliting data:", X_train)
   y_train = y.iloc[:test_index]
   X_test = X.iloc[test_index:]
   y_test = y.iloc[test_index:]
   print("all shapes:", X.shape, X_train.shape, y_train.shape, X_test.shape, y_test.shape)  #(14374, 22) (10061, 22) (4313, 22)
   return X_train, X_test, y_train, y_test

def mean_absolute_percentage_error(y_true, y_pred):
   return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def plotModelResults(model, X_train, X_test, y_train, y_test, plot_intervals=False, plot_anomalies=False):
   """
       Plots modelled vs fact values, prediction intervals and anomalies
   """
   prediction = model.predict(X_test)

   plt.figure(figsize=(15, 7))
   plt.plot(prediction, "g", label="prediction", linewidth=2.0)
   plt.plot(y_test.values, label="actual", linewidth=2.0)

   if plot_intervals:
      cv = cross_val_score(model, X_train, y_train,
                           cv=5,
                           scoring="neg_mean_absolute_error")
      mae = cv.mean() * (-1)
      deviation = cv.std()

      scale = 20
      lower = prediction - (mae + scale * deviation)
      upper = prediction + (mae + scale * deviation)

      plt.plot(lower, "r--", label="upper bond / lower bond", alpha=0.5)
      plt.plot(upper, "r--", alpha=0.5)

      if plot_anomalies:
         anomalies = np.array([np.NaN] * len(y_test))
         anomalies[y_test < lower] = y_test[y_test < lower]
         anomalies[y_test > upper] = y_test[y_test > upper]
         plt.plot(anomalies, "o", markersize=10, label="Anomalies")

   error = mean_absolute_percentage_error(prediction, y_test)
   plt.title("Mean absolute percentage error {0:.2f}%".format(error))
   plt.legend(loc="best")
   plt.tight_layout()
   plt.grid(True);
   plt.savefig("linear.png")

def plotCoefficients(model, X_train):
   """
       Plots sorted coefficient values of the model
   """
   coefs = pd.DataFrame(model.coef_, X_train.columns)
   coefs.columns = ["coef"]
   coefs["abs"] = coefs.coef.apply(np.abs)
   coefs = coefs.sort_values(by="abs", ascending=False).drop(["abs"], axis=1)

   plt.figure(figsize=(15, 9))
   coefs.coef.plot(kind='bar')
   plt.grid(True, axis='y')
   plt.hlines(y=0, xmin=0, xmax=len(coefs), linestyles='dashed')
   plt.savefig("linear-cov.png")
