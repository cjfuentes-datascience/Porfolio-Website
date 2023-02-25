import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title='Carlos J. Fuentes: Data Scientist',
    page_icon=':panda_face:',
    layout='wide'
)

# main page of the website
st.title('Carlos J. Fuentes: Data Scientist :panda_face:')
st.write('''Hi, I'm Carlos! :wave: In this web app, you'll find a collection of projects I've build using various different programming tools.   
''')
st.write("You can use the side bar to navigate the different pages in this web app. :izakaya_lantern:")
st.write('Hope you enjoy! :smile:')
st.write('---')

# building the sidebar
with st.sidebar:
    st.title('Project Portfolio :briefcase:')
    choice = st.radio('Navigation :world_map:', ['Streamlit', 'Python', 'SQL', 'PowerBI', 'Tableau'])
    st.info("This sidebar allows you to navigate to various portfolio destinations in order to view some of the applications and dashboards I've developed. :100:")

# making the sidebar selections work
if choice=='Streamlit':
    st.subheader('Streamlit Projects :spider_web:')
        
    st.write('---')
    # copy and pasting github readme file, 'ctrl'+'shift'+'[' to hide the text below
    st.write("""
        Welcome to my Streamlit Projects page! Here, you'll find a collection of innovative web applications that make data analysis and visualization easier and more efficient. Please feel free to take a look! 

        - Page-Performance-App: https://cjfuentes-datascience-page-performance--page-performance-sjkl73.streamlit.app/

        - Producer-Classification-Model: https://cjfuentes-datascience-producer-classific-pred-prod-class-yh3wdu.streamlit.app/

        - Portfolio Website: https://cjfuentes-datascience-porfolio-website-streaml-portfolio-02zrce.streamlit.app/

        - Linear-Regression-Weekly-Report: https://cjfuentes-datascience-linear-regression-weekly-lr-report-yujt5p.streamlit.app/
        
        - Weekly-Report: https://cjfuentes-datascience-weekly-report-stream-weekly-report-o4z4ny.streamlit.app/
        
        - Sales-Dashboard: https://cjfuentes-datascience-sales-dashboard-st-sales-dashboard-6wpnmb.streamlit.app/

        - Excel-Plotter: https://cjfuentes-datascience-excel-plotter-stream-excel-plotter-urkhnk.streamlit.app/

        - Stocks: https://cjfuentes-datascience-stocks-streamlit-stocks-z6vo0e.streamlit.app/
    """)
    
    st.write("Click the button below to view a list of **Streamlit** applications I've developed to bring data to life.")
    link = 'https://github.com/cjfuentes-datascience/STREAMLIT-PROJECTS'
    st.markdown(f'<a href="{link}" target="_blank" style="background-color: #4681f4; padding: 8px 16px; font-size: 16px; color: white; border-radius: 4px;">Github</a>', unsafe_allow_html=True)

