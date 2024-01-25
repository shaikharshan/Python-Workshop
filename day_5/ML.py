import numpy as np
import pandas as pd
#data plot
#labelled data ->already available
data=pd.read_csv()
# data.head(n) displays first in values
data.shape
# gives size of data,rows and columns
print(type(data))
#type  DataFrame
data.info()
# gives information about data
data.describe()
# gives mean ,sd,min max etc about data
data.isnull().sum()
#sums no. of null values 

# confusion matrix -> true positive,tn,fp,fn