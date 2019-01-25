morse = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

# inputan1=input('masukan kalimat to morse = ')     
# def ubahkemorse(teks):
#     teks=inputan1
#     kalimat = teks.upper().replace(' ','') #meruba Purwadhika menjadi lower, lalu mereplace jika ada spasinya
#     hasil= ''
#     for i in kalimat:
#         hasil +=morse[i]+ ' / '
#     print(hasil)
# ubahkemorse(inputan1)

# inputan2=input('masukan kode morse =')
# def ubahdarimorse(teks):
#     teks=inputan2
#     kalimat = teks.split(' / ') ##mereplace / ada spasinya, jika di split hasilnya akan menjadi list [ ' ...' , '---,,,,']
#     hasil= ''
#     for i in kalimat:
#         hasil +=list(morse.keys())[list(morse.values()).index(i)]
#     print(hasil)

# ubahdarimorse(inputan2)


#cara lain

def ubah(teks):
    if teks.upper() == teks.lower():
        kalimat = teks.split(' / ') ##mereplace / ada spasinya, jika di split hasilnya akan menjadi list [ ' ...' , '---,,,,']
        hasil= ''
        for i in kalimat:
            hasil +=list(morse.keys())[list(morse.values()).index(i)]
        print(hasil)
    else: 
        kalimat = teks.upper().replace(' ','') ##mereplace / ada spasinya, jika di split hasilnya akan menjadi list [ ' ...' , '---,,,,']
        hasil = ''
        for i in kalimat:
            hasil += morse[i] + ' / '
        print(hasil)

ubah(input('\nKetik karakter yang akan diubah = '))