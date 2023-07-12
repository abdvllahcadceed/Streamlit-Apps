# Import Libraries
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# Page Title
image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)
st.write("""
# DNA Nucleotide Count Web App

Application built in `Python` + `Streamlit` + `GitHub` by [Abdullahi M. Cadceed](https://twitter.com/@abdullahcadceed)

This App counts the nucleotide composition of your DNA Sequence
***

""")

# Input Text Box
st.header('Enter Your DNA sequence')

sequence_input = ""
sequence = st.text_area("Input Sequence & Press Ctrl+Enter to Apply", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = ''.join(sequence)

st.write('''
***
''')

# Print the Input DNA Sequence
st.header('Input (DNA Query)')
sequence

# DNA Nucleotide Count
st.header('Output (DNA Nucleotide Count)')

# Print Dictionary
st.subheader('1. The Dictionary')
def DNA_Nucleotide_Count(seq):
	d = dict([
		('A', seq.count('A')),
		('T', seq.count('T')),
		('G', seq.count('G')),
		('C', seq.count('C'))
		])
	return d

X = DNA_Nucleotide_Count(sequence)

#X.label = list(X)
#X.values = list(X.values())

X


# Print Text
st.subheader('2. The Text')
st.write('There are ' + str(X['A']) + 'Adenine (A)')
st.write('There are ' + str(X['T']) + 'Thymine (T)')
st.write('There are ' + str(X['G']) + 'Guanine (G)')
st.write('There are ' + str(X['C']) + 'Cytosine (C)')

# Display DataFrame
st.subheader('3. The DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

# Display Bar Chart
st.subheader('4. The Visualization')
p = alt.Chart(df).mark_bar().encode(
x = 'nucleotide',
y = 'count'
	)

p = p.properties(
	width=alt.Step(60)
	)
st.write(p)














