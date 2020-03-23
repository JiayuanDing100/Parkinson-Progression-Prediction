import pandas as pd
from util_func import read_csv_file

file_path='../data/selected_features.csv'
df = read_csv_file(file_path)
print(df.shape)



