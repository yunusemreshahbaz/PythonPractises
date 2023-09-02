#import os 
dosya_yolu = r"C:\Users\Yunus_Emre\Desktop\deneme.txt"
try:
    
    # Dosyayı "a" (append) modunda aç
    with open(dosya_yolu, "a") as dosya:
        dosya.write("Eklenen Satır.\n")

    print("Dosyaya ekleme işlemi tamamlandı.")

    # Dosyanın konumunu başa al
    with open(dosya_yolu, "r") as dosya:
        icerik = dosya.read()
        print(icerik)

    #Dosyayı "w" (write) modunda açarak overwrite et
    with open(dosya_yolu, "w") as dosya:
        dosya.write("Overwrite ettin!\n")

    print("Overwrite tamamlandı.")

    # Dosyanın konumunu tekrar başa al
    with open(dosya_yolu, "r") as dosya:
        icerik = dosya.read()
        print(icerik)

except FileNotFoundError:
    print("Dosya bulunamadı")

# os.remove("deneme.txt") # yukarıdaki 'import' methodu ile deneme dosyasını sil
