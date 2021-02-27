import pandas as pd
import matplotlib.pyplot as plt

my_series = pd.Series([11.6, 21.1, -24.5, 322.0])
print(my_series)
print("\n\n")

# output in array form
print(my_series.values)
print("\n\n")

some_data ={'Set1': (9875, 56.7968, -5.077508),
            'Set2': (5525, 57.07115, -2.638262),
            'Set3': (5533, 57.00628, -2.728924),
            'Set4': (5555, 57.099211, -2.78042),
            'Set5': (5599, 57.033129, -2725616)
            }

dataframe = pd.DataFrame(some_data)
print(dataframe)
print("\n\n")

# another data set better organized 
some_data = {'Set Name': ['Set 1', 'Set 2', 'Set 3', 'Set 4', 'Set 5'],
            'Attribute1': [1111, 2254, 2114, 1332, 2001],
            'Attribute2': [56.78945, 88.070453, 44.099428, 59.002611, 54.077499],
            'Attribute3': [-51.003228, -31.62262, -31.72224, -31.72242, -31.225416]
            }

dataframe = pd.DataFrame(some_data)
print(dataframe)
print("\n\n")

##################################################

# first n items 
print(dataframe.head(3))
print("\n\n")

# last n items 
tail = print(dataframe.tail(2))
print(tail)
print("\n\n")

# access by index (like an array)
# print(dataframe[0]) # will not work 
# instead we have to do this:

print(dataframe.iloc[0]) # set 1
print(dataframe.iloc[0,2]) 
print("\n\n")

# other approaches to access data 
print(dataframe['Set Name'][0]) # returns set 1
print("\n\n")

# access by attribute
# be careful when using attributes with spaces

print(dataframe.Attribute1)
print("\n\n")

print(dataframe.Attribute1 > 2000)
print("\n\n")

# append some data (adding a new attrivute)
dataframe['New Attribute'] = ['Something1', 'Something2', 'Something3', 'Something4', 'Something5']
print(dataframe)
print("\n\n")

#sort dataframe 
sorted_data = dataframe.sort_values(by = ['Attribute2'], ascending = False)
print(sorted_data.head(4)) # want first 4 of outputs 
print("\n\n")

###################################################################################

# PLOT DATA 
x = dataframe.Attribute1
y = dataframe.Attribute2

plt.scatter(x,y)
plt.savefig("chart.png")
plt.show()

# SHOW NEEDS TO BE AFTER THE SAVE 