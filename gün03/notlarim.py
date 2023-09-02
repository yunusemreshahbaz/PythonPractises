burger = input("1 tavuklu, 2 köfteli, 3 sebzeli: ")
icecek = input("1 ayran, 2 kola, 3 soda: ")
patates = input("1 küçük, 2 orta, 3 büyük: ")

tutar = 0

if burger == "1":
    tutar += 50
    burger = "tavuklu"
elif burger == "2":
    tutar += 80
    burger = "köfteli"
elif burger == "3":
    tutar += 65
    burger = "sebzeli"
else:
    tutar += 0
    burger = "seçilmedi"
    

if icecek == "1":
    tutar += 10
    icecek = "ayran"
elif icecek == "2":
    tutar += 50
    icecek = "kola"
elif icecek == "3":
    tutar += 15
    icecek = "soda"
else:
    tutar += 0
    icecek = "seçilmedi"


if patates == "1":
    tutar += 5
    patates = "küçük"
elif patates == "2":
    tutar += 10
    patates = "orta"
elif patates == "3":
    tutar += 20
    patates = "büyük"
else:
    tutar += 0
    patates = "seçilmedi"
    
    

siparis = """Siparişiniz Hazır
            Burger seçiminiz : {},
            Patates seçiminiz : {},
            İçecek seçiminiz : {},
            Toplam Hesabınız : {}""".format(burger, patates, icecek, tutar)

print(siparis)
