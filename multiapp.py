"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
import os

class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })
    
    def setup(self):
        folder = 'items'
        img = 'favicon-32x32.png'
        favicon_path = os.path.join(folder, img)
        st.set_page_config("XCorp Marketing Dashboard", page_icon=favicon_path,
                           initial_sidebar_state='expanded')

    def run(self):
        self.setup()
        app = st.sidebar.radio(
        #app = st.selectbox(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()
