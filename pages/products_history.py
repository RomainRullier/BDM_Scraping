from classes.DataBase import DataBase
import streamlit as st

db = DataBase()
db.init('conforama-products')

list_products = db.get_all_products()
list_products.reverse()

for product in list_products:
    st.write(product)
    st.markdown("""
    <div style="display: flex; flex-direction: row; justify-content: space-between; align-items: center; margin: 10px 0;">
        <div style="display: flex; flex-direction: row; align-items: center;">
            <img src="%s" style="width: 100px; height: 100px; border-radius: 10px;"/>
            <div style="display: flex; flex-direction: column; margin-left: 10px;">
                <h1 style="font-size: 12px;">%s</h1>
                <div style="display: flex; flex-direction: column; justify-content: evenly">
                    <p style="font-size: 10px;">%s</p>
                    <p style="font-size: 10px;">%s</p>
                    <p style="font-size: 10px;">%s</p>
                </div>
            </div>
        </div>
    </div>
    """ % (product["image"], product["name"], product["seller"], product["rating"], product["price"]), unsafe_allow_html=True)