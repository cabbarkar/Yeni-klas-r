#dosya = open("E:\python\Yeni klasör (2)\Yeni-klas-r\metin.txt","r", encoding="utf-8")

"""print("seeker: ", dosya.tell())
icerik = dosya.read(5)
print("seeker : ", dosya.tell())
icerik2 = dosya.read()
print("seeker : ", dosya.tell())
print(icerik)
print(icerik2)"""

"""icerik = dosya.readline()
icerik2 = dosya.readline()
icerik3 = dosya.readline()
print("seeker : ", dosya.tell())
print(icerik,end="")
print(icerik2,end="")
print(icerik3,end="")"""

"""icerik = dosya.readlines()
print(type(icerik))
print(icerik)
print("seeker : ", dosya.tell())"""


dk = "metin.txt"
dosya = open(dk,"r", encoding="utf-8")
icerik = dosya.read(10)
#dk = dosya.readlines()
print(dosya.tell())
icerik2=dosya.read(3)
print(dosya.tell())
print(icerik)
print(icerik2)
#for satir in icerik: