import streamlit as st
from streamlit_option_menu import option_menu as om   
import pandas as pd


with st.sidebar:
    selected = om(menu_title = "Main Menu",
                  options = ["Home", 'Graphs','Project','Contribute'] 
        )

if selected=='Home':
    st.title('Hello Word')


if selected =='Graphs':
    pass

if selected =='Project':
    pass

if selected =='Contribute':
    pass