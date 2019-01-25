#for loop

nama = ' purwadhika'

for i in nama:
    print(i)

nama = ['andi','budi','caca']

for data in nama:
    print(data,'susanoo')

for data in range(len(nama)):
    print(nama[data], ' Effendi')
    

x=''

for i in range(5):
    for j in range(0, i+1):
        x += '*'
    x += '\n'
print(x)

star =''
for a in range(5):
    star +='$'
    print(star)

for i in range(5):
    for j in range(6,10):
        print(i,'&',j)

# i=0-j=6 maka prnt 0 & 6
# i=0-j=7 maka prnt 0 & 7
# i=0-j=7 maka prnt 0 & 8
# berhenti di 10 karna in range (6,10)

#contoh

list = [[1,2,3],[4,5,7],[7,8,9]]

for baris in list: #in untuk mengakses isi list, yaitu elemn)
    for kolom in baris:#in untuk mengakses elemen dari elemen , yaitu isinya)
        print(kolom)

for baris in list:
    print(baris[0])
    print(baris[1])
    print(baris[2])

#contoh2

list=[]
i=0
while i <=103:
    list.append(i)
    i +=1

for data in list:
    print(data)