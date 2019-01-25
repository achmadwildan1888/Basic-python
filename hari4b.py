#return function

def luas(x):
    print(x*x)

def luas2(y): 
    return(y*y) #merubah nilai y menjadi y*y

luas(12)
print(luas2(8))

def ganjilgenap(angka):
    if angka %2 == 0:
        return 'Angka '+str(angka)+' tergolong genap'
    else:
        return 'Angka '+str(angka)+' tergolong ganjil'

print(ganjilgenap(23))


print('--------------------------------loop---------------------------------')
# looping

# angka =0
# while angka<=6:
#     print(angka)
#     angka+=1

# password = '123'
# inputuser =''

# while inputuser != password:
#     inputuser =input('ketikan password = ')
# --------------------while true ----------------------------
# while True:
#     inputuser1 = input('ketikan nama anda:')
#    print('halo',inputuser1)
# ---------------------password------------------------
# inputuser2 =''
# password2 ='andi'

# while inputuser2!= password2:
#    inputuse2r= input('ketikan password : ')
#     if inputuser2==password2:
#        print('Password benar')
#    else:
#        print('password salah')

password = '1234'
inputuser=''
tebakanke=int(input('masukan tebakan = '))
batastebakan=5
melebihibatas= False
while inputuser !=password and not melebihibatas:
    if tebakanke <= batastebakan:
        inputuser = input('ketikan password: ')
        if inputuser != password and tebakanke <5:
            tebakanke+=1
            print('pass salah percobaanke-', tebakanke)
        elif inputuser !=password and tebakanke ==5:
            tebakanke +=1
            print('pass salah ,kesempatan habis!')
        else:
            print('pass benar')
    else:
        melebihibatas = True
        print('mohon maaf , coba lain kali')