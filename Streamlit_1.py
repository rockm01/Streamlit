import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

values = np.random.normal(loc=10, scale=1.5, size=100)

st.header("Streamlit Tutorial")

st.header("You can display all kinds of data representations such as...")
st.subheader("Tables: ")

st.subheader('Charts:')
st.write(df)

st.markdown('#### Bar Chart:')
st.bar_chart(df)

st.markdown('#### Line Graphs')
st.line_chart(df,y='second column')

st.markdown('#### Histograms')
plt.hist(values, bins=20)

st.markdown('#### Plot a map')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [42.36, -71.06],
    columns=['lat', 'lon'])
st.map(map_data)

# Widgets
st.header("Now let's look at Widgets")

st.markdown('Sliders')
x = st.slider('x')
st.write(x, 'squared is', x * x)

st.markdown('Text Boxes')
st.text_input("Your name", key="name")
st.session_state.name

st.markdown('Check Boxes')
if st.checkbox('Check This to See Something'):
    st.markdown("Mountain.jpg")