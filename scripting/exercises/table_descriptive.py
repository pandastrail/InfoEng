# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:56:19 2017

@author: ksagilop

Basic descriptive statistics of data contained in tables 
"""

''' MODULES '''
import os
import collections
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

''' PATH & FILES '''
if os.name == 'nt':
    work_folder = 'C:\ZHAW\dwh\\' 
    
csv_files = ['Categories.csv', 
             'Customers.csv', 
             'Products.csv', 
             'Orders.csv', 
             'OrderDetails.csv', 
             'Employees.csv']

''' DATAFRAMES '''
dfca = pd.read_csv((work_folder + csv_files[0]), sep=';', index_col='CategoryID', encoding='utf-8')
dfcu = pd.read_csv((work_folder + csv_files[1]), sep=';', index_col='CustomerID', encoding='utf-8')
dfpr = pd.read_csv((work_folder + csv_files[2]), sep=';', index_col='ProductID', encoding='utf-8')
dfor = pd.read_csv((work_folder + csv_files[3]), sep=';', index_col='OrderID', encoding='latin-1')  # encoding 'utf-8' did not worked!
dfod = pd.read_csv((work_folder + csv_files[4]), sep=';', index_col='OrderID', encoding='utf-8')
dfem = pd.read_csv((work_folder + csv_files[5]), sep=';', index_col='EmployeeID', encoding='utf-8')

''' FUNCTIONS '''
def describeDF(df, table_name):
    '''Plot the count, unique and missing values of a dataframe'''
    # Create objects
    #df = df.astype(str)                # Convert all columns astype string
    desc = df.describe(include='all')   # Get descriptive stats for each column
    #print(desc)
    #print(desc.shape)
    size = len(df)                      # Number of rows on table
    cols = list(df.columns)             # Column labels
    nrows, ncols = df.shape             # Number of rows and columns
    values = ([])                       # Placeholder for values
    # Iterate over all columns and get values
    for col in range(len(cols)):
        #print(col)
        count = int(desc.iloc[:1, col])
        missing = size - count
        try:
            unique = int(desc.iloc[1:2, col])
            heat = [count, unique, missing]
            values.append(heat)
        except:
            heat = [count, -1, missing]
            print(cols[col], 'not an object type, unique is NaN')
            values.append(heat)
    # Build and show plot for the dataframe provided
    plt.figure(figsize=(8,6))
    x = ['count', 'unique', 'missing']
    ax = sns.heatmap(values, 
                 annot=True,
                 fmt='g',
                 linewidths=True,
                 yticklabels=cols, 
                 xticklabels=x,
                 cmap='Blues'
                 )
    plt.yticks(rotation=0) 
    header = ('Table ' + table_name + 
              '\nrows: ' + str(nrows) + ', columns: ' + str(ncols))
    ax.set_title(header)
    ax.set_ylabel('Columns')
    fig_file = work_folder + table_name + '.png'
    plt.tight_layout()
    plt.savefig(fig_file, dpi=600)
    plt.show()


''' EXECUTE '''
describeDF(dfca, table_name='Categories')
describeDF(dfcu, table_name='Customers')
describeDF(dfpr, table_name='Products')
describeDF(dfor, table_name='Orders')
describeDF(dfod, table_name='OrderDetails')
describeDF(dfem, table_name='Employees')

