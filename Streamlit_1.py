import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

# Setup dataframes and other objects to use later
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

w_df = pd.read_csv('data/Weather.csv')
values = np.random.normal(loc=10, scale=1.5, size=100)

# Beginning of Streamlit App
st.header("Streamlit Tutorial")

st.markdown("### You can display all kinds of data representations such as...")
st.markdown('#### Basic Dataframe')
st.write(df)

st.markdown("#### Dataframe with some custom styling")

def temp_color(val):
    if val < 35:
        color = 'lightblue'
    elif val < 55:
        color = 'palegreen'
    elif val < 75:
        color = 'lightyellow'
    elif val < 95:
        color = 'moccasin'
    else:
        color = 'pink'
    return f'background-color: {color}'

def make_pretty(styler):
    styler.set_caption('Weather Data')
    styler.format({'Date': lambda t: t.strftime('%b %d, %Y')})
    styler.format({'Yuma': '{:.1f}', 'Nashua': '{:.1f}', 'Chicago': '{:.1f}', 'Denver': '{:.1f}'})
    styler.applymap(temp_color, subset=['Yuma', 'Nashua', 'Chicago', 'Denver'])
    return styler

st.dataframe(w_df.style.pipe(make_pretty), width=600)

st.markdown('### Charts:')

st.markdown('#### Streamlit Supported Charts')
st.markdown('##### Bar Chart:')
st.bar_chart(df, x_label="X Values")

st.markdown('##### Line Graphs')
st.line_chart(df, x='first column', y='second column', color='#ffaa00')

st.markdown('#### Graphs From Other Libraries')
st.markdown('##### Altair Histogram')
data = pd.DataFrame({'values': values})
chart = alt.Chart(data).mark_bar().encode(
    alt.X("values:Q", bin=True, title='Value'),
    alt.Y('count()', title='Count'),
)
st.altair_chart(chart, use_container_width=True)


st.markdown('#### Plot a map')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [42.36, -71.06],
    columns=['lat', 'lon'])
st.map(map_data, color = (255,0,0))


# Widgets
st.markdown("### Now let's look at Widgets")

st.markdown('#### Sliders')
left_column, right_column = st.columns(2)
with left_column:
    with st.container(border=True):
        x = st.slider('x')
        st.write(f'Create Histogram using numpy random.normal function with size = {x} ')

with right_column:
    slide_data = pd.DataFrame({'values': np.random.normal(loc=10, scale=1.5, size=x)})
    chart = alt.Chart(slide_data).mark_bar().encode(
        alt.X("values:Q", bin=True, title='Value'),
        alt.Y('count()', title='Count'),
    ).properties(title='Histogram From Slider')
    st.altair_chart(chart, use_container_width=True)

st.markdown('#### Text Boxes')
st.markdown('##### String Input')
st.text_input("Your name", key="name")
var = st.session_state.name
if var:
    st.write('Hello', var)
st.markdown('##### Date Input')
st.date_input("Date", key="date")
st.write(st.session_state.date)

st.markdown('#### Check Boxes')
if st.checkbox('Check This to See Something'):
    st.image('Mountain.jpg')

st.markdown('#### Buttons')
if st.button('Click Me'):
    st.balloons()

st.markdown('#### Radio Buttons')
output = st.radio(
        'Options',
        ("Option 1", "Option 2", "Option 3", "Option 4"))
st.write(f' You Chose: {output}')

