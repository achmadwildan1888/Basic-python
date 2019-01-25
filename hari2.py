#number

angka = 5j #bilangan imajiner

print(angka)
print(type(angka))



from math import *

print(floor(3.9)) #pembulatan kebawah
print(ceil(3.9))

print(round(3.2))
print(round(3.8))

#rumus akar pangkat 2 ,3 dll 
print("hasil rumus akar pangkat 3 dr 64 = ",round(64**(1/3)))
print(round(pow(64,1/3)))

#variable

#isilah = input('ketik nama anda : ')

#sisi = int(input(' masukan sisi persegi : '))

#print( 'keliling persegi =', (sisi*4) ,'sedangkan luas persegi =', (sisi*sisi))

jumlah = 45000
mangga = jumlah/3
apel= jumlah/3

print('harga mangga = ', mangga)

print('harga apel = ', apel)

#soal
# sekarang jumlah usia A+ B = 49 th
# perbandingan usia A / B = 0.4
# usia A & B 5 tahun lg brp ?

total = 49
rasio  = 0.4 

b= total/ (1+rasio)
a= total-b

a= a+5
b= b+5

print(b)
print(a)

angka =12
angka +=3 #assignment operator langsung mengubah nilai
print(angka)

angka-=5
print(angka)

print(0.1+0.2)

#list

buah = ['mangga','apel','jeruk','melon','melon']

print(buah.index('mangga'))
print(buah.count('melon'))

print(buah[0::2]) #print genapnya saja, start # stop # step

angka = [0,1,2,3,4,5,6,7,8,9]
angka2 = angka.copy()
angka.reverse()
 #meng copy list
print(angka)
print(angka2)

list = [
        [1,2,3],
        [4,5,6],
        (7,8,9)
]
print(list[2][2]) #dari index ke 1 , lihat index dr list tsb

tuple = ( [1,2,3],(4,5,6),(7,8,9))
print(tuple[0])
print(tuple[2][0])

nomor = ([1,2,3],[1,2,3],[4,5,6]) 
nomor[0][1]= 'andi' #bisa ganti index dari list meski dalam tuple
#nomor[0] ='andi'  #tidak bisa karena dalam tuple' 
print(nomor)
