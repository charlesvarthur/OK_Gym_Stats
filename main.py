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

DATABASE_URL = os.environ.get('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

def build():
    queries = ['Select version();','SELECT current_database();', '''CREATE TABLE IF NOT EXISTS exercises (
                id serial PRIMARY KEY,
                exercise varchar(50) NOT NULL,
                reps integer NOT NULL,
                sets integer NOT NULL,
                weight_kg integer NOT NULL,
                exercise_date date
                )      
                ''']
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





#Function to read the database ini file and verify that the section for postgresql exists local solution. 
# @st.experimental_singleton
# def pg_config():
#     return psycopg2.connect(**st.secrets["postgresql"])

# conn = pg_config()

# def run_query(query):
#     try:
#         with conn.cursor() as cur:
#             cur.execute(query)
#             return cur.fetchall()
#     except (Exception, psycopg2.DatabaseError) as error:
#             print(error)
#     finally:
#             conn.close()
#             print('Database connection closed.')           
            

# get_pgversion = run_query("Select version()")
# st.write(get_pgversion)

#Run a test connection for PostgreSQL and return the version data. 
# def data_insert():
#     """ Connect to the PostgreSQL database server """
#     conn = None
#     try:
#         # read connection parameters
#         # connect to the PostgreSQL server
#         print('Connecting to the PostgreSQL database...')
#         # create a cursor
#         cur = conn.cursor()
# 	# Insert Values
#         cur.execute("INSERT INTO exercises (col1, col2) VALUES (%s, %s, %s, %s, %s)", (curdate,exercise,weight_kg,reps,sets))
       
# 	# close the communication with the PostgreSQL
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')

# #Data Input and DB Write
# @st.cache(allow_output_mutation=True)
# def get_data():
#     return []

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

st.subheader('Build returns')
build()



# Cache data for later
# if st.button("Add Data"):
#     get_data().append({'Date': curdate, "Exercise": exercise, "Weight": weight_kg, "Reps": reps, "Sets": sets})
#     stats_df = pd.DataFrame(get_data())
#     if __name__ == '__main__':
#        data_insert()