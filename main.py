from multiapp import MultiApp
from apps import homePage, clusterPage, customerPage, aboutPage


app = MultiApp()


# Add all your application here
app.add_app("Home", homePage.app)
app.add_app("Customer Data", customerPage.app)
app.add_app("Customer Clusters", clusterPage.app)
app.add_app("About", aboutPage.app)
# The main app
app.run()

