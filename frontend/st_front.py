import streamlit as st
import requests
from data_structure import Tuits

def main():
    st.set_page_config(page_title="Sentiment Analysis App", page_icon="📚")
    st.title("Sentiment Analysis 📚🤖")

    with st.form("my_form"):
        tweet1 = st.text_input("First text")
        tweet2 = st.text_input("Second text")

        submitted = st.form_submit_button("PREDICT")

        if submitted:
            msg = Tuits(textos=[tweet1,tweet2])

            response = requests.post('http://localhost:8000/predict', json=msg.__dict__)

            st.write(response.json())


if __name__ == '__main__':
    main()
    