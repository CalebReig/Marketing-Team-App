import streamlit as st
import plotly.express as px
from scipy import stats
import models

@st.cache
def load():
    data = models.load_data()
    return data.drop('Education', axis=1)

def hist_plot(data, x):
    fig = px.histogram(
        data_frame=data,
        x=x,
        title=("Count of " + x)
    )
    return fig

def scatter_plot(data, x, y):
    fig = px.scatter(
        data_frame=data,
        x=x,
        y=y,
        color="Response",
        title=(x + " by " + y),
    )
    return fig

def create_graph(data, x, y=None):
    if y:
        return scatter_plot(data, x, y)
    else:
        return hist_plot(data, x)

def print_stats(data, x, y=None):
    if y:
        v1 = data[x].values
        v2 = data[y].values
        r, p = stats.pearsonr(v1, v2)
        v1_mean = v1.mean()
        v1_std = v1.std()
        v2_mean = v2.mean()
        v2_std = v2.std()
        text = "Correlation Between " + x + " and " + y + ": " + str(round(r, 4)) +\
                "\nCorrelation p-value: " + str(p) + "\n" +\
                x + " Mean: " + str(round(v1_mean, 2)) + "\n" + str(x) + " Standard Deviation: " +\
                str(round(v1_std, 2)) + "\n" + y + " Mean: " + str(round(v2_mean, 2)) + "\n" +\
                y + " Standard Deviation: " + str(round(v2_std, 2))
    else:
        v1 = data[x].values
        v1_mean = v1.mean()
        v1_std = v1.std()
        text = x + " Mean: " + str(round(v1_mean, 2)) + "\n" + str(x) + " Standard Deviation: " +\
                str(round(v1_std, 2))

    return text


def display_var_info(var):
    info = {
        'Income': "Customer's yearly household income",
        'Days_Since_Customer': "Number of days since customer's enrollment with the company",
        'Recency': "Number of days since customer's last purchase",
        'Complain': "1 if customer complained in the last 2 years, 0 otherwise",
        'Age': "The age of the customer",
        "Fam_Size": "The amount of members in the customer's household themself included",
        'Num_Accepted': "The number of previous campaign offers that the customer accepted",
        'MntTotal': "The total amount spent on store items by the customer in the last 2 years",
        'MntWines': "Amount spent on wine in last 2 years",
        'MntFruits': "Amount spent on fruits in last 2 years",
        'MntMeatProducts' : "Amount spent on meat in last 2 years",
        'MntFishProducts': "Amount spent on fish in last 2 years",
        'MntSweetProducts': "Amount spent on sweets in last 2 years",
        'MntGoldProds': "Amount spent on gold in last 2 years",
        'NumWebPurchases': "Number of purchases made through the company’s web site",
        'NumCatalogPurchases': "Number of purchases made using a catalog",
        'NumStorePurchases': "Number of purchases made directly in stores",
        'NumWebVisitsMonth': "Number of visits to company’s web site in the last month"
    }
    return info[var]


def app():
    st.title('XCorp Customer Data')
    st.write('View customer data and statistics. Select 1 or 2 customer attributes below.')
    data = load()
    columns = [var for var in data.columns if var != 'Response']
    x = st.selectbox('X Variable', columns, index=0)
    y = st.selectbox('Y Variable (Optional)', [None] + [var for var in columns if var != x],
                     index=(len(columns)-1))
    st.plotly_chart(create_graph(data, x, y))
    st.write((x + ': ' + display_var_info(x)))
    if y:
        st.write((y + ': ' + display_var_info(y)))
    st.text(print_stats(data, x, y))