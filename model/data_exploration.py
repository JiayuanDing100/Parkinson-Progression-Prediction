import pandas as pd
from util_func import read_csv_file

file_path='../data/selected_features.csv'
df = read_csv_file(file_path)
print("df shape:", df.shape)  # (4784, 379)
df_patient_no = df.groupby('PATNO').agg('median')  # (1674, 375)
print("df_patient_no:", df_patient_no.shape)

print("statistics of visit times:", df['num_visits'].value_counts())
"""
total_times, sampels, patients
6    852 142
7    714 102
1    671 671
2    586 293
3    564 188
5    525 105
4    512 128
8    360 45
"""