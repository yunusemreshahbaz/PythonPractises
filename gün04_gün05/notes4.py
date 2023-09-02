import random
import os

dosya_yolu = "C:\\Users\\Yunus_Emre\\Desktop\\deneme2.txt"

hedef_sayi = random.randint(1, 10)

while True:
    tahmin = int(input("1 ile 10 arasında bir sayı tahmin edin: "))
    
    if tahmin == hedef_sayi:
        print("Tebrikler! Doğru tahmin ettiniz.")
        break
    else:
        print("Yanlış tahmin. Tekrar deneyin.")
        try:
            os.remove(dosya_yolu)
            print(f"{dosya_yolu} dosyası silindi.")
        except FileNotFoundError:
            print(f"{dosya_yolu} dosyası bulunamadı")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
            
