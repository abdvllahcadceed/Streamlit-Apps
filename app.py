import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title

st.markdown('''
# **Automated Exploratory Data Analysis**


Application built in `Python` + `Streamlit` + `GitHub` by [Abdullahi M. Cadceed](https://twitter.com/@abdullahcadceed)

---
''')

# Upload CSV data
with st.sidebar.header('Upload'):
    uploaded_file = st.sidebar.file_uploader("Upload your dataset in CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example of CSV Dataset](https://raw.githubusercontent.com/abdvllahcadceed/datasets/main/unhcr-idp.csv)
""")

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Your Dataset**')
    st.write(df)
    st.write('---')
    st.header('**Exploratory Data Analysis Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting your data to be uploaded!')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**The Example Dataset**')
        st.write(df)
        st.write('---')
        st.header('**The Example Exploratory Data Analysis Report**')
        st_profile_report(pr)
