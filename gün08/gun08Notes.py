"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])
print(thisdict.keys())
print(thisdict.values())
for baslik in thisdict:
    print(baslik)
    print(thisdict[baslik])
"""

"""
# iç içe listeler, çok boyutlu listeler
sebze = ['domates', 'biber']
meyve = ['üzüm', 'çilek', 'kivi', 'karpuz', 'incir', 'ayva', 'armut', 'armut']
sark = ["peynir", "helva", "bal"]
yesillik = ["roka", "maydanoz", "tere"]
#pazar_listesi = sebze + meyve
#print(pazar_listesi)
pazar_listesi = [sebze, meyve, sark, yesillik, "baklava"]
print(pazar_listesi)
print(pazar_listesi[0][0])
print(pazar_listesi[1][1])
for dd in pazar_listesi:
    if type(dd) is list:
        for urun in dd:
            print(urun, end="\t")
        print()
    else:
        print(dd)
"""

"""
class Sporcu():
    total_bornz = 5
    _total_gumus = 15
    __total_madalya = 25
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

class Gsporcu(Sporcu):
    def __init__(self,ad,brans,altin,gumus,bronz):
        super().__init__(ad,brans,altin,gumus,bronz)

    def fbmyazdir(self):
        print("Bronz",self.mbronz)

    def fgmyazdir(self):
        print("gümüş", self._mgumus)
    def famyazdir(self):
        print("Altın", self.__maltin)

class Torun(Gsporcu):
    def __init__(self,ad,brans,altin,gumus,bronz):
        super().__init__(ad,brans,altin,gumus,bronz)

    def fbmyazdir(self):
        print("Bronz",self.mbronz)

    def fgmyazdir(self):
        print("gümüş", self._mgumus)
    def famyazdir(self):
        print("Altın", self.__maltin)



# atlet1 = Sporcu("ali","100 Metre",2,3,9)
# print(atlet1.atlet_bilgisi())
# print("bronz madalya sayısı",atlet1.mbronz)
# print("gümüş madalya sayısı",atlet1._mgumus)
# # print("Altın Madalya",atlet1.__maltin)
# print(atlet1.a_yazdir)
# gatlet = Gsporcu("ali","100 Metre",2,3,9)
# gatlet.fbmyazdir()
# gatlet.fgmyazdir()
# gatlet.famyazdir()

torun = Torun("ali","100 Metre",2,3,9)
# torun.fbmyazdir()
# torun.fgmyazdir()
# torun.famyazdir()
# print(torun.total_bornz)
# print(torun._total_gumus)
# print(torun.__total_altin)

print(Torun.total_bornz)
print(Torun._total_gumus)
print(Torun.__total_altin)
"""

"""
class MyClass():
    x = 5

print(MyClass.x)
a = MyClass()
print(type(a))
print(a.x)
"""

"""
class Person:
    def __init__(self,name="Adsız",age=0):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1)
print(p1.name)
print(p1.age)

p2 = Person()

print(p2.name)
print(p2.age)
"""

"""
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self,fname,lname,bolum):
        Person.__init__(self,fname,lname)
        self.bolum = bolum

x = Student("Mike", "Olsen", "YBS")
x.printname()
print(x.bolum)
"""

"""
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

x = Student("Mike", "Olsen")
x.printname()
"""

"""
import sqlite3 as sql

vt = sql.connect('kitaplik.sqlite')
imlec = vt.cursor()
try:
    imlec.execute('CREATE TABLE IF NOT EXISTS kitap_bilgisi (kitap_adi,kitap_yazari,okunma_durumu,begeni)')
    # IF NOT EXISTS sayesinde kod aşağıdaki hatayı artık vermiyor
except:
    print("tablo zaten vardı, oluşturmadı")

kitap_girisi = "INSERT INTO kitap_bilgisi VALUES ('Suç ve Ceza', 'Dostoyevski', 'hayır','*****')"

imlec.execute(kitap_girisi)
imlec.execute("INSERT INTO kitap_bilgisi VALUES ('Beyaz Diş', 'Jack LONDON', 'evet','***')")

imlec.execute("INSERT INTO kitap_bilgisi VALUES ('Yunan Mitolojisi', 'Anna', 'hayır','****')")
vt.commit()

vt.close()
"""

"""
import os
import sqlite3 as sql
veritabani = 'kitaplik.sqlite'
dosya_mevcut = os.path.exists(veritabani)

vt = sql.connect(veritabani)
imlec = vt.cursor()
# imlec.execute("UPDATE kitap_bilgisi SET begeni = '****' WHERE begeni='***'")
# imlec.execute("UPDATE kitap_bilgisi SET okunma_durumu = 'evet' WHERE okunma_durumu = 'hayır'")

