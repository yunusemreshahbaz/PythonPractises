#BÖLÜM 1

#Soru 1
print("Soru 1")

msg1 = "Fonksiyona verilen değerleri (değişkenler, ifadeler, sabitler) ekrana yazdırır"
msg2 = "Metin ve değişkenleri birleştirmekte kullanılır"
msg3 = "Birden fazla değeri veya metni ekrana yazdırırken aralarına boşluk koymak amacıyla kullanılabilir"
msg4 = "Satır sonuna geçmek veya ayrı satıra yazdırmak istediğimizde de kullanırız"
print(msg1)
print(msg2)
print(msg3)
print(msg4)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")

#Soru 2
print("Soru 2")
isim = "Yunus Emre"
soyisim = "Şahbaz"
yasim = "22"
boyum = "1.80"
okul = "İzmir Ekonomi Üniversitesi"
sınıf = "4. sınıf"
bölüm = "Bilgisayar Mühendisliği"
message = "Python'u seviyorum"
print("Adım : " +isim)
print("Soyisim : " +soyisim)
print("Yasim : " +yasim)
print("Boyum : " +boyum)
print(okul+ "'nde okuyorum, " +sınıf+ " " + bölüm + " öğrencisiyim")
print(message)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")

#Soru 3
print("Soru 3")
print("Yorum satırları yazılan kodu açıklamak, belgelemek, not eklemek veya belirli bir kod bloğunu devre dışı bırakmak gibi amaçlarla kullanılır.")

print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")

#Soru 4
print("Soru 4")
# Bu program kullanıcının adını alıp selam veriyor

# Kullanıcıdan input ile ismi alınır
isim = input("Adınızı girin: ")

# Adı alındıktan sonra kullanıcıya selam verilir
print("Merhaba,", isim, "! Hoş geldiniz.")

print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")

#Soru 5
print("Soru 5")
print("Python'daki temel veri tipleri:")
print("Integer(int), float, String(str), Boolean(bool) ve NoneType(None)")

#int
yas=25
#float
pi=3.14
#str
isim = "Emre"
#Boolean
dogru_mu = True
yanlis_mi = False
#NoneType
degisken = None

#Verilerin print edilmesi:
print("Yaş:", yas, "Tipi:", type(yas))
print("Pi sayısı:", pi, "Tipi:", type(pi))
print("İsim:", isim, "Tipi:", type(isim))
print("Doğru mu?", dogru_mu, "Tipi:", type(dogru_mu))
print("Yanlış mı?", yanlis_mi, "Tipi:", type(yanlis_mi))
print("Değişken:", degisken, "Tipi:", type(degisken))

print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")

#Soru 6
print("Soru 6")
print("type() fonksiyonu bir değişkenin tipini döndürmek için kullanılır")
metin = "Merhaba, dünya!"
tip_metin = type(metin)
print("metin'in veri tipi : ", tip_metin)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")

#Soru 7
print("Soru 7")
ms1 = "Bir programlama dilinde değişken, bir değeri saklamak veya temsil etmek için kullanılan bir sembolik isimdir"
ms2 = "Değişkenlerin amaçları:"
ms3 = "Veri saklama, veri işleme, program akışını kontrol etmek, veri isimlendirme."
ms4 = "Değişkenleri tanımlarken dikkat edilmesi gerekenler:"
ms5 = "İsimlendirme kuralları -> Değişken adları, harf veya alt çizgi (_) ile başlamalıdır. Sayı ile başlayamaz."
ms6 = "İsimlerde büyük-küçük harf ayrımı vardır. Örneğin, 'isim', 'yas', 'total_puan'."
ms7 = "Anlamlı İsimlendirme -> Değişken adları, neyi temsil ettiklerini açık bir şekilde ifade etmelidir. Bu, kodun anlaşılabilirliğini artırır."
ms8 = "Değişken Türü -> Bazı programlama dillerinde değişken türleri belirtilirken, Python gibi dillerde bu otomatik olarak belirlenir."
ms9 = "Değer Atama -> Değişkenlere değer atamadan önce tanımlamalıyız. Örneğin, sayi = 5"
ms10 = "Tür Uyumu -> Python gibi dillerde değişken türü dinamik olarak değişebilir. Ancak bazı dillerde değişken türleri sabittir ve değişkenlere atanacak değerlerin türleri ile eşleşmelidir."
ms11 = "Özel İsimlerden Kaçınma -> Python'da özel anlam taşıyan anahtar kelimeleri değişken adı olarak kullanmaktan kaçınmalıyız."
ms12 = "Kod Stili -> Genel olarak kabul görmüş kodlama standartlarına uygun bir şekilde değişken adları yazmak kodun daha okunabilir ve uyumlu olmasını sağlar."

