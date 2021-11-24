from models import *
import numpy as np
import streamlit as st

def customer_form():
    with st.form('user_inputs'):
        edu = st.selectbox('Education', options=['Basic', 'Master', '2n Cycle', 'Graduation', 'PhD'])
        income = st.number_input('Income', min_value=0, value=30000, step=5000)
        recency = st.number_input('Days Since Last Purchase', min_value=0, value=50, step=5)
        wine = st.number_input('Amount Spent on Wine', min_value=0, value=500, step=50)
        fruit = st.number_input('Amount Spent on Fruit', min_value=0, value=500, step=50)
        meat = st.number_input('Amount Spent on Meat', min_value=0, value=500, step=50)
        fish = st.number_input('Amount Spent on Fish', min_value=0, value=500, step=50)
        sweet = st.number_input('Amount Spent on Sweets', min_value=0, value=500, step=50)
        gold = st.number_input('Amount Spent on Gold', min_value=0, value=500, step=50)
        deals = st.number_input('Number of Deal Purchases', min_value=0, value=1)
        web = st.number_input('Number of Web Purchases', min_value=0, value=2)
        catalog = st.number_input('Number of Catalog Purchases', min_value=0, value=0)
        store = st.number_input('Number of Store Purchases', min_value=0, value=4)
        web_visits = st.number_input('Number of Web Visits', min_value=0, value=1)
        complain = st.selectbox('Complain', options=[0, 1])
        age = st.number_input('Age', min_value=0, value=45)
        days_since_cus = st.number_input('Days Since Becoming a Customer', min_value=0, value=180, step=20)
        fam = st.number_input('Family Size', min_value=1, value=2)
        num_acc = st.number_input('Number of Marketing Accepted', min_value=0, value=0)
        total = wine + meat + fruit + fish + sweet + gold
        st.form_submit_button()
    new_cus = np.array([edu, income, recency, wine, fruit, meat, fish, sweet, gold,
               deals, web, catalog, store, web_visits, complain, age, days_since_cus,
               fam, num_acc, total])

    return new_cus

@st.cache
def load_predict(new_cus):
    pipeline = load_pipeline()
    pred = pipeline.predict(new_cus.reshape(1, -1))
    text = 'Will Respond to Marketing'
    if pred == 0:
        text = 'Will Not Respond to Marketing'
    return text


def app():
    st.title('XCorp Marketing Team Web App')
    st.write('Welcome to the XCorp marketing team web app. This web app ' +\
             'assists the marketing team in making decisions on how to spend ' +\
             'resources on new and existing customers.')
    st.header('Customer Response Prediction')
    st.write('Enter the information of a new customer to predict if the ' + \
             'customer will respond to marketing.')
    new_cus = customer_form()
    prediction = load_predict(new_cus)
    st.write('Prediction: ' + prediction)





