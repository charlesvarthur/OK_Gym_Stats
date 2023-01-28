################
# OK Gym Stats #
################

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib as mp

statistics = pd.DataFrame({
    'Date':[],
    'Exercise':[],
    'Weight':[],
    'Reps':[],
    'Sets':[]
})

st.set_page_config(layout='wide')

st.header('OK Gym Stats')

st.write('This is a test page for OK GYM stats.')