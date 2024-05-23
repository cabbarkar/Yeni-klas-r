import os
from cryptography.fernet import Fernet

dosyaKonumu = "E:\python\Yeni klasör (2)\Yeni-klas-r\password\sifre.txt"
anahtarKonumu = "E:\python\Yeni klasör (2)\Yeni-klas-r\key.data"

def anahtarOlustur():
    key = Fernet.generate_key()
    with open(anahtarKonumu,"wb") as dosya:
        dosya.write(key)
        
def anahtarOku():
    if not os.path.exists(anahtarKonumu):
        print("Dosya oluştuurldu...")
        anahtarOlustur()
    with open(anahtarKonumu, "rb") as file:
        key = file.read()
        return key

key = anahtarOku()
anahtar = Fernet(key)


def tumunugoruntule(dosyaYolu):
    if os.path.exists(dosyaYolu):
        with open(dosyaYolu, "r") as dosya:
            icerik = dosya.readlines()
            for satir in icerik:
                kullaniciadi, sifre = satir.split(":")
                sifre=anahtar.decrypt(sifre.encode()).decode()
                print("Kullanıcı adı: {}, Şifre: {}".format(kullaniciadi, sifre.replace("\n","")))
    else:
        print("yok")

def kullaniciekle(dosyaYolu):
    if os.path.exists(dosyaYolu):
        yeniKullaniciadi = input("Kullanıcı adı giriniz:")
        yeniSifre = input("Şifre giriniz :")
        yeniSifre = anahtar.encrypt(yeniSifre.encode().decode())
        with open(dosyaYolu, "a+") as dosya:
            dosya.write(yeniKullaniciadi+" : "+yeniSifre + "\n")
            
    else:
        print("Dosya yok")
    exit()

def kullaniciSil(dosyaYolu):
    if os.path.exists(dosyaYolu):
        kullaniciAdi = input("Silinecek kullanıcı adını giriniz:")
        with open(dosyaYolu, "r") as dosya:
            icerik = dosya.readlines()
        
        for i, satir in enumerate(icerik):
            if kullaniciAdi in satir:
                icerik.pop(i)
         
            else:
                print("böyle bir kullanıcı yok")
                
        with open(dosyaYolu, "w") as dosya:
            dosya.writelines(icerik)       
    else:
        print("Dosya yok")
    exit()
    
    

def kullaniciSil(dosyaYolu):
    if os.path.exists(dosyaYolu):
        kullaniciAdi = input("Silinecek kullanıcı adını giriniz:")
        with open(dosyaYolu, "r") as dosya:
            icerik = dosya.readlines()
        
        for i, satir in enumerate(icerik):
            if kullaniciAdi in satir:
                icerik.pop(i)
         
            else:
                print("böyle bir kullanıcı yok")
                
        with open(dosyaYolu, "w") as dosya:
            dosya.writelines(icerik)       
    else:
        print("Dosya yok")
    exit()
    
    
def sifredegistirme(path):
    if os.path.exists(path):
        kullaniciAdi = input("Değişecek kullanıcı adını giriniz:")
        with open(path, "r") as dosya:
            tumIcerik = dosya.read()
            if kullaniciAdi not in tumIcerik:
                print("yok böle biri")
                
            dosya.seek(0)
            icerik = dosya.readlines()
        
        for idx, satir in enumerate(icerik):
            if kullaniciAdi in satir:
                kullaniciAdi,sifre = satir.replace("n","").split(":")
                sifre = input("sifre giriniz:")
                icerik[idx] = kullaniciAdi + ":" + sifre + "\n"
        
        with open(path, "w") as dosya:
            dosya.writelines(icerik)


def main():        
    print("seçenekler:\n"
        "1. kullanıcı ve şifre görüntüle\n"
        "2. kullanıcı ekle\n"
        "3. kullanıcı silme\n"
        "4. şifre değiştirme\n"
        "5. anahtar oluştur\n"
        "6. çıkış\n"
        "İşleminiz: ")

    cevap = input("Birseçenek giriniz :")

    if cevap== "1":
        tumunugoruntule(dosyaKonumu)
        #tumunugoruntule
    elif cevap== "2":
        kullaniciekle(dosyaKonumu)
        #kullanıcı ekle
    elif cevap== "3":
        kullaniciSil(dosyaKonumu)
        #kullanıcı silme
    elif cevap== "4":
        sifredegistirme(dosyaKonumu)
        #sifre degistirme
    elif cevap== "5":
        anahtarOlustur(anahtarKonumu)
    elif cevap== "6":
        exit()
    else:
        print("adamın canını sıkma..")
        
main()
