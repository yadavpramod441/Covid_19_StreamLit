
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Covid 19 Vaccination Dashboard")
st.write("Countries which is infected by Corona Cases")
Whole_Data=pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
Country_Vaccine=pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/locations.csv")

@st.cache
def load_data():
    #Whole_Data.groupby('location').last()['']
    #print(Whole_Data['location'].nunique())
    return Whole_Data[~Whole_Data['continent'].isnull()].groupby('location').last().reset_index()[['location','date','new_cases','new_deaths','new_tests','new_vaccinations']].fillna(0)
st.write("Number of Countries Infected by Corona",load_data()['location'].nunique())
st.write("Number of Countries Using Vaccines",Country_Vaccine['location'].nunique())
st.write("Number of Vaccines in market",pd.melt(Country_Vaccine['vaccines'].str.split(',',n = 6,expand=True),id_vars=0)[0].nunique())
st.write("Daily Cases:")
st.dataframe(load_data())
add_selectbox = st.sidebar.selectbox(
    "Select Country",load_data()['location']
    )


@st.cache
def continent():
    GroupbyLocation=Whole_Data.groupby('location').last()
    return px.bar(data_frame=GroupbyLocation.groupby('continent',as_index=False)[['total_cases']].sum(),x='continent',y='total_cases',color='continent')
st.plotly_chart(continent())
