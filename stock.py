# Importing & Loading Packages and Libraries
import yfinance as yf
import streamlit as st
import pandas as pd

st.markdown('''
# **Stock Price App**
# *2010 - 2022*

Application built in `Python` + `Streamlit` + `GitHub` by [Abdullahi M. Cadceed](https://twitter.com/@abdullahcadceed)

---
''')

# define the ticker symbol
tickerSymbol = 'GOOGL'

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# get the historical prices for this ticker
tickerDf = tickerData.history(period='id', start='2010-1-1', end='2022-12-31')

# Open high low close volume dividends stock splits
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
