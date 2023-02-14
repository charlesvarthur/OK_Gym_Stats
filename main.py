################
# OK Gym Stats #
################

#Import modules
import streamlit as st
import pandas as pd
import altair as alt
import datetime as dt
import psycopg2
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL=DATABASE_URL.replace('postgres://', 'postgresql://',1)

engine = create_engine(DATABASE_URL)
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
conn.autocommit = True

db = scoped_session(sessionmaker(bind=engine))

def build():
    queries = ['Select version();','SELECT current_database();']
    outputs = []
    try:
        with conn.cursor() as cur:
            for qry in queries:
                cur.execute(qry)
                outputs.append(cur.fetchall())
            st.write(pd.DataFrame(outputs))
    except (Exception, psycopg2.DatabaseError) as error:
            st.write(error)
    finally:
            conn.close()

#Page display config
st.set_page_config(layout='wide')

#Header
st.header('OK Gym Stats')

#Opening blurb
st.write('This is a test page for OK GYM stats.')

#User data inputs
exercise = st.text_input("Exercise")
curdate = dt.datetime.today().strftime("%d-%m-%Y")
weight_kg = st.slider("Weight in KG", 0, 100)
reps = st.slider("Reps", 0, 50)
sets = st.slider("Sets", 0, 30)

#st.subheader('Build returns')
#build()


#Cache data for later
def insert_row():
    exercise_data = []
    exercise_data.append({'exercise_date': curdate, "exercise": exercise, "weight_kg": weight_kg, "reps": reps, "sets": sets})
    exercise_df = pd.DataFrame(exercise_data)
    st.write(exercise_df)
    try:
        exercise_df.to_sql(name="exercises", con=engine, if_exists='append', index=False, index_label='id')
    except (Exception, psycopg2.DatabaseError) as error:
        st.write(error)
    finally:
        db.commit()
        db.close()

if st.button("Add Data"):
    insert_row()