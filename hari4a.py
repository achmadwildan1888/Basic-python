#function

def halo():
    print('halo, ini function')

halo()

def luas():
    sisi = 12
    print(sisi**2)
luas()

#function dgn parameter

def luasp(sisi):
    print(sisi**2)

luasp(2)
luasp(100)

print('------------------------------fungsi 2 paramter--------------------------')
#function dgn 1 paramter
def luaspjg(p,l):
    print(p*l)
luaspjg(2,4)
luaspjg(3,3)

print('------------------------------fungsi luas trapesium--------------------------')

def luastrap(alas,atap,t):
    luas = (alas+atap)*(t/2)
    print('luas trapesium adalah =', luas)
luastrap(8,4,9)
luastrap(20,17,8)

print('------------------------------konverter rupiah ke dollar--------------------------')

datakurs ={'USD-IDR' : 14000,'IDR-USD':0.00007}

def convert(uang,metode):
    if (metode=='USD-IDR'):
        kurs=datakurs[metode]
        print('hasil convert USD-IDR= ','Rp',uang*kurs)
    elif (metode=='IDR-USD'):
        kurs=datakurs[metode]
        print('hasil conver IDR-USD','US$',uang*kurs)
    else:
        print('kurs tidak ditemukan')
convert(1,'USD-IDR')
convert(80000000,'IDR-USD')
convert(38923829,'jpy')

print('------------------------------konverter rupiah ke dollar dengan input--------------------------')

datakurs ={'USD-IDR' : 14000,'IDR-USD':0.00007}

def convert1():
    metode=input('Silakan masukan metode = ')
    uang=float(input('silakan masukan nominal uang = '))
    if (metode=='USD-IDR'):
        kurs=datakurs[metode]
        print('hasil convert USD-IDR= ','Rp',uang*kurs)
    elif (metode=='IDR-USD'):
        kurs=datakurs[metode]
        print('hasil conver IDR-USD','US$',uang*kurs)
    else:
        print('kurs tidak ditemukan')
convert1()