print(ms1)
print(ms2)
print(ms3)
print(ms4)
print(ms5)
print(ms6)
print(ms7)
print(ms8)
print(ms9)
print(ms10)
print(ms11)
print(ms12)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")

#Soru 8
print("Soru 8")
# Str
isimm = "Sarp"
soyisimm = "Yılmaz"

# Int
yass = 27
ogrenci_sayisi = 50

# Float
ortalama_nott = 85.5
pi = 3.14159265

# Boolean
dogru_muu = True
yanlis_mii = False

# NoneType (Değer Yok) veri tipi
bos_degisken = None

# Veri tiplerini ekrana yazdıralım
print("Ad:", isimm, "Soyad:", soyisimm)
print("Yaş:", yass, "Öğrenci Sayısı:", ogrenci_sayisi)
print("Ortalama Not:", ortalama_nott, "Pi Sayısı:", pi)
print("Doğru mu?", dogru_muu, "Yanlış mı?", yanlis_mii)
print("Boş Değişken:", bos_degisken)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")

#Soru 9
print("Soru 9")

ad = "Yunus Emre"
soyad = "Şahbaz"
yas = 22
boy = 1.81
ilgi_alanlari = ["Kodlamayı", "basketbol oynamayı"]

cikti = f"Adım {ad}, Soyadım {soyad}, Yaşım {yas}, Boyum {boy:.2f} metre. {ilgi_alanlari[0]} ve {ilgi_alanlari[1]} severim."

print(cikti)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")

#Soru 10
print("Soru 10")

ms13 = "Çoklu değişken ataması, bir veya daha fazla değişkene aynı anda değer atama işlemi yapmaktır."
ms14 = "Bu işlem, özellikle birbiriyle ilişkili değerleri gruplayarak atamak veya bir fonksiyondan birden fazla değeri döndürmek için kullanışlıdır."

print(ms13)
print(ms14)

# Örnek
print("Örnek;")
iad, isoyad = "Yunus Emre", "Şahbaz"
iyas, iboy = 22, 1.81
iilgi_alanlarim = ["Kodlama", "Basketbol"]

print("Ad:", iad)
print("Soyad:", isoyad)
print("Yaş:", iyas)
print("Boy:", iboy)
print("İlgi Alanları:", iilgi_alanlarim)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")

#Soru 11
print("Soru 11")

msg5 = "Shell ekranında aşağıdaki komutları çalıştırdığımda olanlar:"
msg6 = "10+20 -> 10 ile 20'yi toplar ve sonucu (30) yazdırır"
msg7 = "4*30 -> 4 ile 30'u çarpar ve 120 yazdırır"
msg8 = "2**1000 -> 2 üzeri 1000'i yazdırır"
msg9 = "print('merhaba') -> 'merhaba' yazdırır"
msg10 = "36/4*(3+2)*4+2 -> matematik kurallarına uyarak işlemleri yapar ve 182.0 yazdırır"

print(msg5)
print(msg6)
print(msg7)
print(msg8)
print(msg9)
print(msg10)
