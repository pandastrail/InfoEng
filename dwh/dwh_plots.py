# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 13:09:20 2017

@author: ksagilop
"""
''' MODULES '''
import os
import collections
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

''' PATH & FILES '''
if os.name == 'nt':
    work_folder = 'C:\ZHAW\dwh\plot\\' 
    
csv_files = ['profit_category.csv', 
             'profit_product.csv']

''' DATAFRAMES & PLOTS '''

''' Profit by Category '''
dfa = pd.read_csv((work_folder + csv_files[0]), sep=',',  encoding='utf-8',
                   usecols=['CategoryName', 'Profit_Category'])
dfb = pd.read_csv((work_folder + csv_files[1]), sep=',',  encoding='utf-8')


''' Profit by Category '''
def profitCat():
    print(dfa)
    print(dfa.describe())
    # Label and color of slice
    categories = list(dfa['CategoryName'])
    colors = []
    for cat in categories:
        if cat == 'Beverages':
            colors.append('C0')
        elif cat == 'Meat/Poultry':
            colors.append('C1')
        elif cat == 'Confections':
            colors.append('C2')
        elif cat == 'Grains/Cereals':
            colors.append('C3')
        elif cat == 'Produce':
            colors.append('C4')
        elif cat == 'Dairy Products':
            colors.append('C5')
        elif cat == 'Seafood':
            colors.append('C6')
        elif cat == 'Condiments':
            colors.append('C7')
    print(colors)
    # Size of slice
    profit_cat = list(dfa['Profit_Category'])
    # Pie plot
    profit_cat_file = work_folder + 'profit_cat' + '.png'
    plt.figure(figsize=(5, 5))
    plt.title('Umsatz pro Produktekategorien')
    plt.axis('equal')
    plt.pie(profit_cat, 
            labels=categories, 
            explode=(0.1,0,0.05,0,0,0,0,0),
            autopct='%1.1f%%',
            colors=colors)
    plt.savefig(profit_cat_file, dpi=600, bbox_inches='tight')
    plt.show()

#profitCat()

''' Profit by Product '''
def profitPro():
    # Number of top products to retrieve, in this case 13    
    dfba = dfb.loc[0:12]
    # Hos much profit in % do these products make?
    print(dfba['Profit_Percentage'].cumsum())
    print(dfba)
    plt.rcdefaults()
    fig, ax = plt.subplots()
    # Label and ticks
    products = list(dfba['ProductName'])
    y_pos = np.arange(len(products))
    # Size of bar
    profit_product = list(dfba['Profit_Product'])
    # Color of bar
    colors = []
    categories = list(dfba['CategoryName'])
    for cat in categories:
        if cat == 'Beverages':
            colors.append('C0')
        elif cat == 'Meat/Poultry':
            colors.append('C1')
        elif cat == 'Confections':
            colors.append('C2')
        elif cat == 'Grains/Cereals':
            colors.append('C3')
        elif cat == 'Produce':
            colors.append('C4')
        elif cat == 'Dairy Products':
            colors.append('C5')
        elif cat == 'Seafood':
            colors.append('C6')
        elif cat == 'Condiments':
            colors.append('C7')
    # Bar plot
    ax.barh(y_pos, 
        profit_product, 
        align='center',
        color=colors, 
        ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(products)
    ax.text(120000, 0, '11.30 %', fontsize=8)
    ax.text(120000, 1, '6.61 %', fontsize=8)
    ax.text(120000, 2, '5.75 %', fontsize=8)
    ax.text(120000, 3, '3.75 %', fontsize=8)
    ax.text(120000, 4, '3.60 %', fontsize=8)
    ax.text(120000, 5, '3.40 %', fontsize=8)
    ax.text(120000, 6, '3.27 %', fontsize=8)
    ax.text(120000, 7, '2.63 %', fontsize=8)
    ax.text(120000, 8, '2.41 %', fontsize=8)
    ax.text(120000, 9, '1.93 %', fontsize=8)
    ax.text(120000, 10, '1.83 %', fontsize=8)
    ax.text(120000, 11, '1.77 %', fontsize=8)
    ax.text(120000, 12, '1.76 %', fontsize=8)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Umsatz ($)')
    ax.set_title('Umsatz Top 13 Produkte, 50% von Umsatz')
    profit_pro_file = work_folder + 'profit_pro' + '.png'
    plt.savefig(profit_pro_file, dpi=600, bbox_inches='tight')
    plt.show()
    
#profitPro()

''' Orders sales development over time '''
# Each point on the scatter is an order?
# Or each point is a product?
x = (1,2,3,4,5,6,2) # Time line over x-axis
y = (10,20,30,40,50,60,35) # Profit for the order or category?
colors = (1,2,3,4,5,6,2) # Which dimension?
area = (100,200,300,400,500,600) # Which dimension?
# One type of marker per set, see matplotlib.markers.MarkerStyle
# One scatter set per category with a different marker
x_pos = np.arange(1,len(x))
x_months = ['ene', 'feb', 'mar', 'abr', 'may', 'jun']
# xticks( arange(12), calendar.month_name[1:13], rotation=17 )

fig, ax = plt.subplots()
ax.scatter(x, 
            y,
            s=area,
            c=colors,
            cmap='BuPu',
            alpha=0.8,
            marker='v',
            label="Cat 1")

plt.scatter(x, 
            y=(20,30,40,50,60,80,10),
            s=area,
            c=colors,
            cmap='BuPu',
            alpha=0.8,
            marker='o',
            label="Cat 2")
ax.set_xticks(x_pos)
ax.set_xticklabels(x_months)
ax.set_xlabel("Label over the x-axis")
ax.set_ylabel("Label over y-axis")
ax.set_title('Tituloooo')
plt.legend()
plt.show()

# Marker = Category
# Color = Discount
# Area = Quantity
# y = Profit pro Product
# x = month
# Shipped Product Profit over a month period

