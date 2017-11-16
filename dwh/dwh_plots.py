# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 13:09:20 2017

@author: ksagilop
"""
''' MODULES '''
import os
import collections
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

''' PATH & FILES '''
if os.name == 'nt':
    work_folder = 'C:\ZHAW\dwh\plot\\' 
    
csv_files = ['profit_category.csv', 
             '']

''' DATAFRAMES & PLOTS '''

''' Profit by Category '''
dfa = pd.read_csv((work_folder + csv_files[0]), sep=',',  encoding='utf-8',
                   usecols=['CategoryName', 'Profit_Category'])

def profitCat():
    print(dfa)
    # Size and labels
    cat = list(dfa['CategoryName'])
    profit_cat = list(dfa['Profit_Category'])
    # Pie plot
    profot_cat_file = work_folder + 'profit_cat' + '.png'
    plt.figure(figsize=(5, 5))
    plt.title('Umsatz pro Produktekategorien')
    plt.axis('equal')
    plt.pie(profit_cat, labels=cat, autopct='%1.1f%%')
    plt.savefig(profot_cat_file, dpi=600, bbox_inches='tight')
    plt.show()

#profitCat()
    
plt.rcdefaults()
fig, ax = plt.subplots()

# Top 10 profit per product
# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = (2,3,5,6,1)

ax.barh(y_pos, performance, align='center',
        color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()