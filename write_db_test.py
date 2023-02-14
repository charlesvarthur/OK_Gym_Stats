####################
# write to db test #
####################

import psycopg2
import os
import pandas as pd
import datetime as dt
from sqlalchemy import create_engine

DATABASE_URL = "dbname=ok_gym_stats user=ok_admin password=ok_admin port=5433"
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
conn.autocommit = True
engine=create_engine("postgresql+psycopg2://ok_admin:ok_admin@localhost:5433/ok_gym_stats")

def build():
    queries = ['Select version();','SELECT current_database();']
    outputs = []
    try:
        with conn.cursor() as cur:
            for qry in queries:
                cur.execute(qry)
                outputs.append(cur.fetchall())
            print(pd.DataFrame(outputs))
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
            conn. close()

#User data inputs
exercise = "Arms"
curdate = dt.datetime.today().strftime("%d-%m-%Y")
weight_kg = 10
reps = 30
sets = 40



#Cache data for later
def insert_row():
    exercise_data = []
    exercise_data.append({'exercise_date': curdate, "exercise": exercise, "weight_kg": weight_kg, "reps": reps, "sets": sets})
    exercise_df = pd.DataFrame(exercise_data)
    print(exercise_df)
    sql = ('Insert Into exercise (exercise_date, exercise, weight_kg, reps, sets) VALUES (%s,%s,%d,%d,%d)' 
            % (exercise_df['exercise_date'], exercise_df['exercise'], exercise_df['weight_kg'], exercise_df['reps'], exercise_df['sets']))
    try:
        exercise_df.to_sql(name="exercises", con=engine, if_exists='append', index=False, index_label='id')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.commit()
        conn.close()



#build()
insert_row()