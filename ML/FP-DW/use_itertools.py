import itertools as it
import pandas as pd

# You can use this instead of a nested loop
for i, j, k in it.product(range(4), range(5), range(3, 7)):
  print(i, j , k)
  
# Generate a Cartesian product of several lists to populate a data frame from a source dictionary.
# You can use the same construct for generating both data and multi-index.
index_dict = {'First': ['A', 'B', 'C', 'D'], 'Second': ['I', 'II'], 'Third': ['1', '2', '3']}
grid_index = pd.MultiIndex.from_tuples(it.product(*index_dict.values()), names=index_dict.keys())

source_dict = {'Name': ['John', 'Jack', 'Adam', 'Mehdi', 'David', 'Ariel'], 'Age': [20, 30, 40, 50]}
grid_dataframe = pd.DataFrame.from_records(it.product(*source_dict.values()), columns=source_dict.keys(), index=grid_index)
# grid_dataframe.set_index(grid_index, inplace=True)

print(grid_dataframe)