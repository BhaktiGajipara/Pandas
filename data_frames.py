# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.
import pandas as pd

data = {"data" : ["data1","data2","data3","data4","data5"],"value" :[22,11,44,33,66]}
var = pd.DataFrame(data)
print(var,"\n")


# Locate Row
# Pandas use the loc attribute to return one or more specified row(s)
print(var.loc[0],"\n")
# return multiple rows
print(var.loc[[1,2]],"\n")

# Named index

# With the index argument, you can name your own indexes
var1 = pd.DataFrame(data,index=["11","22","33","44","55"])
print(var1,"\n")

# Locate Named Indexes
# Use the named index in the loc attribute to return the specified row(s)
print(var1.loc["11"])
