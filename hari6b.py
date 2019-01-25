morsekamus = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
"..-.": "F", "--.": "G", "....": "H",
"..": "I", ".---": "J", "-.-": "K", ".-..": "L",
"--": "M", "-.": "N", "---": "O", ".--.": "P",
"--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V",
".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"}

nomorse = input("Enter your Morse code here:")
nomorse_list = nomorse.split() #this splits the string up wherever there is a space
not_morse = []
morse = True    #The code is morse (so far)
for letter in nomorse_list:
    eng_letter = False
    for key in morsekamus.keys():   #for each of the morse code letters in the dictionary
        if letter == key:
            eng_letter = morsekamus[key]
    if eng_letter: #if a letter was found that corresponds
        not_morse.append(eng_letter)
    else:
        print("Input is not valid morse code.")
        morse = False
if morse == True:
    string = "".join(not_morse) #joining the string together (without spaces in between)
    print(string)