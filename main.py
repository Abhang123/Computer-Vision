import streamlit as st

from streamlit_option_menu import option_menu

import about, capture_and_analyze, account, your_activites

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Quality Analysis',
                options=['Capture and Analyze','Account','Your Activitiess','About'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill','chat-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
                    "icon": {"color": "white", "font-size": "23px"}, 
                    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        

        if app == "Account":
            account.app()           
        if app == 'About':
            about.app()
        if app == 'Capture and Analyze':
            capture_and_analyze.app()
        if app == 'Your Activities':
            your_activites.app()    
             
          
             
    run() 