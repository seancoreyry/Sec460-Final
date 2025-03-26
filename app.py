import streamlit as st
st.set_page_config(

    page_title='Home Page',
    layout='centered',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://streamlit.io/',
        'Report a bug': 'https://github.com',
        'About': 'About your application: **Seans First App**'
        }
)
st.sidebar.title('Home Page')
st.title('Welcome to Seans App for the Sec460 Final!')
