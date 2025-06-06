import streamlit as st
import pandas as pd

st.title("Crop Data Dashboard")
st.subheader("Welcome to crop data dashboard")
st.write("The dashboard provides insights into various crops and their data.")

st.sidebar.header("Please select a file")
st.sidebar.subheader("Upload a Csv file")
file = st.sidebar.file_uploader("upload a file" , type = [("csv")])

option = st.sidebar.selectbox("Select an option", ["Data Preview", "Data Visualization" ], key="sidebar")

if file:
    
    if option == "Data Preview":
        df = pd.read_csv(file)
        st.subheader("Data Preview")
        st.dataframe(df)


    if option == "Data Visualization":
        df = pd.read_csv(file)  
        st.header("Data Analysis")
        st.write(df.describe())

        st.header("Data Visualization")
        crops = df['label'].unique()
        select_crop = st.selectbox("Select a crop", crops)
        st.subheader("Bar Chart")
        st.bar_chart(df[df['label'] == select_crop].drop(columns=['label']))
        st.subheader("Line Chart")
        st.line_chart(df[df['label'] == select_crop].drop(columns=['label']))
        st.subheader("Area Chart")
        st.area_chart(df[df['label'] == select_crop].drop(columns=['label']))

else:
    st.sidebar.warning("Please upload a CSV file to see the data preview and analysis.")
    
    
    