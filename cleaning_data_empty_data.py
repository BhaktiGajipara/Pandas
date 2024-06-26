# Data cleaning means fixing bad data in your data set.
# Empty cells
# Data in wrong format
# Wrong data
# Duplicates

# Empty Cells   //Empty cells can potentially give you a wrong result when you analyze data

# ///1-remove rows
# By default, the dropna() method returns a new DataFrame, and will not change the original.
import pandas as pd

data = pd.read_csv("pandas/data1.csv")
print(data)
new_data = data.dropna()
print(new_data,"\n")
print(data,"\n")
# If you want to change the original DataFrame, use the inplace = True argument
#  the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.
# data.dropna(inplace=True)
# print(data,"\n")

# ///2-Another way of dealing with empty cells is to insert a new value instead.
# The fillna() method allows us to replace empty cells with a value:

# data.fillna(130,inplace=True)
# print(data)


# Replace Only For Specified Columns  //To only replace empty values for one column, specify the column name for the DataFrame
# data['Calories'].fillna(130,inplace=True)
# print(data)


# ///3- Replace Using Mean, Median, or Mode
# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column
x = data["Calories"].mean()
# data['Calories'].fillna(x,inplace=True)
# print(data)
# print(x)

y = data["Calories"].median()
data["Calories"].fillna(y,inplace=True)
print(data)
print(y)
# similarly for mode
y = data["Calories"].mod()