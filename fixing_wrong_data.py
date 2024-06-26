import pandas as pd

# Replacing Values
data = pd.read_csv("pandas/data1.csv")
print(data,"\n")
# data.loc[7,"Duration"] = 45
# print(data)

# For small data sets you might be able to replace the wrong data one by one, but not for big data sets
for x in data.index:
    if data.loc[x,"Duration"] > 120:
        data.loc[x,"Duration"] = 120

print(data)

#  ///another way is to remove methods using dropna() methods
for x in data.index:
    if data.loc[x,"Duration"] > 120:
        data.drop(x,inplace = True)
