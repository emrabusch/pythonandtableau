# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 13:55:14 2024

@author: erabu
"""

import pandas as pd

#file_name = pd.read_csv('file.csv') <--- format of read_csv
data = pd.read_csv('transaction2.csv')
data = pd.read_csv('transaction2.csv', sep=';')

#summary of the data
data.info()

#working with calculations
#Defining variables
#   CostPerItem = 11.73
#   SellingPricePerItem = 21.11
#   NumberOfItemsPurchased = 6

#Mathmatical Operations on Tableau
#   ProfitPerItem = SellingPricePerItem - CostPerItem
#   ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
#   CostPerTransaction = NumberOfItemsPurchased * CostPerItem
#   SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem

#CostPerTransaction column calculation
#   variable = dataframe['column_name']
#   CostPerItem = data['CostPerItem']
#   NumberOfItemsPurchased = data['NumberOfItemsPurchased']
#   CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#adding a new column to a dataFrame
#   data['CostPerTransaction'] = CostPerTransaction
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales per Transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit = sales - cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (sales - cost)/cost
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']
data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction']

#Rounding Markup
#   roundMarkup = round(data['Markup'], 2)
data['Markup'] = round(data['Markup'],2)

#combining data fields
#this won't work because day and year are int64 not strings
# data['Date'] = data['Day'] + '-' + data['Month'] + '-' + data['Year']

#checking columns data type
print(data['Day'].dtype)

#Change columns type
data['Date'] = data['Day'].astype(str) + '-' + data['Month'] + '-' + data['Year'].astype(str)

#using iloc to view specific columns/rows
data.iloc[0] #views the row with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) #first 5 rows

data.iloc[:,2] #all rows, column at index = 2
data.iloc[4,2] #4th row and 2nd column

#split and replace functions
splitCol = data['ClientKeywords'].str.split(',', expand = True)
data['ClientAge'] = splitCol[0].str.replace('[', '')
data['ClientType'] = splitCol[1]
data['LengthOfContract'] = splitCol[2].str.replace(']', '')

#using the lower function to change text to lower case
data['ItemDescription'] = data['ItemDescription'].str.lower()

#merge files
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')
data = pd.merge(data, seasons, on = 'Month')

#dropping columns
data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Month', 'Year'], axis = 1)

#exporting to csv
data.to_csv('ValueInc_Cleaned.csv', index = False)
















