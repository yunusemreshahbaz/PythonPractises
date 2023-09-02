"""
import turtle
import random
# Program fonksiyona gönderilen parametreler ile çokgen çizer.
# Uzunluk paremetresi girilerek herbir kenarın uzunluğu belirlenir.
# Çizim x ve y parametrelerine girilen koordinat noktalarından başlar.
# Bir sonraki parametre çizimin kenar rengini belirler. (Varsayılan değer olarak siyah).
# Çizilen çokgenin içine dolgu olup olmayacağı belirlenir(Varsayılan False).
def Cokgen(kenarSayisi, uzunluk, x, y, renk="black", dolgu=False):
 turtle.penup()
 turtle.setposition(x, y)
 turtle.pendown()
 turtle.color(renk)
 if dolgu:
    turtle.begin_fill()
 for i in range(kenarSayisi):
    turtle.forward(uzunluk)
    turtle.left(360//kenarSayisi)
 if dolgu:
    turtle.end_fill()
# Adım adım çizim işlemi iptal edilerek çizim hızlandırılıyor
    turtle.hideturtle()
    turtle.tracer(0)
# Fonksiyonlar örnek çizimler için kullanılıyor
Cokgen(3, 30, 0, 0) # Üçgen çizimi
Cokgen(4, 30, 50, 50, "blue") # Kenar rengi mavi olan Kare çizimi
Cokgen(5, 30, 100, 100, "red", True) # Dolgusu kırmızı olan beşgen çizimi
turtle.update()
turtle.exitonclick() # Fare tuşuna tıklandığında çıkış işlemi yapılacaktır.
"""

"""
class Ogrenci:
    bolum = "Mühendislik"
    
    def __init__(self):
        self.ad = 'Yunus'
        self.soyad = ''

ogr1 = Ogrenci()
print(ogr1.ad)
print(ogr1.bolum)
print(Ogrenci.bolum)
"""

"""
class Ogrenci:
    bolum = "Mühendislik"

    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad

    def tamad(self):
        tam_isim = self.ad + " " +self.soyad
        return tam_isim

ogr1 = Ogrenci("Yunus","Şahbaz")
print(ogr1.ad)
print(ogr1.tamad())

print()

ogr2 = Ogrenci("Semih","Ocak")
print(ogr2.ad)
"""

"""
class Calisan:
    sirket = "BTK"

    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.f_eposta()

    def f_eposta(self):
        return (self.ad + self.soyad).lower() + "@sirket.com"

    @classmethod
    def pi(cls):
        return 3.14

print("Genel şirket1:",Calisan.sirket)

print()

calisan1 = Calisan("Yunus","Şahbaz",50000)
print("Yunus'un şirketi1:",calisan1.sirket)
print("Yunus'un adı1:",calisan1.ad)
print("Yunus'un maaşı1:",calisan1.maas)
calisan1.maas *= 1.5
print("Yunus'un maaşı2",calisan1.maas)
calisan1.sirket = "Aselsan"
print("Yunus'un şirketi2",calisan1.sirket)

print()

print("Genel şirket2:",Calisan.sirket)
Calisan.sirket = "THY"
print("Genel şirket3:",Calisan.sirket)

print()

calisan2 = Calisan("Gülce","Gök",50000.5)
print("Gülce'nin şirketi1:",calisan2.sirket)

print()

print(calisan1.eposta)
print(calisan1.pi())
print(Calisan.pi())
"""

"""
class Calisan:
    zam_orani = 1.07
    per_say = 0
    
    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.f_eposta()
        Calisan.per_say += 1

    def f_eposta(self):
        return (self.ad + self.soyad).lower() + "@sirket.com"

    def arttir(self):
        # self.maas *= 1.05  # manuel olarak zam oranını yazdık
        # self.maas *= Calisan.zam_orani  # Calisan sınıfındaki zam oranı
        self.maas *= self.zam_orani
        # Herkese gene Calisan sınıfındaki zam oranını kullanıyor ancak
        # istediğimiz kişiye farklı zam oranı verebiliyoruz


print(Calisan.per_say)
calisan1 = Calisan("Yunus","Şahbaz",50000)
print(Calisan.per_say)
calisan2 = Calisan("Emre","Şahbaz",45000)
print(Calisan.per_say)
calisan1.arttir()
print(calisan1.maas)

calisan2.zam_orani = 1.15
calisan2.arttir()
print(calisan2.maas)
"""

"""
class sporcu():
    def __init__(self,ad,brans,altin,gumus,bronz):
        self.ad = ad
        self.brans = brans
        self.mbronz = bronz #public veri halka açık değişken
        self._mgumus = gumus #protected yarı gizli
        self.__maltin = altin #private tam gizli
    def atlet_bilgisi(self):
        return "Sporcu adı : {}, Branşı :{}".format(atlet1.ad,atlet1.brans)
    @property
    def a_yazdir(self):
        amadalya = self.__maltin
        return "altın madalya sayısı {}".format(self.__maltin)

atlet1 = sporcu("ali","100 Metre",2,3,9)
print(atlet1.atlet_bilgisi())
print("bronz madalya sayısı",atlet1.mbronz)
print("gümüş madalya sayısı",atlet1._mgumus)
print(atlet1.a_yazdir)
"""
