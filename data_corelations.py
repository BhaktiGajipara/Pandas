import pandas as pd

# The corr() method calculates the relationship between each column in your data set.
data = pd.read_csv("pandas/data.csv")
print(data,"\n")
print(data.corr())
# The corr() method ignores "not numeric" columns
# The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.
# number varies from -1 to 1.
