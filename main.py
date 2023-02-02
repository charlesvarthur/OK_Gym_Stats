################
# OK Gym Stats #
################

#Import modules
import streamlit as st
import pandas as pd
import altair as alt
import matplotlib as mp
import datetime as dt
import psycopg2 as pg

# Data Source
#stats_csv=pd.DataFrame('https://onedrive.live.com/Edit.aspx?resid=7AAF84FB66348F8!119&wd=cpe&authkey=!APLLMYlHMN-aTTQ')

@st.cache(allow_output_mutation=True)
def get_data():
    return []

#Page display config
st.set_page_config(layout='wide')

#Header
st.header('OK Gym Stats')

#Opening blurb
st.write('This is a test page for OK GYM stats.')

#User data inputs
exercise = st.text_input("Exercise")
curdate = dt.datetime.now()
weight_kg = st.slider("Weight in KG", 0, 100)
reps = st.slider("Reps", 0, 50)
sets = st.slider("Sets", 0, 30)

# Cache data for later
if st.button("Add Data"):
    get_data().append({'Date': curdate, "Exercise": exercise, "Weight": weight_kg, "Reps": reps, "Sets": sets})
    stats_df = pd.DataFrame(get_data())
    st.write(stats_df)

#Write the csv 
st.write(stats_df)