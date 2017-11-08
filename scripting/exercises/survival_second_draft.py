
# coding: utf-8

# # Use pandas to generate a key;value file to submit to the leaderboard
# ## First use a pure Gender based probability approach, where all females will survive

# Import modules needed

from pandas import Series, DataFrame
import pandas as pd

# Define path to working csv files, input and output
f = r'/home/hase/Documents/ZHAW/InfoEng/Lectures/Scripting/data/titanic3_test.csv'
fo = r'/home/hase/Documents/ZHAW/InfoEng/Lectures/Scripting/data/submit/titanic3_test_gender.csv'

# Create a dataframe from the csv file
# delimiter is ';', set index to be the 'id', and use only the columns 'id' and 'sex'
df = pd.read_csv(f, sep=';', index_col='id', usecols=['id', 'sex'])
df.head()  # Get the first five rows of the dataframe

# Add a new column named "survived"
# Create a lambda function to pass the logic to the new column on the dataframe
def gender(row):
    if row['sex'] == 'female':
        return 1
    else:
        return 0

# Then, apply the lambda function created to a new column "survived"
df['survived'] = df.apply(lambda row: gender(row),axis=1)  # axis=1 means it applies to a row level
# Needs to be lambda to a pass a function to df.apply?

df.drop('sex', axis=1, inplace=True)   # axis=1 means column-wise, and inplace=True does operation in place
# #### Rename index and column to comply the format to be submitted
df.index.name = 'key'
df.rename(columns={'survived':'value'}, inplace=True)
print(df.head())

# #### Done with indexing, from this point, create a new csv file for gender based probability and submit
df.to_csv(fo, sep=';')

# ### Result on the leaderboard (https://openwhisk.ng.bluemix.net/api/v1/web/ZHAW%20ISPROT_ISPROT17/default/titanic.html)
# #### test_gender_based_28102017 → 0.7777777777777778