if choice=='Python':
    st.subheader('Python Projects :snake:')
    st.write("Click the button below to view a list of **Python** applications I've developed to bring data to life.")
    link = 'https://github.com/cjfuentes-datascience/PYTHON-PROJECTS'
    st.markdown(f'<a href="{link}" target="_blank" style="background-color: #4681f4; padding: 8px 16px; font-size: 16px; color: white; border-radius: 4px;">Github</a>', unsafe_allow_html=True)
    
    st.write('---')
    # copy and pasting github readme file, 'ctrl'+'shift'+'[' to hide the text below
    st.write("""
        Below is a collection of Python projects I've compiled and uploaded to GitHub. Please feel free to have a look!

        - Producer-Classification-Model: https://github.com/cjfuentes-datascience/Producer-Classification-Model-Python

        - Loan-Repayment-Prediction: https://github.com/cjfuentes-datascience/Loan-Repayment-Prediction-Python

        - KNN-Diabetes: https://github.com/cjfuentes-datascience/KNN-Diabetes-Python

        - Predicting-Credit-Card-Fraud: https://github.com/cjfuentes-datascience/Predicting-Credit-Card-Fraud-Python

        - Clustering-With-K-Means: https://github.com/cjfuentes-datascience/Clustering-With-K-Means-Python

        - Weekly-Report: https://github.com/cjfuentes-datascience/Weekly-Report-Python

        - Compare-Machine-Learning-Classifiers: https://github.com/cjfuentes-datascience/Compare-Machine-Learning-Classifiers-Python

        - Building-a-Classification-Model: https://github.com/cjfuentes-datascience/Building-a-Classification-Model-Python

        - Fashion-Multiclass-Classification-Logistic-Regression: https://github.com/cjfuentes-datascience/Fashion-Multiclass-Classification-Logistic-Regression-Python

        - Multiclass-Classification: https://github.com/cjfuentes-datascience/Multiclass-Classification-Python

        - Logistical-Regression: https://github.com/cjfuentes-datascience/Logistical-Regression-Python

        - Predicting-Insurance-Charges: https://github.com/cjfuentes-datascience/Predicting-Insurance-Charges-Python

        - Simple-Linear-Regression-Model: https://github.com/cjfuentes-datascience/Simple-Linear-Regression-Model-Python

        - Beginner-Machine-Learning-Project: https://github.com/cjfuentes-datascience/Beginner-Machine-Learning-Project-Python

        - Tennis-Ace: https://github.com/cjfuentes-datascience/Tennis-Ace-Python

        - Women's-E-Commerce-Clothing: https://github.com/cjfuentes-datascience/Women-s-E-Commerce-Clothing

        - Honey-Production: https://github.com/cjfuentes-datascience/Honey-Production-Python

        - Linear Regression at Codecademy: https://github.com/cjfuentes-datascience/Linear-Regression-at-Codecademy-Python

        - K-Means Clustering From Scratch: https://github.com/cjfuentes-datascience/K-means-Clustering-From-Scratch-Python

        - Heart Disease Research Part I: https://github.com/cjfuentes-datascience/Heart-Disease-Research-Part-I-Python

        - Olympics Linear Regression: https://github.com/cjfuentes-datascience/Olympics-Linear-Regression-Python

        - NBA Trends: https://github.com/cjfuentes-datascience/NBA-Trends-Python

        - Exploring Student Data: https://github.com/cjfuentes-datascience/Exploring-Student-Data-Python

        - Sublime Limes Line Graphs: https://github.com/cjfuentes-datascience/Sublime-Limes-Line-Graphs-Python

        - Diagnosing Diabetes: https://github.com/cjfuentes-datascience/Diagnosing-Diabetes-Python

        - Census Variable Manipulation: https://github.com/cjfuentes-datascience/Census-Variable-Manipulation-Python

        - Automobile Variable Types: https://github.com/cjfuentes-datascience/Automobile-Variable-Types-Python

        - Page Visits Funnel: https://github.com/cjfuentes-datascience/Page-Visits-Funnel-Python

        - Fraud Detection: https://github.com/cjfuentes-datascience/Fraud-Detection-Python

        - A/B Testing for ShoeFly.com: https://github.com/cjfuentes-datascience/A-B-Testing-for-ShoeFly.com-Python

        - Exploring Mushrooms: https://github.com/cjfuentes-datascience/Exploring-Mushrooms-Python

        - Airline-Analysis: https://github.com/cjfuentes-datascience/Airline-Analysis-Python

        - Cleaning-US-Census-Data: https://github.com/cjfuentes-datascience/Cleaning-US-Census-Data-Python
    """)

