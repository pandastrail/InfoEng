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
# No index_col to retrieve all columns
# Import with dtype 'str' as needed to get unique values; i.e. all primary keys or ID's
# Remove columns as needed, for example, Photo on 'Employees'
dfca = pd.read_csv((work_folder + csv_files[0]), sep=';',  encoding='utf-8',
                    dtype={'CategoryID':'str'})
dfcu = pd.read_csv((work_folder + csv_files[1]), sep=';', encoding='utf-8',
                    dtype={'CustomerID':'str'})
dfpr = pd.read_csv((work_folder + csv_files[2]), sep=';', encoding='utf-8',
                    dtype={'ProductID':'str', 'SupplierID':'str', 'CategoryID':'str'})
dfor = pd.read_csv((work_folder + csv_files[3]), sep=';', encoding='latin-1',
                    dtype={'OrderID':'str', 'EmployeeID':'str'})  # encoding 'utf-8' did not worked!
dfod = pd.read_csv((work_folder + csv_files[4]), sep=';', encoding='utf-8',
                    dtype={'OrderID':'str', 'ProductID':'str'})
dfem = pd.read_csv((work_folder + csv_files[5]), sep=';', encoding='utf-8',
                    usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13],
                    dtype={'EmployeeID':'str'})

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


