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

def ubahkemorse(teks):
    kalimat = teks.upper().replace(' ','') #meruba Purwadhika menjadi lower, lalu mereplace jika ada spasinya
    hasil= ''
    for i in kalimat:
        hasil +=morse[i]+ ' / '
    print(hasil)

ubahkemorse('wildan')
#the logic is here

# x = { 'nama' :'andi', 
# 'usia':22,'kota':'bandung'}

# 1.print(list(x.keys())[0]) 
# 2.print(list(x.values().index('andi')) # ini adalah list dari values , maka masukan kedalam list
# 3.print(list(x.keys())[list(x.values()).index(21)])  #ini adalah key dari value, derived from point 1

def ubahdarimorse(teks):
    kalimat = teks.split(' / ') ##mereplace / ada spasinya, jika di split hasilnya akan menjadi list [ ' ...' , '---,,,,']
    hasil= ''
    for i in kalimat:
        hasil +=list(morse.keys())[list(morse.values()).index(i)]
    print(hasil)

ubahdarimorse('.-- / --- / .-- / ---')