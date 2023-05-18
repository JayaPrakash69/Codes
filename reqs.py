import requests
import pandas as pd
url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
res=requests.get(url)
token=res.json()
token_data=pd.DataFrame(token)
print(token_data['instrumenttype'])