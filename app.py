
import streamlit as st
import pandas as pd
from Navigation import home,vaccines,india,about,important_links
PAGES = {
    "Home": home,
    "Vaccines": vaccines,
    "India": india,
    "About Us":about,
    "Important Links":important_links
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.test()
