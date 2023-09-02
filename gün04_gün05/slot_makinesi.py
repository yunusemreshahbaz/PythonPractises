def kayit_ol():
    ad = input("Adınızı girin: ")
    soyad = input("Soyadınızı girin: ")
    sifre = input("Şifrenizi girin: ")
    kredi = int(input("Yüklemek istediğiniz kredi miktarını girin: "))
    
    with open("C:\\Users\\Yunus_Emre\\Desktop\\hesaplar.txt", "a") as dosya:
        dosya.write(f"{ad} {soyad} {sifre} {kredi}\n")
    print("Kaydınız başarıyla oluşturuldu.")

def giris_yap():
    ad = input("Adınızı girin: ")
    soyad = input("Soyadınızı girin: ")
    sifre = input("Şifrenizi girin: ")
    
    with open("C:\\Users\\Yunus_Emre\\Desktop\\hesaplar.txt", "r") as dosya:
        hesaplar = dosya.readlines()
        for hesap in hesaplar:
            bilgiler = hesap.strip().split()
            if ad == bilgiler[0] and soyad == bilgiler[1] and sifre == bilgiler[2]:
                return int(bilgiler[3])
    
    return None

def main():
    while True:
        print("Hoşgeldiniz!")
        secenek = input("Giriş yapmak için 'giriş yap', kaydolmak için 'kaydol' yazın (Çıkmak için 'q'): ").lower()
        
        if secenek == "q":
            break
        elif secenek == "kaydol":
            kayit_ol()
        elif secenek == "giriş yap":
            kredi = giris_yap()
            
            if kredi is None:
                print("Hesap bulunamadı, lütfen tekrar deneyiniz.")
                continue
            
            print(f"Hoşgeldiniz {ad} {soyad}")  # Bu satırda ad ve soyad değişkenlerini eklemelisin
            print(f"Bakiyeniz: {kredi} TL")
            
            while True:
                oyun_soru = input("Oynamak ister misiniz? (E/H): ").lower()
                if oyun_soru == "h":
                    break
                elif oyun_soru == "e":
                    if kredi < 1:
                        print("Bakiye yetersiz, lütfen kredi yükleyiniz.")
                        continue
                    
                    bahis = int(input("Bahis miktarını girin (1/5/10 TL): "))
                    if bahis not in [1, 5, 10]:
                        print("Geçersiz bahis miktarı. Lütfen 1, 5 veya 10 TL girin.")
                        continue
                    
                    kredi -= bahis
                    
                    # Oyunun geri kalanı burada devam ediyor
                    
                    print(f"Toplam krediniz: {kredi} TL")
                else:
                    print("Geçersiz seçenek, lütfen 'E' veya 'H' girin.")
        else:
            print("Geçersiz seçenek.")

if __name__ == "__main__":
    main()
