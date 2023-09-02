"""
baslangic = 3
bitis = 15
artis = 2
for dd in range (baslangic, bitis, artis):
    print(dd)
"""
"""
pizza_dilim = int(input("Kaç dilim pizza yemek istersiniz? "))

for dilim in range(1, pizza_dilim + 1):
    print(f"{dilim}. dilim pizzanız")
    input("Dilimi yediniz mi? (Eğer yediyseniz Enter'a basın)")

print("Afiyet olsun")
"""
"""
toplam = 0
for dd in range(10):
    toplam += dd
    print(dd,toplam)
"""
"""
toplam = 0
baslangic = 37
bitis = 100
artis = 2
for dd in range(baslangic, bitis, artis):
    toplam += dd
    print(dd,toplam)
"""
"""
sayi = int(input("Faktöriyelini hesaplamak istediğiniz bir sayı girin: "))

faktoriyel = 1
for dd in range(1, sayi + 1):
    faktoriyel *= dd

print(f"{sayi}! = {faktoriyel}")
"""
"""
isim = input("Ad girin: ")
sira = int(input("Kaçıncı harfi yazdırmak istersiniz? (1'den başlayarak): "))

gercek_harf_sayaci = 0
hedef_harf = ""

for harf in isim:
    if harf != " ":
        gercek_harf_sayaci += 1
        if gercek_harf_sayaci == sira:
            hedef_harf = harf
            break

if hedef_harf:
    print(f"{isim} isminin {sira}. gerçek harfi: {hedef_harf}")
else:
    print("Geçersiz sıra numarası !")
"""
"""
a = 0
toplam = 0
while a<=10:
    for dd in range (a):
        toplam += dd
        print(a, toplam)
    a += 1
"""
"""
for dd in range(10):
    if dd == 5:
        continue # döngünün kendisinden sonra kaldığı yerden devam etmesini sağlar
    print(dd)
"""
"""
sayac = 0
carpim = 1
while True:
    sayi = int(input("Bir sayı girin: "))
    if sayi == 0 or sayac == 10:
        print("girdiğiniz sayıların çarpımı", carpim)
        break
    sayac += 1
    carpim *= sayi
"""
"""
adet = int(input("Kaç tane sayıyı hesaplamak istiyorsun: "))
carpim = 1
while True:
    sayi = int(input("Bir sayı giriniz: "))
    if sayi == 0 or adet == 0:
        print("Girdiğiniz sayıların çarpımı:", carpim)
        break
    adet -= 1
    if sayi == 111:
        continue
    carpim *= sayi # suppose 2^5 hesaplayacaksın. 5 kere 2 girmen gerekirken 6 kere 2 giriyorsun ancak sonucu doğru bir şekilde 32 olarak printliyor.
"""
"""
ders_sayisi = int(input("Toplam kaç dersin var : "))
genel_ortalama_toplami = 0
for ders in range(1, ders_sayisi + 1):
    print(ders, ", derste kaç sınavınız var : ")
    sinav_sayisi = int(input())
    toplam = 0
    for sinav in range(1,sinav_sayisi+1):
        print(ders, "dersinin,", sinav, "sınav notu")
        sinav_puani = int(input())
        toplam += sinav_puani
    ortalama = toplam/sinav_sayisi
    genel_ortalama_toplami += ortalama
sonuc_ortalamasi = genel_ortalama_toplami/ders_sayisi
print("derslerinizin genel ortalaması ", sonuc_ortalamasi)
"""
"""
tek_toplam = 0
tek_sayac = 0
cift_toplam = 0
cift_sayac = 0

for _ in range(20):
    sayi = int(input("Bir sayı girin: "))
    if sayi % 2 == 0:
        cift_toplam += sayi
        cift_sayac += 1
    else:
        tek_toplam += sayi
        tek_sayac += 1

if tek_sayac > 0:
    tek_ortalama = tek_toplam / tek_sayac
    print(f"Tek sayıların ortalaması: {tek_ortalama:.2f}")

if cift_sayac > 0:
    cift_ortalama = cift_toplam / cift_sayac
    print(f"Çift sayıların ortalaması: {cift_ortalama:.2f}")
"""

#yöntem 1
"""
sayimiz = 42
while True:
    tahmin = int(input("Bir sayı girin: "))
    
    if tahmin != sayimiz:
        print("Yanlış, bir kez daha dene!")
        if tahmin < sayimiz:
            print("Daha büyük bir sayı girmelisiniz.")
        elif tahmin > sayimiz:
            print("Daha küçük bir sayı girmelisiniz.")
    else:
        print("Tebrikler, Kazandınız!")
        break
"""
#yöntem 2
"""
tutulan = 42
tahmin = int(input("Bir sayı giriniz: "))
while not(tutulan == tahmin):
    if tahmin > tutulan:
        tahmin = int(input("Daha küçük bir sayı giriniz: "))
    else:
        tahmin = int(input("Daha büyük bir sayı giriniz: "))
else:
    print("Tebrikler, Kazandınız!")
"""
