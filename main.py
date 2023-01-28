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

#Data Source
statistics = pd.DataFrame({
    'Date':[],
    'Exercise':[],
    'Weight':[],
    'Reps':[],
    'Sets':[]
})

#Page display config
st.set_page_config(layout='wide')

#Header
st.header('OK Gym Stats')

#Opening blurb
st.write('This is a test page for OK GYM stats.')

