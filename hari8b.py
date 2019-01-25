import json

datajson1 = '{"nama":"andi"}'
datalist = [{'nama':'andi','usia':'21'}]
datadict = json.loads(datajson1) #mengubah json menjadi dictionary , untuk sebaliknya json.dumps()

print(datadict)
print(datadict['nama'])

file = open('data.json','r')
datajson=file.read()
print(datajson)

datapy = json.loads(datajson) #mengubah json ke python
print(datapy)