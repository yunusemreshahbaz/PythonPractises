print("asda")
print(type(print("asd")))

"""
a,b = 5,10
print(a,b)
c = a
print(a,b,c)
a = b
print(a,b,c)
b = c
print (a,b,c)
"""
"""
a,b = 5,10
print(a,b)
a,b = b,a
print(a,b)
"""
"""
print("Adınız?")
ad = input()
print("Yaşınız?")
yas = int(input())
print("Not ortalamanız?")
avg = float(input())
print("En sevdiğiniz sayı?")
sayi = int(input())
print("Merhaba",ad,"! Siz",yas,"yasindasiniz. Not ortalamanız",avg,"ve en sevdiğiniz sayı",sayi)
"""
"""
print((4-1)**2,(7//3)/2) #9,1
"""
"""
print("Otoban uzunluğu (km) ?")
yol = float(input())
print("Geçen süre (saat) ?")
zaman = float(input())
hız = yol/zaman
print("Hızınız:",hız)
hız_limiti = 120
if hız > hız_limiti:
    ceza_tutari = (hız - hız_limiti)*5
    print(f"Hız limitini {hız_limiti} km/saat aştınız !")
    print(f"Ceza tutarı: {ceza_tutari} TL")
else:
    print("Hız limiti içinde seyahat ediyorsunuz, ceza almadınız.")
"""
"""
def main():
    yevmiye = 350
    try:
        calisma_gun_sayisi = int(input("Çalışma gün sayısını giriniz: "))
        
        if calisma_gun_sayisi <= 0:
            print("Geçerli bir çalışma gün sayısı giriniz.")
        else:
            yevmiye_toplam = yevmiye * calisma_gun_sayisi
            print(f"{calisma_gun_sayisi} gün çalıştığınızda yevmiye tutarı: {yevmiye_toplam} TL")
    except ValueError:
        print("Geçerli bir sayı girmelisiniz.")

if __name__ == "__main__":
    main()
"""
"""
print("Adınız ?")
ad = input()
if ad == "Yunus":
    print("Adaşız seninle")
else:
    print("adaş değiliz")
"""
"""
print("Not ortalamanız ?")
avg = int(input())
if 100>=avg>=0:
    if avg >= 85:
        print("Takdir'e hak kazandınız")
    elif avg >= 70 and avg<85:
        print("Teşekkür'e hak kazandınız")
    elif avg<70:
        print("Bir halt alamadın")
else:
    print("Hatalı girdi")
"""
"""
gun = input("hangi gün? ")
if gun == "pazartesi":
    print(1)
elif gun == "salı":
    print(2)
else:
    print(3)
"""
"""
memleket = input("hangi memleket? ")
if memleket == "amasya":
    print("hemşeriyiz")
else:
    print("hemşeri değiliz")
"""
"""
print("ilk sayıyı girin")
sayi = int(input())
print("ikinci sayıyı girin")
sayii = int(input())
if sayi > sayii:
    print(sayi,sayii)
elif sayi == sayii:
    print(sayi,sayii)
elif sayi < sayii:
    print(sayii,sayi)
else:
    print("Hatalı girdi")   
"""
"""
print("ilk sayıyı girin")
sayi = int(input())
print("ikinci sayıyı girin")
sayii = int(input())
print("üçüncü sayıyı girin")
sayiii = int(input())
if sayi > sayii and sayi > sayiii:
    if sayii > sayiii:
        print(sayi,sayii,sayiii)
    elif sayiii > sayii:
        print(sayi,sayiii,sayii)
elif sayii > sayi and sayii > sayiii:
    if sayi > sayiii:
        print(sayii,sayi,sayiii)
    elif sayiii > sayi:
        print(sayii,sayiii,sayi)
elif sayiii > sayi and sayiii > sayii:
    if sayi > sayii:
        print(sayiii,sayi,sayii)
    elif sayii > sayi:
        print(sayiii,sayii,sayi)
else:
    print("hatalı girdi")
"""
"""
print("birinci ort:")
avg = int(input())
print("ikinci ort:")
avgg = int(input())
print("üçüncü ort:")
avggg = int(input())
mavg = (avg+avgg+avggg)/3
if mavg == 100:
    print("dersi direkt geçtin!")
elif 100>mavg>=85:
    print("dersi geçtin")
elif 85>mavg>=60:
    print("dersten kalmadın, devam")
elif 60>mavg>=0:
    print("dersten kaldın")
else:
    print("hatalı girdi")
"""
"""
email = input("E-posta adresini girin: ")
if "@" in email:
    print("Geçerli bir mail adresi girdiniz.")
else:
    print("Geçersiz mail adresi!")
"""
"""
programlama_dili = input("Sevdiğiniz programlama dilini girin (python, java, c#, javascript): ")
if programlama_dili == "python":
    print("Python'u Guido van Rossum geliştirmiştir.")
elif programlama_dili == "java":
    print("Java'yı James Gosling geliştirmiştir.")
elif programlama_dili == "c#":
    print("C#'ı Anders Hejlsberg geliştirmiştir.")
elif programlama_dili == "javascript":
    print("JavaScript'i Brendan Eich geliştirmiştir.")
else:
    print("Geçerli bir programlama dili giriniz.")
"""
"""
ad = "yunus"
print(len(ad))
"""
"""
ad = "yunusemresahbaz"
print(len(ad))
print(ad[5])
print(ad[-5])
print(ad[::])
print(ad[:5])
print(ad[5:])
print(ad[5:8])
print(ad[::2])
print(ad[3:10:3])

print(ad[::-1])
print(ad[-8:-5])
print(ad[-5:-8:-1])
"""
"""
ad1 = "Recep"
ad2 = "ilayda"
ad3 = "esra"
metin = "Merhaba {} eğitime hoşgeldiniz"
print(metin.format(ad1))
print(metin.format(ad2))
print(metin.format(ad3))
print(metin)
metin2 = "Merhaba {}, {}, {} eğitime hoşgeldiniz"
print(metin2.format(ad1,ad2,ad3))
metin3 = "Merhaba {k1}, {k2}, {k3} eğitime hoşgeldiniz ".format(k1 = ad2, k2 = ad1, k3 = ad3)
print(metin3)
"""

print("txt1",end="")
print("txt2")
print("txt1",end="\n")
print("txt2")
print("txt1",end="\t BTK \t")
print("")
print("txt1", "txt2", "txt3",sep="")
print("txt1", "txt2", "txt3",sep=",")
