import streamlit as st
from scrapping.GetProductsConforama import GetProductsConforama
import time

search = st.text_input(label='Wich product do you want to search ?')

btn_submit = st.button(label='Submit')

if btn_submit:
    st.write('You search for : %s' % search)
    cdiscount = GetProductsConforama()
    st.write(cdiscount.get_products(search))