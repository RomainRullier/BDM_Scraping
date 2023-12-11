import streamlit as st
from scrapping.ScrapBM import GetArticlesBySearchBM
import pandas as pd

st.set_page_config(page_title="Streamlit", page_icon="🔫", layout="wide")

st.title("BDM Scrapping")
df = None
is_extracted = False

with st.form(key='my_form'):
    search = st.text_input(label='Enter your search')
    slider = st.number_input(label='Enter the number of pages', min_value=1, max_value=999, value=1)
    submit = st.form_submit_button(label='Submit')

    if submit:
        scrap_bm = GetArticlesBySearchBM(search, slider)
        exported_data = scrap_bm.get_articles_by_pages()
        scrap_bm.saves_articles_to_json(exported_data)
        st.balloons()
        st.success("Data exported successfully!")

        df = pd.read_json("exports/%s.json" % search)
        st.write(df)
        is_extracted = True

if is_extracted:
    st.download_button(
        label="Download data",
        data=df.to_csv().encode('utf-8'),
        file_name='export_article.csv',
        mime='text/csv'
    )





