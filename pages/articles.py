import streamlit as st
import pandas as pd

from os import listdir
from os.path import isfile, join

df = None


st.set_page_config(page_title="Streamlit App", page_icon="🧊", layout="wide")

mypath = "exports"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

st.title("Articles")

file = st.selectbox("Select a file", onlyfiles)

if file:
    df = pd.read_json("exports/%s" % file)

if df is not None:
    for index, row in df.iterrows():
        col, col2 = st.columns(2)
        with col:
            st.image(row["img"])
        with col2:
            st.markdown("""
            <div style="border: 1px solid #f5f5f5; padding: 10px; border-radius: 10px;">
               <h1 style="font-size: 12px;">%s</h1>
                <p style="font-size: 10px;">%s</p>
                <p style="font-size: 10px;">%s</p>
            </div>
         
            """
                        % (row["name_article"], row["category"], row["datetime"][0]), unsafe_allow_html=True)


