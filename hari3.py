#set
print('-----------------------------------set--------------------------------')

tes = {1,2,3}
 #  print(tes[0]) , tidak bisa diakses elemennya 

 #check elemen
print(2000 in tes)

 #add an element
tes.add('budi')
print(tes)

 #add element
data= ([3,4,'caca','dedi'])
tes.update(data)
print(tes)

#remove element
tes.remove('dedi') #bisa pake .discard , tidak akan error sperti .remove
print(tes)

#delete all elements 
# del tes 

#delete all element
#set.clear()
#print(set)
print('-----------------------------------dictionary-------------------------------------')
#dictionary = {key : value}

bulan = {
    1: 'januari',
    2: 'februari',
    3: 'maret',
    4: 'april',
    5: 'may',
    6: 'juni'
}

print(bulan[2])
print(bulan.get(2))
print(bulan.get(13))

#merubah value
bulan[1]='January'
print(bulan[1])

#add item
bulan[7] = 'july'
print(bulan) 

# update
bulan.update ({7: 'julijuli'})
print(bulan)

#remove item
bulan.pop(7) # atau bisa pake del bulan[7]
print(bulan)
print('-------------------------------------------------------')
student =['andi','budi','caca']

nama= input('ketik nama baru =' )
student.append(nama)
print(student)