if choice=='SQL':
    st.subheader('SQL Projects :bookmark_tabs:')
    st.write("Click the button below to view a list of **SQL** applications I've developed to bring data to life.")
    link = 'https://github.com/cjfuentes-datascience/SQL-PROJECTS'
    st.markdown(f'<a href="{link}" target="_blank" style="background-color: #4681f4; padding: 8px 16px; font-size: 16px; color: white; border-radius: 4px;">Github</a>', unsafe_allow_html=True)
    
    st.write('---')
    # copy and pasting github readme file, 'ctrl'+'shift'+'[' to hide the text below
    st.write("""
        Below is a collection of SQL projects I've compiled and uploaded to GitHub. Please feel free to have a look!

        - SpeedySpoon Data Aggregation: https://github.com/cjfuentes-datascience/SpeedySpoon-Data-Aggregation-SQL

        - Business Metrics For Mineblocks: https://github.com/cjfuentes-datascience/Business-Metrics-For-Mineblocks-SQL

        - Bakery Functions: https://github.com/cjfuentes-datascience/Bakery-Functions-SQL

        - Airline Table Transformations: https://github.com/cjfuentes-datascience/Airline-Table-Transformations-SQL

        - Transforming Flight Tables: https://github.com/cjfuentes-datascience/Tranforming-Flight-Tables-SQL

        - Set Operations: https://github.com/cjfuentes-datascience/Set-Operations-SQL

        - Customer Segmentation: https://github.com/cjfuentes-datascience/Customer-Segmentation-SQL

        - New York Restaurants: https://github.com/cjfuentes-datascience/New-York-Restaurants-SQL

        - Fraud Detection: https://github.com/cjfuentes-datascience/Fraud-Detection-Python

        - Analyze Hacker News Trends: https://github.com/cjfuentes-datascience/Analyze-Hacker-News-Trends-SQL
""")

if choice=='PowerBI':
    st.subheader('PowerBI Projects :chart_with_upwards_trend:')
    st.write("Click the button below to view a list of **PowerBI** applications I've developed to bring data to life.")
    link = 'https://github.com/cjfuentes-datascience/POWER-BI-PROJECTS'
    #st.button('Github', link)
    st.markdown(f'<a href="{link}" target="_blank" style="background-color: #4681f4; padding: 8px 16px; font-size: 16px; color: white; border-radius: 4px;">Github</a>', unsafe_allow_html=True)

    st.write('---')
    # copy and pasting github readme file, 'ctrl'+'shift'+'[' to hide the text below
    st.write("""
        Below is a collection of Power BI projects I've compiled and uploaded to GitHub. Please feel free to have a look!

        - Sales-Report: https://github.com/cjfuentes-datascience/Sales-Report-PowerBI

        - Data-Professional-Survey: https://github.com/cjfuentes-datascience/Data-Professional-Survey

        - Executive-Summary-Finance-Report: https://github.com/cjfuentes-datascience/Executive-Summary-Finance-Report 

        - Exploring-Top-Google-Searches-2021: https://github.com/cjfuentes-datascience/Exploring-Top-Google-Searches-2021-PowerBI

        - E-Commerce-Data-and-Profit-Analysis: https://github.com/cjfuentes-datascience/E-Commerce-Data-and-Profit-Analysis

        - Adventure-Works-Sales-Analysis: https://github.com/cjfuentes-datascience/Adventure-Works-Sales-Analysis

        - IT-Spend: https://github.com/cjfuentes-datascience/IT-Spend
""")

if choice=='Tableau':
    st.subheader('Tableau Projects :chart_with_downwards_trend:')
    st.write("Click the button below to view a list of **Tableau** applications I've developed to bring data to life.")
    link = 'https://github.com/cjfuentes-datascience/TABLEAU-PROJECTS'
    st.markdown(f'<a href="{link}" target="_blank" style="background-color: #4681f4; padding: 8px 16px; font-size: 16px; color: white; border-radius: 4px;">Github</a>', unsafe_allow_html=True)
    
    st.write('---')
    # copy and pasting github readme file, 'ctrl'+'shift'+'[' to hide the text below
    st.write("""
        Below is a collection of Tableau projects I've compiled and uploaded to GitHub. Please feel free to have a look!

        - Customer-Analysis: https://public.tableau.com/app/profile/carlos3124/viz/CustomerAnalysis_16716030653630/Dashboard1

        - Walmart Retail Data Analysis: https://public.tableau.com/app/profile/carlos3124/viz/WalmartRetailDataAnalysis_16716465467070/Dashboard1

        - Global-Performance-Dashboard: https://public.tableau.com/app/profile/carlos3124/viz/GlobalPerformanceDashboard_16722453536720/Dashboard1

        - Product-Line-Performance: https://public.tableau.com/app/profile/carlos3124/viz/ProductLinePerformance_16643961849890/ProductLinePerformance
""")

st.write('---')

st.text('Thanks For Stopping By!')
