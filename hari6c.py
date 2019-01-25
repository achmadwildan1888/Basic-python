morsekamus = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
"..-.": "F", "--.": "G", "....": "H",
"..": "I", ".---": "J", "-.-": "K", ".-..": "L",
"--": "M", "-.": "N", "---": "O", ".--.": "P",
"--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V",
".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"}

def ubahketeks(teks):
    kalimat=teks.replace(' ','')
    hasil= ''
    for i in kalimat.split(' '):
        hasil +=morsekamus[i]
    print(hasil)

ubahketeks('-.-. -.. -.- .-..')