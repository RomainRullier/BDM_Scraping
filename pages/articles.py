import streamlit as st
import pandas as pd

from os import listdir
from os.path import isfile, join

st.set_page_config(page_title="Streamlit App", page_icon="🧊", layout="wide")

mypath = "exports"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

st.title("Articles")

file = st.selectbox("Select a file", onlyfiles)

df = pd.read_json("exports/%s" % file)

st.write(df.T)

