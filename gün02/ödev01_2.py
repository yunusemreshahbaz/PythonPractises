not1 = 64
not2 = 86
not3 = 70
sum = not1 + not2 + not3
avg = sum/3
print(avg)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")

print("Adınız nedir ?")
ad = input()
print(ad,"yaşın kaç ?")
yas = int(input())
print(ad*yas)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")

print("Pi değeri ne olsun ?")
pi = float(input())
print("Dairenin yarı çap değeri ne olsun ?")
yaricap = float(input())
daire_cevresi = 2*pi*yaricap
daire_alani = pi*(yaricap**2)
print("Dairenin Çevresi : ", daire_cevresi)
print("Dairenin Alanı : ", daire_alani)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")

from datetime import datetime

simdi = datetime.now()

dogum_tarihi = input("Doğum tarihinizi (GG.AA.YYYY) formatında girin: ")

gun, ay, yil = map(int, dogum_tarihi.split('.'))

yas = simdi.year - yil - ((simdi.month, simdi.day) < (ay, gun))

if yas >= 18:
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet almak için henüz yaşınız uygun değil.")
    
print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")

