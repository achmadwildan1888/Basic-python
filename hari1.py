kalimat = ' sekolah Hari in Andi tidak Sekolah'
cari = 'sekolah'
kalcari = kalimat.upper().replace(cari.upper(), '') #mengubah sekolah menjadi string kosong diubah jadi upper 

print(len(kalimat))
print(len(kalcari))
print(len(cari))

print(int((len(kalimat)) - len(kalcari)) / len(cari)) 

kalimat1 = ' sekolah Hari in Andi tidak Sekolah'
print(kalimat1.split('a')) # memotong kalimat pada bagian A

kalimat2 ='sekolah Hari in Andi tidak Sekolah'

print(kalimat2.replace('a','i')) #bisa buat 3 karakter ,yg ke 3 berapa jmlahnya

print(kalimat2.replace('a','i').replace('k','d'))

#int&float

jumlah = -12
bobot = -12.7

print(type(jumlah))
print(type(bobot))