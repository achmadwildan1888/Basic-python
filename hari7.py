#package in python

import datetime 
x = datetime.datetime.now()
print(x)

waktu = str(x).split(' ')
dateform = waktu[0]
tahun = dateform.split('-')[0]
bulan = dateform.split('-')[1]
tanggal = dateform.split('-')[2]
print(tahun,bulan,tanggal)

hourform = waktu[1]
jam = hourform.split(':')[0]
menit = hourform.split(':')[1]
detik = hourform.split(':')[2]

print(jam,menit,detik)

#caradefault
hari = {
    'Monday' : 'Senin', 'Tuesday' : 'Selasa'
}

bulan = {
    'January' : 'Januari' , 'February ' : 'Februari'
}

print(hari[x.strftime('%A')])
print(bulan[x.strftime('%B')])

print(x.strftime('%A-%B'))

#threading 

# import threading
# def printtiapdetik():
#     threading.Timer(1.00,printtiapdetik).start()
#     print('halo dunia')
# printtiapdetik()

import time
def tes():
    while True:
        print('Tes 1 2 3')
        time.sleep(1)
tes()

import time
def tes():
    while True:
        x=datetime.datetime.now()
        print(x.strftime('sekarang jam %H:%M:%S WIB'))
        time.sleep(0.0000000000000001)
tes()