import os
import json
import numpy as np
import pandas as pd


df = pd.read_json('../data/result_edited.json')

df.drop(df.columns[[0, 4]], axis = 1, inplace = True)


df

#print(df.nunique())
#print(df.shape[1])


df.to_csv (r'export_dataframe.csv', index = False, header=True)


#################################################################################################


import os
import json
import numpy as np
import pandas as pd

df = pd.read_csv('../input/people-csv/Edu.Unifor.csv')

df.drop(df.iloc[:, 4:30], inplace = True, axis = 1)
#df.drop(df.iloc[:, 4:31], inplace = True, axis = 1)
df.drop(df.columns[[0, 2, 5, 7]], axis = 1, inplace = True)



df.head()

print(df.nunique())
print(df.shape[1])



df.to_csv (r'./export_dataframe.csv', index = False, header=True)




#df_Edu
#df_Goo
#df_Tel
#df_Yah