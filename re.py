dosyaKonumu = "E:\python\Yeni klasör (2)\Yeni-klas-r\metin.txt"

import os

if os.path.exist(dosyaKonumu):
    print("dosyayı buldum.. işlem yapıyorum.")
    with open(dosyaKonumu, "+r") as dosya:
        icerik = dosya.read()
        print(icerik)
else:
    print("Dosya yok gözün kör olmasın..")