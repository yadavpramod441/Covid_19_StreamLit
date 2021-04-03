import streamlit as st
import pandas as pd
import plotly.express as px


def test():
    st.set_page_config(layout="wide")
    st.title("India Covid Cases")

    India=pd.read_csv("https://api.covid19india.org/csv/latest/state_wise.csv")
    India.replace('Total','India',inplace=True)
    India_Selected_Column=India[['State','Confirmed','Recovered','Deaths','Active']]
    State=st.selectbox("Select State",India[['State']])

    col1,col2 = st.beta_columns((1,1))

    ### Column 1
    col1.header("Cumulative")

    IndianStatesDaily=pd.read_csv("https://api.covid19india.org/csv/latest/states.csv")
    col1.plotly_chart(px.line(data_frame=IndianStatesDaily[IndianStatesDaily['State']==State],x='Date',y='Confirmed',title=State))
    col1.plotly_chart(px.line(data_frame=IndianStatesDaily[IndianStatesDaily['State']==State],x='Date',y='Recovered',title=State))
    col1.plotly_chart(px.line(data_frame=IndianStatesDaily[IndianStatesDaily['State']==State],x='Date',y='Tested',title=State))
    col1.plotly_chart(px.line(data_frame=IndianStatesDaily[IndianStatesDaily['State']==State],x='Date',y='Deceased',title=State))



    ### Column 2
    col2.header("Daily")
    IndianStatesDaily=pd.read_csv("https://api.covid19india.org/csv/latest/states.csv")
    col2.plotly_chart(px.bar(data_frame=IndianStatesDaily[IndianStatesDaily['State']==State],x='Date',y='Confirmed',title=State))
    col2.plotly_chart(px.bar(data_frame=IndianStatesDaily[IndianStatesDaily['State']==State],x='Date',y='Recovered',title=State))
    col2.plotly_chart(px.bar(data_frame=IndianStatesDaily[IndianStatesDaily['State']==State],x='Date',y='Tested',title=State))
    col2.plotly_chart(px.bar(data_frame=IndianStatesDaily[IndianStatesDaily['State']==State],x='Date',y='Deceased',title=State))
