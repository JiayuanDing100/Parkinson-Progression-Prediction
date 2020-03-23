import numpy as np
import pandas as pd


def read_csv_file(file_path):
   df = pd.read_csv(file_path)
   return df


def patients_selection(df, threshold=6):
    '''return a dataframe containing only the patients with number of visits > threshold'''
    if 'PATNO' in df.columns:
        visits_number_by_pat=df.groupby('PATNO').size().sort_values(ascending=False)
        print("visits_number_by_pat:", visits_number_by_pat)

        mask_sel=visits_number_by_pat>=threshold

        patients_sel=list(mask_sel[mask_sel.values==True].index)
        print("Meet the requirement of number of visit times:", len(patients_sel))  #1003 patients
        df=df.loc[df['PATNO'].isin(patients_sel),:] # return all patients in patients_sel with all columns, loc[row, column]
        df=df.sort_values('PATNO')
        #print("df.loc", df.loc[df['PATNO'].isin(patients_sel),'num_visits'])
        return (patients_sel, df)
    else:
        return 0


