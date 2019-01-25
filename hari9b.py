import requests

inputanuang= int(input('masukan uang dalam rupiah = ...Rp.'))
inputanuang2=str(inputanuang)
metode=input('Silakan masukan metode = ')
bank = bank=input('silakan masukan jenis bank = ')
url= 'https://blockchain.info/tobtc?currency=USD&value='+inputanuang2
url2='https://kurs.web.id/api/v1/'+ bank

data=requests.get(url)
listkurs=data.json()

data2=requests.get(url2)
listkurs2=data2.json()
hargajual=int(listkurs2['jual'])
print(bank)
#belum selesai silahkan lanjutkan ke datarequest
def konversi():
    if (metode=='IDR-Bitcoin'):
        rupiahtoUSD= inputanuang / hargajual
        rupiahtoUSDint= str(rupiahtoUSD)
        url3= 'https://blockchain.info/tobtc?currency=USD&value='+rupiahtoUSDint
        data3=requests.get(url3)
        listkurs3=data3.json()
        print('hasil dari IDR-bitcoin = ',listkurs3 )
    elif (metode=='US-Bitcoin'):
        print('hasil dari IDR-bitcoin = ',url )
    else:
        print('metode tidak ada')
konversi()
#rupiah ke USD, USD ke bitcoin
