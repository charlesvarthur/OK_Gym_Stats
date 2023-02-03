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
from configparser import ConfigParser, Error
import config


#Function to read the database ini file and verify that the section for postgresql exists. 
def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

#Run a test connection for PostgreSQL and return the version data. 
def data_insert():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = pg.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# Insert Values
        cur.execute("INSERT INTO exercises (col1, col2) VALUES (%s, %s, %s, %s, %s)", (curdate,exercise,weight_kg,reps,sets))
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, pg.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

#Data Input and DB Write
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
    if __name__ == '__main__':
       data_insert()

#Write the csv 
st.write(stats_df)