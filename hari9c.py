import requests
appid = ' '
url = ' ' 
cari= 'Jakarta'

data = requests.get(url+cari+'&APPID='+appid)

print(data.json(['weather'][0]['main']))