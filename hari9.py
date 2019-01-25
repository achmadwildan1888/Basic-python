import requests

# url = 'http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1'

# data = requests.get(url)
# listquote = data.json()

# print(listquote)
# print(listquote[0]['content'])

print('--------------------masuk ke bag kurs-----------------------------')

# inputbank = input('masukan jenis bank = ....')
# inputanuang=int(input('masukan uang dalam dollar = ....'))

# url2= 'https://kurs.web.id/api/v1/'+ inputbank

# data=requests.get(url2)
# listkurs=data.json()
# hargajual=int(listkurs['jual'])

# print('kurs BCA saat ini=',hargajual)
# print('inputan uang =',inputanuang ,'US$')
# print('hasil konversi ke rupiah kurs BCA sbb = ',(inputanuang*hargajual))

def convert1():
    bank=input('silakan masukan jenis bank = ')
    metode=input('Silakan masukan metode = ')
    uang=float(input('silakan masukan nominal uang = '))
    url2= 'https://kurs.web.id/api/v1/'+bank

    data=requests.get(url2)
    listkurs=data.json()
    listbank= listkurs['bank']
    print('Bank yang digunakan adalah',listbank)
    listkurserror = listkurs['error']
    

    if (str(listkurserror) =="true"): 
        print('bank tidak ditemukan')
    else:
        (bank.upper()==listkurs['bank']) #tidak mengenali bank karna hilang dipostman
        print(listkurs['bank'])
        

    if (metode=='USD-IDR'):   
        hargajual=listkurs['jual']
        hargabeli=listkurs['beli']
        kurs=int(hargabeli)
        print('hasil convert USD-IDR= ','Rp',uang*kurs, 'dengan harga jual = ', hargajual ,'dan harga beli = ', hargabeli)
    elif (metode=='IDR-USD'):
        hargajual=listkurs['jual']
        hargabeli=listkurs['beli']
        kurs=int(hargajual)
        print('hasil convert IDR-USD=','US$',uang/kurs,'dengan harga jual = ', hargajual ,'dan harga beli = ', hargabeli)
    else:
        print('kurs tidak ditemukan')
convert1()

