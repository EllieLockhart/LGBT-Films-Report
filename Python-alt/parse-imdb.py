import os
import pandas as pd
import numpy as np
import sklearn

#set pandas formatting parameters
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 25)

#read in the data tables provided
showbiz_core = pd.read_table("name.basics.tsv",sep='\t')

#temporary hack - print the entire dataframe as test
print(showbiz_core)
