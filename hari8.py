#file handling
#'r'ead,'w'rite,'a'ppend,'x'create,'r+'ead

file = open('data.txt','r')
print(file.read())
print(file.readable())
print(file.readline()) #hanya membaca baris pertama
print(file.readlines()) # setiap baris ditampilkan dlm list

file=open('data.txt','a') #jika 'w' maka akan overwrite semua file
file.write('\nGIlang')

 #file =open('data2.txt','x') # this create data2.txt

list = ['Andi','Budi','Caca']
file2 = open('data2.txt','w')

for i in list:
    file2.write(i+'\n')

#hanya bisa text based , python, txt . docx ,pptx error

#untuk menghapus
# import os
# os.remove('tes.json')
# os.rmdir('ok') #menghapus directory ok 

file = open('datajson.json','w')

file.write('[{"nama":"andi"},{"nama":"budi"},{"nama":"caca"}]')