"""
import sqlite3 as sql
vt = sql.connect('kitaplik_db.sqlite')
imlec = vt.cursor()

def ekle(kitap_adi="",kitap_yazari="",okunma_durumu="",begeni=""):
    imlec.execute(
        "CREATE TABLE IF NOT EXISTS kitaplik_tb (kitap_id INTEGER PRIMARY KEY  AUTOINCREMENT, kitap_adi,kitap_yazari,okunma_durumu,begeni)")
#    print(kitap_adi,kitap_yazari,okunma_durumu,begeni)
    kitap_girisi = "INSERT INTO kitaplik_tb (kitap_adi,kitap_yazari,okunma_durumu,begeni) VALUES ('"+kitap_adi+"','"+kitap_yazari+"','"+okunma_durumu+"','"+begeni+"')"
#    print(kitap_girisi)
    imlec.execute(kitap_girisi)
    vt.commit()
def listele():
    imlec.execute("SELECT * FROM kitaplik_tb")
    kitaplar = imlec.fetchall()
#    print(kitaplar)
    for i in kitaplar:
        for k in i:
            print(k, end=" ")
        print("")

def guncelle(guncellenecek):
    gkitap = input("Güncel kitap adını giriniz")
    gyazar = input("Güncel kitap yazarını")
    gokunma = input("Güncel kitap okunma durumunu giriniz")
    gbegeni = input("Güncel kitap beğeni değerini giriniz")
    guncelleme_kodu = "UPDATE kitaplik_tb SET kitap_adi='"+gkitap+"',kitap_yazari='"+gyazar+"',okunma_durumu='"+gokunma+"',begeni='"+gbegeni+"' WHERE kitap_id = '"+guncellenecek+"'"
    imlec.execute(guncelleme_kodu)
    vt.commit()
def sil(silinecek):
    silme_kodu="DELETE FROM kitaplik_tb WHERE kitap_id='"+silinecek+"'"
    imlec.execute(silme_kodu)
    vt.commit()
def cikis():
    vt.close()
    print("Çıkış Yapıldı İyi Günler")
"""


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
"""

"""
import sys
import veritabani_06 as baglanti

def ana_menu():
    print("-"*56)
    print("-"*10, "Kitaplık Programımıza Hoş Geldiniz", "-"*10)
    print("-"*56)

def kitap_ekle():
    kitap = input("kitap adını giriniz: ")
    yazar = input("kitap yazarını: ")
    okunma = input("kitap okunma durumunu giriniz: ")
    begeni = input("kitap beğeni değerini giriniz: ")
    baglanti.ekle(kitap, yazar, okunma, begeni)

def kitap_listele():
    baglanti.listele()

def kitap_guncelle():
    baglanti.listele()
    guncellenecek = input("güncellemek istediğiniz kitabın id'sini giriniz: ")
    baglanti.guncelle(guncellenecek)

def kitap_sil():
    baglanti.listele()
    silinecek = input("silmek istediğiniz kitabın id'sini giriniz: ")
    baglanti.sil(silinecek)

def main():
    while True:
        ana_menu()
        print("-"*10, "Yapmak istediğiniz işlemi Seçiniz", "-"*10)
        print("-" * 10, "(E)klemek,(L)istelemek,(G)üncellemek,(S)ilmek,(Ç)ıkmak", "-" * 10)
        islem = input()
        if islem == "Ç" or islem == "ç":
            baglanti.cikis()
            sys.exit()
        elif islem == "E" or islem == "e":
            kitap_ekle()
        elif islem == "L" or islem == "l":
            kitap_listele()
        elif islem == "G" or islem == "g":
            kitap_guncelle()
        elif islem == "S" or islem == "s":
            kitap_sil()

if __name__ == "__main__":
    main()
"""

"""
import sqlite3 as sql

# Veritabanı bağlantısını oluştur
vt = sql.connect('kitaplik.sqlite')
imlec = vt.cursor()

# Kullanıcı kütüphanesini görüntüle
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

# Kitap ekle
def kitap_ekle(kullanici_id, kitap_adi, kitap_yazari, okunma_durumu, begeni):
    sorgu = "INSERT INTO kitaplik_tb (kitap_adi, kitap_yazari, okunma_durumu, begeni, kullanici_id) VALUES (?, ?, ?, ?, ?)"
    imlec.execute(sorgu, (kitap_adi, kitap_yazari, okunma_durumu, begeni, kullanici_id))
    vt.commit()
    print("Kitap başarıyla eklendi.")

# Kitap güncelle
def kitap_guncelle(kullanici_id, kitap_id, okunma_durumu, begeni):
    sorgu = "UPDATE kitaplik_tb SET okunma_durumu = ?, begeni = ? WHERE kitap_id = ? AND kullanici_id = ?"
    imlec.execute(sorgu, (okunma_durumu, begeni, kitap_id, kullanici_id))
    vt.commit()
    print("Kitap bilgileri güncellendi.")

# Kitap sil
def kitap_sil(kullanici_id, kitap_id):
    sorgu = "DELETE FROM kitaplik_tb WHERE kitap_id = ? AND kullanici_id = ?"
    imlec.execute(sorgu, (kitap_id, kullanici_id))
    vt.commit()
    print("Kitap başarıyla silindi.")

# Ana döngü
while True:
    print("-" * 56)
    print("-" * 10, "Kitaplık Programımıza Hoş Geldiniz", "-" * 10)
    print("-" * 56)
    
    # Kullanıcı oturum açma veya kimlik doğrulama işlemleri burada yapılmalıdır.
    kullanici_id = 1  # Örnek olarak kullanici_id'yi sabit olarak ayarlıyoruz.
    
    print("-" * 10, "Yapmak istediğiniz işlemi Seçiniz", "-" * 10)
    print("-" * 10, "(1) Kütüphanemi Görüntüle, (2) Kitap Ekle, (3) Kitap Güncelle, (4) Kitap Sil, (5) Çıkış", "-" * 10)
    islem = input()
    
    if islem == "1":
        kullanici_kutuphanesi_goruntule(kullanici_id)
    elif islem == "2":
        kitap_adi = input("Kitap adını giriniz: ")
        kitap_yazari = input("Kitap yazarını giriniz: ")
        okunma_durumu = input("Okunma durumunu giriniz (1: Okundu, 0: Okunmadı): ")
        begeni = input("Beğeni değerini giriniz: ")
        kitap_ekle(kullanici_id, kitap_adi, kitap_yazari, okunma_durumu, begeni)
    elif islem == "3":
        kitap_id = input("Güncellemek istediğiniz kitabın ID'sini giriniz: ")
        okunma_durumu = input("Yeni okunma durumu (1: Okundu, 0: Okunmadı): ")
        begeni = input("Yeni beğeni değeri: ")
        kitap_guncelle(kullanici_id, kitap_id, okunma_durumu, begeni)
    elif islem == "4":
        kitap_id = input("Silmek istediğiniz kitabın ID'sini giriniz: ")
        kitap_sil(kullanici_id, kitap_id)
    elif islem == "5":
        vt.close()
        sys.exit()
    else:
        print("Geçersiz işlem. Lütfen tekrar deneyin.")
"""

