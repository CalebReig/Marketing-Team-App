import streamlit as st


def app():
    st.title('About')
    st.header('About XCorp')
    st.write("""
            XCorp is a fictional company used to represent the store that this data derived from.
            This app was made to demonstrate how customer data can be used to assist the marketing team.
            """)
    st.header('About the Data')
    st.write("""
            This dataset was collected from Kaggle @ https://www.kaggle.com/imakash3011/customer-personality-analysis.
            The initial analysis of this data and model creation/clustering is on my github @ https://github.com/CalebReig/ML-Projects/tree/main/Customer-Analysis.
            """)
    st.header('Creator Contact Info')
    st.write("""
            email: reigadacaleb@gmail.com\n
            github: https://github.com/CalebReig\n
            linkedin: https://www.linkedin.com/in/caleb-reigada-840a23201/
            """)