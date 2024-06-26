# Pandas is a Python library used for working with data sets
# It has functions for analyzing, cleaning, exploring, and manipulating data
import pandas as pd

my_data = {
    'cars' : ['BMW',"Thar",'honda','farari'],
    'passing' : [1,2,3,4]
}

myvar = pd.DataFrame(my_data)
print(myvar)

print("pandas version : ",pd.__version__)