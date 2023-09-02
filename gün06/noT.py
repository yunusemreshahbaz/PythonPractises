"""
yazdir = print
yazdir("merhaba")
giris = input
tamsayi = int
tamsayi_giris = tamsayi(giris())
sayi = tamsayi_giris()
yazdir(sayi)
"""
"""
def selamla():
    print("Merhaba Derse Hoşgeldiniz")

mesaj = selamla()
print(mesaj)
print(type(mesaj))
print(selamla())
"""
"""
def Pi():
   # print("Pi fonksiyonu çalıştı")
   # return 3.14

   pi_degeri = float(input("Bir pi değeri giriniz: "))
   return pi_degeri

donus = Pi()
print(donus)
print(type(donus))
cevre = Pi()*5**2
print(cevre)
print(type(Pi()))
"""
"""
def kare(a):
    return a**2

sayi = int(input("Hangi sayının karesini hesaplayalım: "))
deger = kare(sayi)
print(deger)
"""
"""
def daire(pi,r):
    alan = pi * (r**2)
    return alan

print(daire(3.14159265, 5))
"""
"""
def sayiyazdir(*sayilar):
    x = [*sayilar]
    print(x)
    for sayi in x:
        print(sayi)
sayiyazdir(1,2,3,4,5,6)
"""

"""
# **kwargs -> keywordli argumanlar almamızı sağlar
def o_karti(**kwargs):
    print(kwargs)
    o_bilgiler = {**kwargs}
o_karti(o_adi="Yunus",o_no=35,o_sehir="İzmir")
"""
"""
def faktoriyel(n):
    if n>0:
        return n * faktoriyel(n-1)
    elif n == 0:
        return 1
    else:
        print("hata")

sayi = int(input("Hangi sayının faktoriyelini hesaplayalım: ))
"""
"""
def o_listesi(liste):
    if not liste:
        return
    else:
        print(liste[0])
        o_listesi(liste[1:])

liste = ["Ali", "Veli", "Can"]
o_listesi(liste)

print()
print(o_listesi(["Ahmet","Ayşe","Cem"]))
"""
"""
def birinci():
    print("Program başlatma fonksiyonu")
    ikinci()

def ikinci():
    print("sonradan çalışan fonksiyon")

if __name__ == '__main__':
    birinci()
"""
"""
from math import sqrt

def asal(n):
    kok=round(sqrt(n))+1
    kontrol = 0
    for deneme in range(2,kok):
        if n % deneme == 0:
            kontrol += 1
    return True if kontrol == 0 else False

def main():
    en_buyuk = int(input("Asal sayıları hangi değere kadar gösterelim? "))
    for deger in range(2,en_buyuk+1):
        if asal(deger):
            print(deger,end=" ")
print()
main()
"""

