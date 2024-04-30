from random import randint

bilgisayarSecimi = randint(1,100)
MIN = 1
MAX = 100
tahminListesi = []
while True:
    kullaniciSecimi = input("{}-{} arasında Sayi arassında giriniz : ".format(MIN,MAX))
    if kullaniciSecimi=="q":
        break
    elif not kullaniciSecimi.isdigit():
        print("sayı giriniz:")
        continue
    kullaniciSecimi=int(kullaniciSecimi)
    
    tahminListesi.append(kullaniciSecimi)
    
    if kullaniciSecimi > bilgisayarSecimi:
        print("Daha küçük olmalı")
        MAX = kullaniciSecimi

    if bilgisayarSecimi > kullaniciSecimi:
        print("Daha büyük olmalı")
        MIN = kullaniciSecimi

    if bilgisayarSecimi == kullaniciSecimi:
        print("Kutlaaarrııııızzzz....")
        break
    
for idx,i in enumerate(tahminListesi):
    print(idx+1,". Tahmin : ",i)

print("tahmin sayısı: {}".format(len(tahminListesi)))

