"""
import random
print(random.random())
print(random.randrange(1,49))
"""
"""
import random
print(random.random())
rastgele = random.randrange(1,100)
tahminSayisi = 10
taban = 0
tavan = 101
while tahminSayisi >= 1:
    tahmin = int(input(f'{taban} - {tavan} arasında bir sayı giriniz: '))
    if tahmin == rastgele:
        print("Tebrikler")
        break
    elif tahmin > rastgele:
        tavan = tahmin
    elif tahmin < rastgele:
        taban = tahmin
    tahminSayisi -= 1
    print("kalan hakkınız", tahminSayisi)
"""
"""
import random
taban = 1
tavan = 100
tutulan_sayi = random.randint(taban, tavan)
deneme_sayisi = 0
    
while True:
    tahmin = random.randint(taban, tavan)
    deneme_sayisi += 1
        
    if tahmin == tutulan_sayi:
        print(f"Tebrikler! {deneme_sayisi}. denemede sayıyı buldunuz: {tutulan_sayi}")
        break
    elif tahmin < tutulan_sayi:
        print(f"{deneme_sayisi}. deneme: {tahmin}. Tahmininiz daha düşük. Aralık: [{tahmin}-{tavan}]")
        taban = tahmin
    elif tahmin > tutulan_sayi:
        print(f"{deneme_sayisi}. deneme: {tahmin}. Tahmininiz daha yüksek. Aralık: [{taban}-{tahmin}]")
        tavan = tahmin
"""


"""
import datetime
import time
time.sleep(5)
a = input("ilk bilgiyi giriniz: ")
giris = datetime.datetime.now()
b = input("ikinci bilgiyi giriniz: ")
cikis = datetime.datetime.now()
fark = cikis - giris
print(fark.microseconds)
"""
"""
import time
for dd in range(10):
    print("Yunus Emre")
    time.sleep(5)

print("Program sonlandı.")
"""

"""
# 10000'e kadar olan asal sayıların adedi ve bulurken geçen zaman
from time import perf_counter

sonDeger = 10000
sayac = 0
zaman = perf_counter() # Süre başlatılıyor
# En küçük asal sayı olan 2'den istenilen değere kadar döngü kuruluyor
for deger in range(2, sonDeger + 1): # Sırayla sayılar ele alınıyor
    kontrol = True # Değerlerin kontrol edilmesi için ilk değer True veriliyor
# Asal olma özelliğinin kontrolü için bölenlerinin döngüsü kuruluyor
    for bolenSayi in range(2, deger):
        if deger % bolenSayi == 0:
            kontrol = False # Tam bölme işlemi oluştuysa kontrol False yapılıyor
            break # ve döngü sonlandırılıyor

    if kontrol:
        sayac += 1 # Asal olma özelliği sağlanmışsa sayac arttırılıyor

print() # Yeni satır başı
gecenZaman = perf_counter() - zaman # İşlem tamamlandıktan sonra süre sonlandırılıyor
print("Adet:", sayac, " Geçen Zaman:", gecenZaman, " saniye")
"""

"""
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist))
print(type(thislist))

thislist2 = list(("apple", "banana", "cherry"))
print(thislist2[1])

list1 = [1, 2, 3, 4]
print(list1[-1]) # sonuncu itemi printler

# list2 = [True, False, False]

# list3 = ["abc", 34, True, 40, "male"]

thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist3[2:5]) # 3 4 ve 5. itemleri printler
print(thislist3[:4]) # baştan ilk 4 itemi printler
print(thislist3[2:]) # baştaki ilk 2 item hariç listenin sonundaki iteme kadar printler
print(thislist3[-4:-1]) # 4. itemden başlayıp sonuna kadar yazdırır (son item hariç)

if "apple" in thislist3:
	print("Yes, 'apple' is in the fruits list")

thislist3[0] = "changed apple"
if "apple" in thislist3:
	print("Yes, 'apple' is in the fruits list")
else:
	print("No, 'apple' is not in the fruits list")

print(thislist3)

thislist3[1:3] = ["changed banana", "changed cherry"]
print(thislist3)

thislist3.insert(3, "inserted avacado")
print(thislist3)

thislist3.append("added pineapple")
print(thislist3)

# append: listenin sonuna ekler
# insert: listenin istediğimiz yerine ekleriz

thislist3.extend(list1) # list1'in elementlerini thislist3'ün sonuna ekledik
print(thislist3)

thistuple = ("kiwi", "orange")
thislist3.extend(thistuple)
# extend ile sadece listeleri değil tuple, directory, set'leri de ekleyebilirsin
print(thislist3)

thislist3.remove("changed apple")
# remove: eğer birden fazla varsa karşılaştığı ilk 'changed apple' itemini siler
print(thislist3)

thislist3.pop(0) # belli indexi silmek için kullanılır
print(thislist3)
"""

"""
dosya = open("deneme.txt", "r")
metin = dosya.read()
print(len(metin))
"""
"""
dosya_yolu = r"C:\Users\Yunus_Emre\Desktop\deneme.txt"

try:
    with open(dosya_yolu, "a") as dosya:
        
        icerik = dosya.read()
        print(icerik)
        print("Dosya uzunluğu:", len(icerik))

       # VEYA (satır satır okuması için)
        
       # for satir in dosya.readlines():
       #     print(satir)
       # print("Dosya uzunluğu:", len(satir)) # Son satırın uzunluğunu print eder


except FileNotFoundError:
    print("Dosya bulunamadı.")
"""
