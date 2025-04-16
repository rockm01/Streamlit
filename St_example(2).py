import streamlit as st
import pandas as pd

# Show headers, subheaders, and markdowns
st.image('SL_Logo.png')
st.caption('Matthew Rock')
st.caption('OIM 7502')
st.divider()

#if st.checkbox('Let\'s Begin'):

pill = st.pills(" ", ['What is Streamlit?', 'Why Use Streamlit?', 'How do I start?'])
if pill == 'What is Streamlit?':
    st.markdown('##### Streamlit is a python library that runs python code and displays in a browser window. The user interacts through the browser via prompted inputs. Streamlit makes it easy to create webpage applications to display data with minimal code')
elif pill == 'Why Use Streamlit?':
    st.markdown('##### - Highly Interactive')
    st.markdown('##### - Easy to Use')
    st.markdown('##### - No HTML/CSS/JS Required')
    if st.button('Horray!'):
        st.balloons()

elif pill == 'How do I start?':
    st.markdown('##### Let\'s get started!')
    st.code('pip install streamlit',
            language='python')



