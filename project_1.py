import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Data Cleaning Dashboard")

# File uploader to upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)

    # Display the first few rows of the dataframe
    st.subheader("Original Dataset")
    st.write(df.head())

    # Display dataset info
    st.subheader("Dataset Info")
    st.write(df.info())

    # Handle missing values
    st.subheader("Remove Missing Values")
    if st.checkbox("Remove rows with missing values", value=True):
        df_cleaned = df.dropna()
        st.write("Rows with missing values have been dropped.")
    else:
        df_cleaned = df
        st.write("Missing values remain.")

    # Drop duplicates
    st.subheader("Remove Duplicates")
    if st.checkbox("Remove duplicate rows", value=True):
        df_cleaned = df_cleaned.drop_duplicates()
        st.write("Duplicate rows have been dropped.")
    else:
        st.write("Duplicate rows remain.")

    # Basic data transformation example: Convert all column names to lowercase
    st.subheader("Convert Column Names to Lowercase")
    if st.checkbox("Convert column names to lowercase"):
        df_cleaned.columns = [col.lower() for col in df_cleaned.columns]
        st.write("Column names converted to lowercase.")
    else:
        st.write("Column names remain unchanged.")

    # Display cleaned data
    st.subheader("Cleaned Dataset")
    st.write(df_cleaned.head())

    # Download button to download the cleaned data
    st.subheader("Download Cleaned Data")
    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    cleaned_data = convert_df(df_cleaned)
    st.download_button(
        label="Download cleaned CSV",
        data=cleaned_data,
        file_name='cleaned_data.csv',
        mime='text/csv'
    )
