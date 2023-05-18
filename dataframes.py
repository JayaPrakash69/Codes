import pandas as pd
import numpy as np
lst=[["tata",1,2,3,4],["infos",5,6,7,8]]
df=pd.DataFrame(lst)
print(df)
df.columns=['stock','open','low','high','close']
df.index=['t','i']
print(df)
df['average']=(df['low']+df['high'])/2
print(df)
df['range']=df['low']-df['high']
print(df)
print(df['high']['i'])