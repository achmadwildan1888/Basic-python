# x = range(1, 16)

# for y in x:
#     if y % 3 == 0 and y % 5 == 0:
#         print ("Ting")
#     elif y % 5 == 0:
#         print ("Dor")
#     elif y % 3 == 0:
#         print ("Ces")
#     else:
#         print(y)

def fizzbuz(x):
    for y in range(1,x+1):
        if y % 3 == 0 and y % 5 == 0:
            print ("Ting")
        elif y % 5 == 0:
            print ("Dor")
        elif y % 3 == 0:
            print ("Ces")
        else:
            print(y)
fizzbuz(15)

#penerjemah ke morse

# def morse(a):
#     for b in range(a):
#         if 'a':
#             print('.-')
#         elif 'b':
#             print('-...')
#         else:
#             print(b)
# morse('saya bingbgbgbbg')

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