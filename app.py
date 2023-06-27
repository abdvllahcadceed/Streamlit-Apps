import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title
st.image("https://www.onepointltd.com/wp-content/uploads/2019/12/ONE-POINT-01-1.png")

st.markdown('''
# **Automated Exploratory Data Analysis**

This is the **EDA Application** created in Streamlit using the **Pandas-Profiling** library.

Application built in `Python` + `Streamlit` by [Abdullahi M. Cadceed](https://twitter.com/@abdullahcadceed)

---
''')

# Upload CSV data
with st.sidebar.header('Upload'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file](https://https://raw.githubusercontent.com/abdvllahcadceed/pyProjects/main/unhcr-idp.csv)
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
    st.header('**EDA Report**')
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
        st.header('**EDA Report**')
        st_profile_report(pr)
