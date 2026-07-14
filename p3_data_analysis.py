import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Data Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("Analysing Data")
st.divider()

file = st.file_uploader("Upload your CSV file", type=["csv"])


# condition to check if file is uploaded
if file is not None:
    df = pd.read_csv(file)
    st.success("File uploaded sucessfully!")

# metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Rows", df.shape[0])
    col2.metric("Total Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())
    col4.metric("Duplicate Rows", df.duplicated().sum())

    st.divider()
    st.subheader("Data Preview")
    st.dataframe(df.head())

    st.divider()
    st.subheader("Statistics")
    st.dataframe(df.describe())

    st.divider()
    st.subheader("Charts")

    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()

    if len(numeric_cols) > 0:
        selected_col = st.selectbox("Select column to chart", numeric_cols)
        st.bar_chart(df[selected_col])
    else:
        st.warning("No numeric columns found for charts.")


    st.divider()
    st.subheader("Download Data")

    csv = df.to_csv(index=False)
    st.download_button(
        label="Download CSV file",
        data= csv,
        file_name="analysed_data.csv",
        mime="text/csv"
    )



    
