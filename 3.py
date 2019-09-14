kata_1 = input ("kata/frasa pertama :")

cou_1 = len(kata_1)

kata_2 = input ("kata / frasa kedua : ")

cou_2 = len(kata_2)

if cou_2>cou_1 :
            print ('frasa kedua tidak boleh lebih banyak dari frasa pertama!!')
else:
            kata = str(kata_1.count(kata_2))

print ('ditemukan '+ kata + ' kali')
