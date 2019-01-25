# #import
import hari6f

hari6f.ubah(input('masukan karakter'))

#lambda

kali = lambda a,b : a*b

print(kali(2,3))

def tes(x):
    return lambda a : a*x

duakali = tes(2)
tigakali = tes(3)

print(duakali(31))
print(tigakali(31))

print('----------------------try & except---------------------')

try:
    nilai1 = int(input('ketik angka : '))
    nilai2 = int(input('ketik angka : '))
    print(nilai1/nilai2)
except ValueError:
    print('maaf nilai bukan angka')
except ZeroDivisionError:
    print('nilai tak terhingga')