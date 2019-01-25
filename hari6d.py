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

def trans(teks):
    periksa= []
    hasil =''
    for i in range(len(teks)): #dibentuk untuk menyesuaikan panjang karakter ,maka dimasukan ke list
        if teks[i]== '/':
            periksa=teks.split('/') # split per / 
    for j in range (len(periksa)):
        for kunci,v in morse.items(): #ambil key n value dari dict
            if periksa[j]==v: #memeriksa satu2 , elemen ke 0 periksa ke value morse
                hasil+=kunci
    print(hasil)

trans('-----/.----')