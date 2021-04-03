
import streamlit as st
import pandas as pd
from Navigation import home,vaccines,india
PAGES = {
    "Home": home,
    "Vaccines": vaccines,
    "India": india
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.test()
