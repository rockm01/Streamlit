import pandas as pd

vol_df = pd.read_csv('data/Volcanoes_cleaned.csv')
list = ['Year', 'Mo', 'Dy']
for i in list:
    vol_df[i] = vol_df[i].fillna(1)
    vol_df[i] = vol_df[i].astype(int)
    vol_df[i] = vol_df[i].astype(str)

vol_df['date'] = vol_df['Year'].astype(str) + '-' + vol_df['Mo'].astype(str) + '-' + vol_df['Dy'].astype(str)
vol_df['date'] = pd.to_datetime(vol_df['date']).dt.strftime('%m-%d-%Y')

print(vol_df.head())
vol_df.to_csv('data/Volcanoes_cleaned.csv', index=False)