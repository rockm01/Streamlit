import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from geopy.geocoders import Nominatim

eq_df = pd.read_csv('data/Earthquake_cleaned.csv')
eq_df['time'] = pd.to_datetime(eq_df['time']).dt.strftime('%m-%d-%Y')
vol_df = pd.read_csv('data/Volcanoes_cleaned.csv')

#Setup the sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Earthquake Data", "Volcano Data"])

if page == "Earthquake Data":
    countries = eq_df['country'].unique().tolist()
    countries.sort()

    st.header("Earthquake Data")
    with st.container(border=True):
        left_column, right_column = st.columns(2)
        with right_column:
            s_all = st.checkbox("Select All")
        with left_column:
            if s_all:
                country_select = st.multiselect("Select Country", countries, default=countries)
            else:
                country_select = st.multiselect("Select Country", countries, default=None
                                            )
        left_column, right_column = st.columns(2)
        with left_column:
            start_date = st.date_input("Start Date", value=pd.to_datetime(eq_df['time']).min())
        with right_column:
            end_date = st.date_input("End Date", value=pd.to_datetime(eq_df['time']).max())

        mag = st.slider("Select Magnitude", min_value=0, max_value=10, value=(0, 10))



    tab1, tab2 = st.tabs(["Map", "Data"])

    map_df = eq_df[(eq_df['country'].isin(country_select)) &
                   ((eq_df['mag'] <= mag[1]) & (eq_df['mag'] >= mag[0])) &
                    ((eq_df['time'] >= start_date.strftime('%m-%d-%Y')) & (eq_df['time'] <= end_date.strftime('%m-%d-%Y')))
                       ][['latitude', 'longitude']]
    display_df = eq_df[(eq_df['country'].isin(country_select)) &
                       ((eq_df['mag'] <= mag[1]) & (eq_df['mag'] >= mag[0])) &
                       ((eq_df['time'] >= start_date.strftime('%m-%d-%Y')) & (eq_df['time'] <= end_date.strftime('%m-%d-%Y')))
                        ][['country', 'mag', 'depth', 'time']]
    tab1.map(map_df)
    tab2.dataframe(display_df, width=600)


if page == "Volcano Data":
    st.header("Volcano Data")

    vol_df['Death_log'] = np.log10(vol_df['Deaths'])

    a_chart = alt.Chart(vol_df).mark_boxplot(color='red').encode(
        x=alt.X('Deaths:Q', scale=alt.Scale(type='log')),
        y=alt.Y("Type:N"),
    ).properties(title='Boxplot of Number of Deaths by Volcano Type since 1990')
    st.altair_chart(a_chart)

    #Create Summary Data
    vol_df_sum = vol_df.groupby('Country').agg('count').sort_values(by='Name')
    vol_df_sum = vol_df_sum.reset_index()

    a_chart_2 = alt.Chart(vol_df_sum).mark_bar(color='steelblue').encode(
        x=alt.X("Country:N").axis(labelAngle=90).sort('-y'),
        y="Name:Q"
    ).properties(title='Ranking of Countries by Number of Volcano Eruptions since 1990')
    st.altair_chart(a_chart_2)