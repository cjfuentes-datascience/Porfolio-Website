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
    st.write("Click the button below to view a list of **Streamlit** applications I've developed to bring data to life.")
    link = 'https://github.com/cjfuentes-datascience/STREAMLIT-PROJECTS'
    st.markdown(f'<a href="{link}" target="_blank" style="background-color: #4681f4; padding: 8px 16px; font-size: 16px; color: white; border-radius: 4px;">Github</a>', unsafe_allow_html=True)
    
    st.write('---')
    # copy and pasting github readme file, 'ctrl'+'shift'+'[' to hide the text below
    st.write("""
        Welcome to my Streamlit Projects page! Here, you'll find a collection of innovative web applications that make data analysis and visualization easier and more efficient. Please feel free to take a look! 

        - Page-Performance-App: https://cjfuentes-datascience-page-performance--page-performance-sjkl73.streamlit.app/

        - Producer-Classification-Model: https://cjfuentes-datascience-producer-classific-pred-prod-class-yh3wdu.streamlit.app/

        - Portfolio Website: https://cjfuentes-datascience-porfolio-website-streaml-portfolio-02zrce.streamlit.app/

        - Linear-Regression-Weekly-Report: A Streamlit web app that performs linear regression analysis and displays the predictions https://cjfuentes-datascience-linear-regression-weekly-lr-report-yujt5p.streamlit.app/
        - Weekly-Report: A streamlined web application for effortlessly creating weekly reports https://cjfuentes-datascience-weekly-report-stream-weekly-report-o4z4ny.streamlit.app/

        - Sales-Dashboard: An intuitive web application for visualizing sales data in a meaningful and organized way https://cjfuentes-datascience-sales-dashboard-st-sales-dashboard-6wpnmb.streamlit.app/

        - Excel-Plotter: A user-friendly web application that empowers you to plot your data from an excel file with ease https://cjfuentes-datascience-excel-plotter-stream-excel-plotter-urkhnk.streamlit.app/

        - Stocks: A dynamic web application that keeps you updated on your favorite stocks https://cjfuentes-datascience-stocks-streamlit-stocks-z6vo0e.streamlit.app/
    """)

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

        - Weekly-Report: This project aims to automate the weekly report creation process using the pandas library in Python. https://github.com/cjfuentes-datascience/Weekly-Report-Python

        - Compare-Machine-Learning-Classifiers: This project demonstrates how to compare the performance of several machine learning classifiers in Python using the scikit-learn package. https://github.com/cjfuentes-datascience/Compare-Machine-Learning-Classifiers-Python

        - Building-a-Classification-Model: This project demonstrates how to build a simple machine learning model in Python using the scikit-learn package. The model is a classification model used to classify Iris flowers using the random forest algorithm. https://github.com/cjfuentes-datascience/Building-a-Classification-Model-Python

        - Fashion-Multiclass-Classification-Logistic-Regression: This project uses logistic regression to classify images of clothing into different categories
        https://github.com/cjfuentes-datascience/Fashion-Multiclass-Classification-Logistic-Regression-Python

        - Multiclass-Classification: This project uses various machine learning algorithms to classify instances into one of multiple classes
        https://github.com/cjfuentes-datascience/Multiclass-Classification-Python

        - Logistical-Regression: The goal of this project is to implement logistic regression algorithm on multiple datasets and compare the results
        https://github.com/cjfuentes-datascience/Logistical-Regression-Python

        - Predicting-Insurance-Charges: This project uses logistic regression to predict insurance charges
        https://github.com/cjfuentes-datascience/Predicting-Insurance-Charges-Python

        - Simple-Linear-Regression-Model: The goal of this project is to demonstrate the basic implementation of linear regression and its usage https://github.com/cjfuentes-datascience/Simple-Linear-Regression-Model-Python

        - Beginner-Machine-Learning-Project: This project is a beginner's project that covers the basics of machine learning and data analysis
        https://github.com/cjfuentes-datascience/Beginner-Machine-Learning-Project-Python

        - Tennis-Ace: Creating a linear regression model that predicts the outcome for a tennis player based on their playing habits. https://github.com/cjfuentes-datascience/Tennis-Ace-Python

        - Women's-E-Commerce-Clothing: Data analysis project that uses Python to explore and visualize data from a clothing company's e-commerce website.  https://github.com/cjfuentes-datascience/Women-s-E-Commerce-Clothing

        - Honey-Production: Data analysis project that uses Python to explore and visualize data on honey production in the United States.
        https://github.com/cjfuentes-datascience/Honey-Production-Python

        - Linear Regression at Codecademy: A project involving the implementation of linear regression in Python.
        https://github.com/cjfuentes-datascience/Linear-Regression-at-Codecademy-Python

        - K-Means Clustering From Scratch: A project implementing the K-Means clustering algorithm from scratch in Python. 
        https://github.com/cjfuentes-datascience/K-means-Clustering-From-Scratch-Python

        - Heart Disease Research Part I: A project analyzing heart disease data and implementing various machine learning models to predict the presence of heart disease.
        https://github.com/cjfuentes-datascience/Heart-Disease-Research-Part-I-Python

        - Olympics Linear Regression: A project using linear regression to analyze Olympic data.
        https://github.com/cjfuentes-datascience/Olympics-Linear-Regression-Python

        - NBA Trends: A project analyzing trends in NBA data.
        https://github.com/cjfuentes-datascience/NBA-Trends-Python

        - Exploring Student Data: A project exploring and analyzing student data.
        https://github.com/cjfuentes-datascience/Exploring-Student-Data-Python

        - Sublime Limes Line Graphs: A project creating line graphs to visualize data on the sales of Sublime Limes.
        https://github.com/cjfuentes-datascience/Sublime-Limes-Line-Graphs-Python

        - Diagnosing Diabetes: A project using machine learning to predict the presence of diabetes.
        https://github.com/cjfuentes-datascience/Diagnosing-Diabetes-Python

        - Census Variable Manipulation: A project manipulating and analyzing census data.
        https://github.com/cjfuentes-datascience/Census-Variable-Manipulation-Python

        - Automobile Variable Types: A project exploring and analyzing data on automobile variables.
        https://github.com/cjfuentes-datascience/Automobile-Variable-Types-Python

        - Page Visits Funnel: A project analyzing page visit data to optimize a website's sales funnel.
        https://github.com/cjfuentes-datascience/Page-Visits-Funnel-Python

        - Fraud Detection: A project using machine learning to detect fraudulent activity.
        https://github.com/cjfuentes-datascience/Fraud-Detection-Python

        - A/B Testing for ShoeFly.com: A project implementing A/B testing on the ShoeFly.com website. https://github.com/cjfuentes-datascience/A-B-Testing-for-ShoeFly.com-Python

        - Exploring Mushrooms: A project exploring and analyzing mushroom data.
        https://github.com/cjfuentes-datascience/Exploring-Mushrooms-Python

        - Airline-Analysis: Python project that involves analyzing airline data. https://github.com/cjfuentes-datascience/Airline-Analysis-Python

        - Cleaning-US-Census-Data: Python project that involves cleaning and preparing US Census data for analysis. https://github.com/cjfuentes-datascience/Cleaning-US-Census-Data-Python
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

        - SpeedySpoon Data Aggregation: A project involving the aggregation of data from the SpeedySpoon database.
        https://github.com/cjfuentes-datascience/SpeedySpoon-Data-Aggregation-SQL

        - Business Metrics For Mineblocks: A project analyzing business metrics for the Mineblocks game.
        https://github.com/cjfuentes-datascience/Business-Metrics-For-Mineblocks-SQL

        - Bakery Functions: A project involving the creation of functions for a bakery database.
        https://github.com/cjfuentes-datascience/Bakery-Functions-SQL

        - Airline Table Transformations: A project involving the transformation of tables in an airline database.
        https://github.com/cjfuentes-datascience/Airline-Table-Transformations-SQL

        - Transforming Flight Tables: A project involving the transformation of flight tables.
        https://github.com/cjfuentes-datascience/Tranforming-Flight-Tables-SQL

        - Set Operations: A project involving the use of set operations in SQL.
        https://github.com/cjfuentes-datascience/Set-Operations-SQL

        - Customer Segmentation: A project involving the segmentation of customers in a database.
        https://github.com/cjfuentes-datascience/Customer-Segmentation-SQL

        - New York Restaurants: A project involving the analysis of restaurant data in New York. 
        https://github.com/cjfuentes-datascience/New-York-Restaurants-SQL

        - Fraud Detection: A project using SQL to detect fraudulent activity.
        https://github.com/cjfuentes-datascience/Fraud-Detection-Python

        - Analyze Hacker News Trends: A project analyzing trends in Hacker News data using SQL.
        https://github.com/cjfuentes-datascience/Analyze-Hacker-News-Trends-SQL
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

        - Sales-Report: The report includes several visualizations and a dashboard that allows users to explore and analyze different aspects of the sales data. https://github.com/cjfuentes-datascience/Sales-Report-PowerBI

        - Data-Professional-Survey: This project involves analyzing data from a survey of data professionals, including their demographics, skills, and experience, and presenting the results in a Power BI dashboard. https://github.com/cjfuentes-datascience/Data-Professional-Survey

        - Executive-Summary-Finance-Report: This project involves creating an executive summary of financial data and presenting it in a Power BI dashboard. https://github.com/cjfuentes-datascience/Executive-Summary-Finance-Report 

        - Exploring-Top-Google-Searches-2021: This project involves analyzing data on the top Google searches of 2021 and presenting the results in a Power BI dashboard.
        https://github.com/cjfuentes-datascience/Exploring-Top-Google-Searches-2021-PowerBI

        - E-Commerce-Data-and-Profit-Analysis: This project involves analyzing data on an e-commerce business, including sales data and customer demographics, and presenting the results in a Power BI dashboard. https://github.com/cjfuentes-datascience/E-Commerce-Data-and-Profit-Analysis

        - Adventure-Works-Sales-Analysis: This project involves analyzing sales data for a fictional company, Adventure Works, and presenting the results in a Power BI dashboard. https://github.com/cjfuentes-datascience/Adventure-Works-Sales-Analysis

        - IT-Spend: This project involves analyzing data on IT spend and presenting it in a Power BI dashboard. https://github.com/cjfuentes-datascience/IT-Spend
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

        - Customer-Analysis: Dashboard that provides insights into customer behavior and demographics.
        https://public.tableau.com/app/profile/carlos3124/viz/CustomerAnalysis_16716030653630/Dashboard1

        - Walmart Retail Data Analysis: Visualization of data related to the retail operations of Walmart, using Tableau software. https://public.tableau.com/app/profile/carlos3124/viz/WalmartRetailDataAnalysis_16716465467070/Dashboard1

        - Global-Performance-Dashboard: Visual analytics tool that allows users to track and monitor the performance of a company or organization on a global scale. https://public.tableau.com/app/profile/carlos3124/viz/GlobalPerformanceDashboard_16722453536720/Dashboard1

        - Product-Line-Performance: Visualization that shows the performance of different product lines over time.
        https://public.tableau.com/app/profile/carlos3124/viz/ProductLinePerformance_16643961849890/ProductLinePerformance
""")

st.write('---')

st.text('Thanks For Stopping By!')
