import streamlit as st
from scrapping.GetProductsConforama import GetProductsConforama
import time

search = st.text_input(label='Wich product do you want to search ?')

btn_submit = st.button(label='Submit')

data = []

if btn_submit:
    st.write('You search for : %s' % search)
    cdiscount = GetProductsConforama(handless=True)
    data = cdiscount.get_products(search)

    for product in data:
        st.markdown("""
        <div style="display: flex; flex-direction: row; justify-content: space-between; align-items: center; margin: 10px 0;">
            <div style="display: flex; flex-direction: row; align-items: center;">
                <img src="%s" style="width: 100px; height: 100px; border-radius: 10px;"/>
                <div style="display: flex; flex-direction: column; margin-left: 10px;">
                    <h1 style="font-size: 12px;">%s</h1>
                    <div style="display: flex; align-items: center; justify-content: evenly">
                        <p style="font-size: 10px;">%s</p>
                        <p style="font-size: 10px;">%s</p>
                        <p style="font-size: 10px;">%s</p>
                    </div>
                </div>
            </div>
        </div>
        """ % (product["image"], product["name"], product["seller"], product["rating"], product["price"]), unsafe_allow_html=True)