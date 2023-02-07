import streamlit as st

st.set_page_config(
    page_title='Carlos J. Fuentes: Data Scientist',
    page_icon=':panda_face:',
    layout='wide'
)

st.title('Carlos J. Fuentes: Data Scientist :panda_face:')
st.write('''Hi, I'm Carlos! :wave: In this web app, you'll find a collection of projects I've build using various different programming tools.   
''')
st.write("You can use the side bar to navigate the different pages in this web app. :izakaya_lantern:")
st.write('Hope you enjoy! :smile:')
st.write('---')

# building the sidebar
with st.sidebar:
    st.title('Project Portfolio :briefcase:')
    choice = st.radio('Navigation :world_map:', ['Python', 'Streamlit', 'SQL', 'PowerBI', 'Tableau'])
    st.info("This sidebar allows you to navigate to various portfolio destinations in order to view some of the applications and dashboards I've developed. :100:")

# making the sidebar selections work

if choice=='Python':
    st.subheader('Python Projects :snake:')
    st.write("Click the button below to view a list of **Python** applications I've developed to bring data to life.")
    link = 'https://github.com/cjfuentes-datascience/PYTHON-PROJECTS'
    st.markdown(f'<a href="{link}" target="_blank" style="background-color: #4681f4; padding: 8px 16px; font-size: 16px; color: white; border-radius: 4px;">Github</a>', unsafe_allow_html=True)

if choice=='Streamlit':
    st.subheader('Streamlit Projects :spider_web:')
    st.write("Click the button below to view a list of **Streamlit** applications I've developed to bring data to life.")
    link = 'https://github.com/cjfuentes-datascience/STREAMLIT-PROJECTS'
    st.markdown(f'<a href="{link}" target="_blank" style="background-color: #4681f4; padding: 8px 16px; font-size: 16px; color: white; border-radius: 4px;">Github</a>', unsafe_allow_html=True)

if choice=='SQL':
    st.subheader('SQL Projects :bookmark_tabs:')
    st.write("Click the button below to view a list of **SQL** applications I've developed to bring data to life.")
    link = 'https://github.com/cjfuentes-datascience/SQL-PROJECTS'
    st.markdown(f'<a href="{link}" target="_blank" style="background-color: #4681f4; padding: 8px 16px; font-size: 16px; color: white; border-radius: 4px;">Github</a>', unsafe_allow_html=True)

if choice=='PowerBI':
    st.subheader('PowerBI Projects :chart_with_upwards_trend:')
    st.write("Click the button below to view a list of **PowerBI** applications I've developed to bring data to life.")
    link = 'https://github.com/cjfuentes-datascience/POWER-BI-PROJECTS'
    #st.button('Github', link)
    st.markdown(f'<a href="{link}" target="_blank" style="background-color: #4681f4; padding: 8px 16px; font-size: 16px; color: white; border-radius: 4px;">Github</a>', unsafe_allow_html=True)

if choice=='Tableau':
    st.subheader('Tableau Projects :chart_with_downwards_trend:')
    st.write("Click the button below to view a list of **Tableau** applications I've developed to bring data to life.")
    link = 'https://github.com/cjfuentes-datascience/TABLEAU-PROJECTS'
    st.markdown(f'<a href="{link}" target="_blank" style="background-color: #4681f4; padding: 8px 16px; font-size: 16px; color: white; border-radius: 4px;">Github</a>', unsafe_allow_html=True)




st.write('---')

st.text('Thanks For Stopping By!')
