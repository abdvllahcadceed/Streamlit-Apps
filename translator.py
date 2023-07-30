from google_trans_new import google_translator
import streamlit as st

translator = google_translator()

st.title("Simple Somali to English Web App Translator")

st.write("""
Application built in `Python` + `Streamlit` + `GitHub` by [Abdullahi M. Cadceed](https://twitter.com/@abdullahcadceed)
""")

text = st.text_input("Type Your Text Here & Press ENTER!")
translate = translator.translate(text,lang_tgt='de')
st.write(translate)
