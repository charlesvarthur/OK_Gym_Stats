########################
# Bingo card generator #
# Charles Arthur       #
# 11-08-2023           #
########################

import random as rand
import pandas as pd
import os

staging_directory = "/Users/charlesarthur/Desktop/"
file_name = "excellent_bingo_gen.csv"

if os.path.isfile(staging_directory + file_name):
    os.remove(staging_directory + file_name)
else:
    count = 0 
    while count < 200:
        #Generate 5 sets of numbers, between 1 and 75
        num_gen = []
        num_gen = rand.sample(range(1, 75), 25)

        #Pre sort and check for the data output with no duplicates
        num_gen.sort()
        pre_fr = [[num_gen[0:5]],[num_gen[5:10]],[num_gen[10:15]],[num_gen[15:20]],[num_gen[20:25]]]
        # print(pre_fr)

        #Import the data into a standard dataframe and check the output:
        grid = pd.DataFrame(pre_fr)
        grid.to_csv(staging_directory + file_name, mode='a', index=False, header=False)

        count +=1

    print("File " +staging_directory + file_name + " has successfully been created")