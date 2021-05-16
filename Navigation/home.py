import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

def test():
        
    st.title("Covid 19 Dashboard")



    ## Loading Data
    Whole_Data=pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
    Country_Vaccine=pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/locations.csv")
    GroupbyLocation=Whole_Data.groupby('location').last()
    Countries=Whole_Data.groupby('location',as_index=False).last()['location']
    

    ## Division of page
    col1=st.sidebar
    col2,col3=st.beta_columns((3,1))


    Select_Country=col1.selectbox("Select Country",Whole_Data.groupby('location',as_index=False).last()['location'],index=int(Countries[Countries=='World'].index[0]))

    #col2.text("In {} Stringency index is : {}".format(Select_Country,Whole_Data[Whole_Data['location']==Select_Country]['stringency_index'].max()))

    @st.cache
    def new_cases():
        return px.bar(data_frame=Whole_Data[Whole_Data['location']==Select_Country],x='date',y='new_cases',title="New Cases",labels={'new_cases':"New Cases","date":"Date"})
    col2.plotly_chart(new_cases())

    @st.cache
    def new_deaths():
        return px.bar(data_frame=Whole_Data[Whole_Data['location']==Select_Country],x='date',y='new_deaths',title="New Deaths",labels={'new_deaths':"New Deaths","date":"Date"},color_discrete_sequence=["red"])
    col3.plotly_chart(new_deaths())

    ## Need to check this
    @st.cache
    def new_test():
        return px.bar(data_frame=Whole_Data[~Whole_Data['continent'].isnull()].groupby('date')['new_tests'].sum().reset_index(),x='date',y='new_tests',title="New Tests",labels={'new_tests':"New Tests","date":"Date"},color_discrete_sequence=["green"])
    col2.plotly_chart(new_test())

    @st.cache
    def new_vaccines():
        return px.bar(data_frame=Whole_Data[Whole_Data['location']==Select_Country],x='date',y='new_vaccinations',title="New Vaccinations",labels={'new_vaccinations':"New Vaccinations","date":"Date"},color_discrete_sequence=["red"])
    col3.plotly_chart(new_vaccines())



    @st.cache
    def world_map():
        return px.scatter_geo(data_frame=GroupbyLocation[~GroupbyLocation['continent'].isnull()].fillna(0),locations='iso_code',color='continent',size='total_cases')
    col2.plotly_chart(world_map())

    @st.cache
    def continents():
        return px.bar(data_frame=GroupbyLocation.groupby('continent',as_index=False)[['total_cases']].sum(),x='continent',y='total_cases',color='continent')
    col3.plotly_chart(continents())

    Select_Continent=st.selectbox("Select Continent",list(Whole_Data['continent'].dropna().unique()),index=0)
    
    @st.cache
    def continents_country():
        GroupbyLocation=Whole_Data.groupby('location').last().reset_index()
        #GroupbyLocation=GroupbyLocation['continent'].dropna().unique()
        return px.bar(data_frame=GroupbyLocation[GroupbyLocation['continent']==Select_Continent],x='location',y='total_cases',hover_name='total_cases',title=Select_Continent,labels={'location':'Country','total_cases':"Total Cases"})
    st.plotly_chart(continents_country())


    #Select_Vaccine=col1.selectbox("Select Vaccine",pd.melt(Country_Vaccine['vaccines'].str.split(',',n = 6,expand=True),id_vars=0)[0].unique())

    @st.cache
    def Median_age():
        Whole_Data1=Whole_Data.copy(deep=True)
        Whole_Data1['AgeGroup']=np.where(Whole_Data1['median_age']>35,'Older',np.where(((Whole_Data1['median_age']>20) & (Whole_Data1['median_age']<35)),'Mid','Younger'))
        return px.bar(data_frame=Whole_Data1.groupby('location').last().reset_index(),x='location',y='total_deaths',color='AgeGroup',hover_name='median_age')

    st.plotly_chart(Median_age())





