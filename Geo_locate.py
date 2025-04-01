import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from geopy.geocoders import Nominatim

eq_df = pd.read_csv('data/Earthquake.csv')
eq_df_cleaned = eq_df.dropna(subset=['latitude', 'longitude'])
eq_df_cleaned['address'] = ''

geolocator = Nominatim(user_agent="Earthquake_App_unique_4195")

for row in range(len(eq_df_cleaned)):
    coord = (float(eq_df_cleaned.loc[0, 'latitude']), float(eq_df_cleaned.loc[0, 'longitude']))
    location = geolocator.reverse(coord, exactly_one=True)

    if location:
        eq_df_cleaned.loc[0, 'address'] = location.raw.get("address", []).get('country', 'Unknown')
    else:
        eq_df_cleaned.loc[0, 'address'] = 'Unknown'

pd.to_csv('data/Earthquake_cleaned.csv', index=False)
