import streamlit as st
import pandas as pd


st.header('Show Dataframe')
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.dataframe(df, width=600)

