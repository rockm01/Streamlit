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


#--------------- Beginning of Streamlit App ---------------#
st.title("this is a title")
st.header("Streamlit Tutorial")
st.subheader('subheader')

# Show headers, subheaders, and markdowns
st.markdown("### You can display all kinds of data representations such as...")
st.markdown('#### Basic Dataframe')

# Show a plain dataframe using st.write
st.write(df)


#--------------- Dataframes ---------------#
# Show a dataframe with styling
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
st.divider()


#--------------- Charts ---------------#
st.markdown('### Charts:')
st.markdown('#### Streamlit Supported Charts')
st.markdown('##### Bar Chart:')

st.bar_chart(df, x_label="Columns", y_label="Y Values")

st.markdown('##### Line Graphs')
st.line_chart(df, x='first column', y='second column', color=(255,0,0))

st.markdown('#### Graphs From Other Libraries')
st.markdown('##### Altair Histogram')
data = pd.DataFrame({'values': values})


# Show support for other chart libraries such as Altair
chart = alt.Chart(data).mark_bar().encode(
    alt.X("values:Q", bin=True, title='Value'),
    alt.Y('count()', title='Count'),
)
st.write(chart, use_container_width=True)


#--------------- Maps ---------------#
st.markdown('#### Plot a map')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [42.36, -71.06],
    columns=['lat', 'lon'])
st.map(map_data, color = (255,0,130), size = 10)
#--------------- Widgets ---------------#
st.markdown("### Now let's look at Widgets")

# Show a slider and also introduce containers and columns
st.markdown('#### Sliders')
left_column, middle,  right_column = st.columns(3)

# Declare items shown in left column
with left_column:
    with st.container(border=True):
        x  = st.slider('x', min_value = 1, max_value = 50)
        st.write(f'Create Histogram using numpy random.normal function with size = {x} ')

# Declare items shown in right column
with right_column:
    slide_data = pd.DataFrame({'values': np.random.normal(loc=10, scale=1.5, size=x)})
    chart = alt.Chart(slide_data).mark_bar().encode(
        alt.X("values:Q", bin=True, title='Value'),
        alt.Y('count()', title='Count'),
    ).properties(title='Histogram From Slider')
    st.altair_chart(chart, use_container_width=True)

# Text Box Inputs
st.markdown('#### Text Boxes')
st.markdown('##### String Input')
st.text_input("Your name", key="name")
var = st.session_state.name
if var:
    st.write('Hello', var)

# Date Inputs
st.markdown('##### Date Input')
st.date_input("Date", key="date")
st.write(st.session_state.date)

# Check Boxes
st.markdown('#### Check Boxes')
if st.checkbox('Check This to See Something'):
    st.image('Mountain.jpg')

# Buttons
st.markdown('#### Buttons')
if st.button('Click Me'):
    st.balloons()

# Radio Buttons
st.markdown('#### Radio Buttons')
output = st.radio(
        'Options',
        ("Option 1", "Option 2", "Option 3", "Option 4"))
st.write(f' You Chose: {output}')

