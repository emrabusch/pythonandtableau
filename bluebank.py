# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:32:48 2024

@author: erabu
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
#json_file = open('loan_data_json.json')
#data = json.load(json_file)
data = json.load(open('loan_data_json.json'))

#method 2 to read json data
#with open('loan_data_json.json') as json_file:
#    data= json.load(json_file)

#transorm to dataframe
loandata = pd.DataFrame(data)

#finding unique values for the purpose column
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe the data for a specified column
loandata['fico'].describe()

#using EXP() to get the annual income
loandata['annualincome'] = np.exp(loandata['log.annual.inc'])

#FICO score category
# for x in range(0, len(loandata)):
#     if loandata['fico'][x] >= 300 and loandata['fico'][x] < 400:
#         loandata['ficoCat'][x] = 'Very Poor'
#     elif loandata['fico'][x] >= 400 and loandata['fico'][x] < 600:
#         loandata['ficoCat'][x] = 'Poor'
#     elif loandata['fico'][x] >= 600 and loandata['fico'][x] < 660:
#         loandata['ficoCat'][x] = 'Fair'
#     elif loandata['fico'][x] >= 660 and loandata['fico'][x] < 780:
#         loandata['ficoCat'][x] = 'Good'
#     elif loandata['fico'][x] >= 780:
#         loandata['ficoCat'][x] = 'Excellent'
#     else:
#         loandata['ficoCat'][x] = 'Unknown'

ficocat = []
for x in range(0, len(loandata)):
    category = loandata['fico'][x]
    
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 600 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 780:
            cat = 'Good'
        elif category >= 780:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Error'
    ficocat.append(cat)

ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat

#df.loc as conditional statements
# df.loc[df[columnname] condition, newcolumnname] = 'value if the condition is met'

#for interest rates, a new column is wanted
loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

#number of loans/rows by fico.category
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.1)
plt.show()

#scatter plots
ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = '#4caf50')
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv', index = True)












