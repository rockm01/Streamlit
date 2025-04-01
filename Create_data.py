import pandas as pd
import numpy as np

df = {"Yuma":[],
        "Nashua":[],
        "Chicago":[],
        "Denver":[]}

df = pd.DataFrame(df)
df['Yuma'] = np.random.normal(loc = 80, scale = 10.5, size = 31)
df['Nashua'] = np.random.normal(loc = 45, scale = 5.5, size = 31)
df['Chicago'] = np.random.normal(loc = 48, scale = 10, size = 31)
df['Denver'] = np.random.normal(loc = 56, scale = 15, size = 31)
df['Date'] = pd.date_range(start='3/1/2024', end='3/31/2024')
df = df[['Date', 'Yuma', 'Nashua', 'Chicago', 'Denver']]

df.to_csv('data/Weather.csv', index=False)