imlec.execute("DELETE FROM kitap_bilgisi WHERE okunma_durumu = 'hayır'")

vt.commit()

vt = sql.connect(veritabani)
imlec = vt.cursor()
imlec.execute("SELECT * FROM kitap_bilgisi")
kitaplar = imlec.fetchall()
print(kitaplar)
for i in kitaplar:
    for k in i:
        print(k,end=" ")
    print("")

vt.close()
"""

"""
# veritabanı oluşturmak
#sqlite3 modülünü dahil ediyoruz
import sqlite3 as sql
vt = sql.connect('kitaplik.sqlite') # bağlanacak olduğumuz veri tabanının adını
# yazıyoruz eğer sistemde adını yazdığımız veri tabanı yoksa yazılan adda
# bir veri tabanı oluşturuluyor
imlec = vt.cursor() # veri tabanı üzerinde işlem yapmak için imleç oluşturuyoruz
imlec.execute("CREATE TABLE IF NOT EXISTS ozel (kitap_id INTEGER PRIMARY KEY  "
              "AUTOINCREMENT, kitap_adi ,kitap_yazari,okunma_durumu,begeni)")
#kitap bilgisi adında içerisine bir tablşo oluşturuyoruz ilgili alanlar ile birlikte
# hata almamak için IF NOT EXISTS varlık kontrolü
kitap_girisi = ("INSERT INTO ozel (kitap_adi,kitap_yazari,okunma_durumu,begeni) "
                "VALUES ('Suç ve Ceza', 'Dostoyevski', 'evet','*****')")
kitap_girisi_2=("INSERT INTO ozel (kitap_adi,kitap_yazari,okunma_durumu,begeni) "
                "VALUES ('Beyaz Diş', 'Jack LONDON', 'evet','***')")
imlec.execute(kitap_girisi)
imlec.execute(kitap_girisi_2)
vt.commit() # veri tabanına hafızadaki bilgiyi kaydetmek için
vt.close() # veri tabanını kapatmak için
"""


import sys
import veritabani_06 as baglanti

print("-"*56)
print("-"*10, "Kitaplık Programımıza Hoş Geldiniz", "-"*10)
print("-"*56)
while 1 == 1:
    print("-"*10, "Yapmak istediğiniz işlemi Seçiniz", "-"*10)
    print("-" * 10, "(E)klemek,(L)istelemek,(G)üncellemek,(S)ilmek,(Ç)ıkmak", "-" * 10)
    islem = input()
    if islem == "Ç" or islem == "ç":
        baglanti.cikis()
        sys.exit()
    elif islem == "E" or islem == "e":
        kitap = input("kitap adını giriniz")
        yazar = input("kitap yazarını")
        okunma = input("kitap okunma durumunu giriniz")
        begeni = input("kitap beğeni değerini giriniz")
        baglanti.ekle(kitap, yazar, okunma, begeni)
    elif islem == "L" or islem == "l":
        baglanti.listele()
    elif islem == "G" or islem == "g":
        baglanti.listele()
        guncellenecek = input("güncellemek istediğiniz kitabın id'sini giriniz")
        baglanti.guncelle(guncellenecek)
    elif islem == "S" or islem == "s":
        baglanti.listele()
        silinecek = input("silmek istediğiniz kitabın id'sini giriniz")
        baglanti.sil(silinecek)
    elif islem == "T" or islem == "t":
        print("\nSayı Tahmini Oyununa Hoş Geldiniz!")
        print("1 ile 100 arasında rastgele bir sayı seçildi.")
        
        hedef_sayi = random.randint(1, 100)
        tahmin_hakki = 5
        
        while tahmin_hakki > 0:
            print("\nKalan Tahmin Hakkınız:", tahmin_hakki)
            
            try:
                tahmin = int(input("Tahmininizi girin (1 ile 100 arasında): "))
            except ValueError:
                print("Geçerli bir sayı girin.")
                continue
            
            if tahmin < 1 or tahmin > 100:
                print("Lütfen 1 ile 100 arasında bir sayı girin.")
                continue
        
            if tahmin == hedef_sayi:
                print("Tebrikler! Doğru tahmin ettiniz. Hedeflenen sayı:", hedef_sayi)
                break
            elif tahmin < hedef_sayi:
                print("Daha yüksek bir sayı girin.")
            else:
                print("Daha düşük bir sayı girin.")
            
            tahmin_hakki -= 1
        
        if tahmin_hakki == 0:
            print("\nTahmin hakkınız tükendi. Hedeflenen sayı:", hedef_sayi)
