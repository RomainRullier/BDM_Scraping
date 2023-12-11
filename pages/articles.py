import streamlit as st
import pandas as pd

from os import listdir
from os.path import isfile, join

df = None


st.set_page_config(page_title="Streamlit App", page_icon="🧊", layout="wide")

mypath = "exports"

list_files = [f.replace(".json", '') for f in listdir(mypath)]

st.title("Articles")

file = st.selectbox("Select a file", list_files)

if file:
    df = pd.read_json("exports/%s.json" % file)

if df is not None:
    for index, row in df.iterrows():
        st.markdown("""
        <div style="margin-top : 20px">
            <a href="%s" target="_blank" style="text-decoration : none; color : inherit">
            <div style="display: flex; flex-direction: row; border: 1px solid #f5f5f5; padding: 10px; border-radius: 10px;">
                <img src="%s" style="width: 100px; height: 100px; border-radius: 10px;"/>
                <div style="display: flex; flex-direction: column; margin-left: 10px;">
                    <h1 style="font-size: 12px;">%s</h1>
                    <p style="font-size: 10px;">%s</p>
                    <p style="font-size: 10px;">%s</p>
                </div>
            </div>
        </div>
        """ % ( row["link_article"], row["img"], row["name_article"], row["category"], row["datetime"][0]), unsafe_allow_html=True)
