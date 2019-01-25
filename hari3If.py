#if statement
print('------------------------if statement ---------------------')

angka =12

if angka ==12:
    print('anda benar!')
elif angka <= 12:
    print('angka kuurang dr 12')
else:
    print('angka => 12')

bekerja = True
tahun = 1

if bekerja and tahun >=2:
    print('anda sdh bekerja berpengalaman')
elif bekerja and tahun <2:
    print('anda pegawai baru')
elif not bekerja and tahun <2:
    print('anda sedang mencari bekerja')
else:
    print('anda sdh lama tdk bekerja')
print('------------------------ganjil genap ---------------------')


#angka= int(input('input angka =' ))

#if angka % 2 == 0:
   # print(angka,'adalah genap')
#else:
   # print(angka, 'adalah ganjil')

print('------------------------calculator ---------------------')

#angka1= float(input('Masukan angka1 =' ))
#operator= input(' masukan operator :(+-/*)=')
#angka2= int(input('Masukan angka2 =' ))

#if operator == '+':
   # print(angka1+angka2)
#elif operator == '-':
   # print(angka1-angka2)
#elif operator =='*':
    #print(angka1*angka2)
#elif operator =='/':
    #print(angka1/angka2)
#else:
    #print('tdk ada operator')

print('------------------------IMT ---------------------')

massa= float(input('Masukan massa(kg) =' ))
tinggi= float(input('Masukan tinggi(cm) =' ))
IMT = float(massa / ((tinggi/100)**2))

print(IMT)

if (IMT < 18.5):
    print('bb kurang')
elif (IMT >= 18.5 and IMT < 24.9):
    print('bb ideal')
elif IMT >= 25.0 and IMT < 29.9:
    print('bb berlebih')
elif IMT >= 30.0 and IMT < 39.9:
    print('bb sangat berlebih')
else:
    print('obesitas')