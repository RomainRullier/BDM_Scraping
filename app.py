import streamlit as st
from scrapping.ScrapBM import GetArticlesBySearchBM

st.set_page_config(page_title="Streamlit", page_icon="🔫", layout="wide")

st.title("BDM Scrapping")

st.sidebar.title("Menu")

pages = ["Accueil", "Recherche"]
choice = st.sidebar.selectbox("Choix de la page", pages)

if choice == "Accueil":
    st.header("Accueil")

if choice == "Recherche":
    st.header("Recherche")
    search = st.text_input("Rechercher un article")
    submit = st.button("Valider")