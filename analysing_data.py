# Viewing the Data
# The head() method returns the headers and a specified number of rows, starting from the top.

import pandas as pd

data = pd.read_csv("pandas/data.csv")
print("top 10 data :\n",data.head(10))

# mber of rows is not specified, the head() method will return the top 5 rows

# The tail() method returns the headers and a specified number of rows, starting from the bottom
print("last 10 data :\n",data.tail(10),"\n")

# The DataFrames object has a method called info(), that gives you more information about the data set.
# The info() method also tells us how many Non-Null values there are present in each column
print(data.info())
