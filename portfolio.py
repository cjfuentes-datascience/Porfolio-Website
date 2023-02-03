import streamlit as st
import pandas as pd
import webbrowser

st.title('Carlos J. Fuentes: Data Scientist :panda_face:')
st.write('''Hi, I'm Carlos! :wave: In this web app, you'll find a collection of projects I've build using various different programming tools.   

''')
st.write("Simply follow the instructions below to get a glimpse of what I've built throughout my career. :izakaya_lantern:")
st.write('You can use the side bar to navigate the different pages in this webapp. :world_map:')
st.write('Hope you enjoy! :smile:')
st.write('---')

# building the sidebar
with st.sidebar:
    st.title('Project Portfolio')
    choice = st.radio('Navigation', ['Streamlit', 'Python', 'SQL', 'PowerBI', 'Tableau'])
    st.info("This sidebar allows you to navigate to various portfolio destinations in order to view some of the applications and dashboards I've developed. :100:")

# making the sidebar selections work
if choice=='Streamlit':
    st.subheader('Streamlit Projects :spider_web:')
    st.write("Click the button below to view a list of **Streamlit** applications I've developed to bring data to life.")
    link = 'https://github.com/cjfuentes-datascience/STREAMLIT-PROJECTS'
    if st.button('Github'):
        webbrowser.open_new_tab(link)

if choice=='Python':
    st.subheader('Python Projects :snake:')
    st.write("Click the button below to view a list of **Python** applications I've developed to bring data to life.")
    link = 'https://github.com/cjfuentes-datascience/PYTHON-PROJECTS'
    if st.button('Github'):
        webbrowser.open_new_tab(link)

if choice=='SQL':
    st.subheader('SQL Projects :bookmark_tabs:')
    st.write("Click the button below to view a list of **SQL** applications I've developed to bring data to life.")
    link = 'https://github.com/cjfuentes-datascience/SQL-PROJECTS'
    if st.button('Github'):
        webbrowser.open_new_tab(link)

if choice=='PowerBI':
    st.subheader('PowerBI Projects :chart_with_upwards_trend:')
    st.write("Click the button below to view a list of **PowerBI** applications I've developed to bring data to life.")
    link = 'https://github.com/cjfuentes-datascience/POWER-BI-PROJECTS'
    #st.button('Github', link)
    if st.button('Github'): # this is the only way to make the button work apparently
        webbrowser.open_new_tab(link)



if choice=='Tableau':
    st.subheader('Tableau Projects :chart_with_downwards_trend:')
    st.write("Click the button below to view a list of **Tableau** applications I've developed to bring data to life.")
    link = 'https://github.com/cjfuentes-datascience/TABLEAU-PROJECTS'
    if st.button('Github'):
        webbrowser.open_new_tab(link)

st.write('---')

st.text('Thanks For Stopping By!')
