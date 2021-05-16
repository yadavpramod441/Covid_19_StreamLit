import streamlit as st
import pandas as pd
import plotly.express as px

Vaccine=pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/locations.csv")
s=Vaccine.apply(lambda x: pd.Series(x['vaccines'].split(',')),axis=1).stack().reset_index(level=1, drop=True)
s.name='vaccine'
a=Vaccine.drop('vaccines',axis=1).join(s)
a['vaccine']=a['vaccine'].apply(lambda x : x.strip())
a=a.groupby(by=['vaccine','location','iso_code'],as_index=False)['source_website'].count()

def test():
    st.write("Vaccine Page")
    #vaccine_selected=st.selectbox("Select Vaccine",a['vaccine'].value_counts().index,index=0)
    st.dataframe(data=a.groupby(by='vaccine',as_index=False)['location'].count().rename(columns={'location':'Countries Using'}))


    @st.cache
    def vaccine_map():
        return px.scatter_geo(data_frame=a,locations='iso_code',color='vaccine',hover_data=['location'])
    st.plotly_chart(vaccine_map())
