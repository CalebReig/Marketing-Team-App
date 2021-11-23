import streamlit as st
import plotly.express as px
import models

def create_3d_scatter(data):
    fig = px.scatter_3d(data,
                        x='0',
                        y='1',
                        z='2',
                        color='Cluster')
    return fig

@st.cache
def load_data():
    data = models.load_3d()
    return data

def display_cluster(clus):
    info = {
        'Cluster 0':
            """
            Cluster 0
            ---------
            * Low Spending
            * Lower Income
            * Larger Family
            * Middle Aged
            * Doesn't Respond to Marketing
            """,
        'Cluster 1':
            """
            Cluster 1
            ---------
            * Moderate Spending
            * Smaller Family
            * Retirement Aged
            * High Catalog and Web Purchases
            * Long Time Customer
            * Moderate Response to Marketing
            """,
        'Cluster 2':
            """
            Cluster 2
            ---------
            * High Spending
            * Smaller Family
            * Moderate Catalog and Web Purchases
            * Early-Middle Aged
            * Slight Response to Marketing
            """,
        'Outliers (-1)':
            """
            Outliers (-1)
            -------------
            * Variant Spending
            * Medium-High Income
            * Medium Sized Family
            * Middle Aged
            * Moderate Catalog and Web Purchases
            * High Response to Marketing
        """
    }
    return info[clus]

def app():
    st.title('XCorp Customer Clusters')
    st.write('XCorp customer can be grouped into one of four clusters based on their behaviors. ' +\
             'See how our customers are grouped in the display below of customer data represented in 3 dimensions.')
    data = load_data()
    st.plotly_chart(create_3d_scatter(data))
    clus = st.selectbox('About the Clusters', ['Cluster 0', 'Cluster 1', 'Cluster 2', 'Outliers (-1)'])
    st.markdown(display_cluster(clus))

