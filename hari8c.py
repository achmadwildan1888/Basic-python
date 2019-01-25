import requests
# nama = 'Anthony Joshua'
# url = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?p='+nama

# data = requests.get(url)
# output = data.json()
# print(data.json())
# print(output['player'][0]['strNationality'])

inputan=input('ketik nama klub = ')
url2 = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t='+inputan

data2 = requests.get(url2)
listpemain = data2.json()['player']
#print semua nama pemain klub tertentu
for name in listpemain:
    print(name['strPlayer'])
#print dengan posisi tertentu
print('untuk list keeper sbb = ' )
for name in listpemain:
    if name['strPosition'] ==  'Goalkeeper':
        print(name['strPlayer'])