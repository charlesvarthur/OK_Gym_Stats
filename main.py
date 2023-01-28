################
# OK Gym Stats #
################

#Import modules
import streamlit as st
from st_aggrid import AgGrid as aG
import pandas as pd
import numpy as np
import altair as alt
import matplotlib as mp
import datetime as dt

# #Data Source
# statistics = pd.DataFrame({
#     'Date':[],
#     'Exercise':[],
#     'Weight':[],
#     'Reps':[],
#     'Sets':[]
# })

statistics = []

@st.cache(allow_output_mutation=True)
def get_data():
    return statistics

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


if st.button("Add Data"):
    get_data().append({'Date': curdate, "Exercise": exercise, "Weight": weight_kg, "Reps": reps, "Sets": sets}, ignore_index=True)

st.write(pd.DataFrame(get_data()))