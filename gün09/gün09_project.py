
import sqlite3 as sql
import sys

vt = sql.connect('kitaplik_db.sqlite')
imlec = vt.cursor()

def kullanici_kutuphanesi_goruntule(kullanici_id):
    sorgu = "SELECT kitap_id, kitap_adi, kitap_yazari, okunma_durumu, begeni FROM kitaplik_tb WHERE kullanici_id = ?"
    imlec.execute(sorgu, (kullanici_id,))
    kitaplar = imlec.fetchall()
    
    if not kitaplar:
        print("Kütüphaneniz boş.")
    else:
        print("Kütüphanenizdeki kitaplar:")
        for kitap in kitaplar:
            print(f"Kitap Adı: {kitap[1]}")
            print(f"Yazar: {kitap[2]}")
            print(f"Okunma Durumu: {'Okundu' if kitap[3] else 'Okunmadı'}")
            print(f"Beğeni: {kitap[4]}")
            print("-" * 30)

def kitap_ekle(kullanici_id, kitap_adi, kitap_yazari, okunma_durumu, begeni):
    sorgu = "INSERT INTO kitaplik_tb (kitap_adi, kitap_yazari, okunma_durumu, begeni, kullanici_id) VALUES (?, ?, ?, ?, ?)"
    imlec.execute(sorgu, (kitap_adi, kitap_yazari, okunma_durumu, begeni, kullanici_id))
    vt.commit()
    print("Kitap başarıyla eklendi.")

def kitap_guncelle(kullanici_id, kitap_id, okunma_durumu, begeni):
    sorgu = "UPDATE kitaplik_tb SET okunma_durumu = ?, begeni = ? WHERE kitap_id = ? AND kullanici_id = ?"
    imlec.execute(sorgu, (okunma_durumu, begeni, kitap_id, kullanici_id))
    vt.commit()
    print("Kitap bilgileri güncellendi.")

def kitap_sil(kullanici_id, kitap_id):
    sorgu = "DELETE FROM kitaplik_tb WHERE kitap_id = ? AND kullanici_id = ?"
    imlec.execute(sorgu, (kitap_id, kullanici_id))
    vt.commit()
    print("Kitap başarıyla silindi.")

def kullanici_kayit():
    ad = input("Adınız: ")
    soyad = input("Soyadınız: ")
    eposta = input("E-posta adresiniz: ")
    sifre = input("Şifreniz: ")
    
    # E-posta adresinin veritabanında daha önce kaydedilip kaydedilmediğini kontrol eder:
    imlec.execute("SELECT * FROM kullanici_bilgileri WHERE eposta = ?", (eposta,))
    var_mi = imlec.fetchone()
    
    if var_mi:
        print("Bu e-posta adresi zaten kayıtlı.")
    else:
        imlec.execute("INSERT INTO kullanici_bilgileri (ad, soyad, eposta, sifre) VALUES (?, ?, ?, ?)", (ad, soyad, eposta, sifre))
        vt.commit()
        print("Kayıt başarıyla tamamlandı. Giriş yapabilirsiniz.")

    

def kullanici_giris():
    eposta = input("E-posta adresiniz: ")
    sifre = input("Şifreniz: ")
    
    imlec.execute("SELECT * FROM kullanici_bilgileri WHERE eposta = ? AND sifre = ?", (eposta, sifre))
    kullanici = imlec.fetchone()
    
    if kullanici:
        print(f"Merhaba, {kullanici[1]} {kullanici[2]}! Giriş başarılı.")
        return kullanici[0]  # Kullanıcı kimliğini döndür
        
    else:
        print("Hatalı e-posta veya şifre. Tekrar deneyin.")
        return None

# Ana döngü
while True:
    print("-" * 56)
    print("-" * 10, "Kitaplık Programımıza Hoş Geldiniz", "-" * 10)
    print("-" * 56)
    
    print("-" * 10, "Yapmak istediğiniz işlemi Seçiniz", "-" * 10)
    print("-" * 10, "(1) Giriş Yap, (2) Kayıt Ol, (3) Çıkış", "-" * 10)
    islem = input()
    
    if islem == "1":
        kullanici_id = kullanici_giris()
        if kullanici_id is not None:
            # Başarılı girişten sonra ana menüye dönüş:
            while True:
                print("-" * 56)
                print("-" * 10, "Kitaplık Programımıza Hoş Geldiniz", "-" * 10)
                print("-" * 56)
                
                print("-" * 10, "Yapmak istediğiniz işlemi Seçiniz", "-" * 10)
                print("-" * 10, "(1) Kütüphanemi Görüntüle, (2) Kitap Ekle, (3) Kitap Güncelle, (4) Kitap Sil, (5) Çıkış", "-" * 10)
                alt_islem = input()
                
                if alt_islem == "1":
                    kullanici_kutuphanesi_goruntule(kullanici_id)
                elif alt_islem == "2":
                    kitap_adi = input("Kitap adını giriniz: ")
                    kitap_yazari = input("Kitap yazarını giriniz: ")
                    okunma_durumu = input("Okunma durumunu giriniz (1: Okundu, 0: Okunmadı): ")
                    begeni = input("Beğeni değerini giriniz: ")
                    kitap_ekle(kullanici_id, kitap_adi, kitap_yazari, okunma_durumu, begeni)
                elif alt_islem == "3":
                    kitap_id = input("Güncellemek istediğiniz kitabın ID'sini giriniz: ")
                    okunma_durumu = input("Yeni okunma durumu (1: Okundu, 0: Okunmadı): ")
                    begeni = input("Yeni beğeni değeri: ")
                    kitap_guncelle(kullanici_id, kitap_id, okunma_durumu, begeni)
                elif alt_islem == "4":
                    kitap_id = input("Silmek istediğiniz kitabın ID'sini giriniz: ")
                    kitap_sil(kullanici_id, kitap_id)
                elif alt_islem == "5":
                    break  # Alt menüden çıkış yap
                else:
                    print("Geçersiz işlem. Lütfen tekrar deneyin.")
    elif islem == "2":
        kullanici_kayit()
    elif islem == "3":
        vt.close()
        sys.exit()
    else:
        print("Geçersiz işlem. Lütfen tekrar deneyin.")
