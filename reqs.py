import requests
import pandas as pd
url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
res=requests.get(url)
token=res.json()
token_data=pd.DataFrame(token)
token_data.to_csv("angel.csv")
t=pd.read_csv("angel.csv",low_memory=False)
t.drop(columns=['Unnamed: 0'], inplace=True)
print(t['instrumenttype'].isna())