def toplama(num1:int,num2:int):
    return num1+num2

def cikarma(num1:int,num2:int):
    return num1-num2

def carpma(num1:int,num2:int):
    return num1*num2

def bolme(num1:int,num2:int):
    return num1/num2
    

def kokalma(num1:int,num2:int):
    return num1**(1/num2)

def kuvvetalma(num1:int,num2:int):
    return num1**num2

def kalan(num1:int,num2:int):
    return num1%num2

secim = input("1. Toplama\n"\
                "2. çıkartma\n"\
                "3. Çarpma\n"\
                "4.Bölme\n"\
                "5.kök alma\n"\
                "6.Kuvvet Alma\n"\
                "7.Bölümden Kalanını Bulma\n"\
                "8. çıkış\n"\
                "Yapmak istediğiniz işlemi seçiniz>")
if secim=="8":
    exit()

if not secim.isdigit():
    print("Lütfen 1 ile 8 arası bir sayı giriniz.")
    
elif int(secim) not in range(1,9):
    print("Aralık dışı sayı girdiniz!!!")
    
sayi1 = int(input("Birinci sayıyı giriniz:"))
sayi2 = int(input("İkinci sayıyı giriniz:"))
sonuc=0
if secim=="1":
    sonuc=toplama(sayi1,sayi2)
    
elif secim=="2":
    sonuc=cikarma(sayi1,sayi2)
    
elif secim=="3":
    sonuc=carpma(sayi1,sayi2)
    
elif secim=="4":
    sonuc=bolme(sayi1,sayi2)
    if sayi2==0:
        sonuc=="sonsuz"

elif secim=="5":
    sonuc=kokalma(sayi1,sayi2)
    
elif secim=="6":
    sonuc=kuvvetalma(sayi1,sayi2)
    
elif secim=="7":
    sonuc=kalan(sayi1,sayi2)
    
print("işlem sonucu: {}".format(sonuc))