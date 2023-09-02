"""
gorevler = []
while True:
    gorev = input("Yapılacak bir görev giriniz (Bittiyse X giriniz): ")
    if gorev.lower() == "x":
        break
    else:
        gorevler.append(gorev)

print(gorevler)
while gorevler!=[]:
    bitenler = []
    for dd in range(len(gorevler)):
        durum = input(f'{gorevler[dd]} görevinizi yaptınız mı? e-h ?')
        if durum.lower() == "e":
            bitenler.append(dd)
    gorevler = gorevler - bitenler
else:
    print("Tüm görevler tamamlanmıştır")
"""

"""
x = 50

def myfunc():
    global x
    x = 300
    print(x)

def fonk2():
    print(x)

fonk2()
myfunc()
fonk2()
"""
"""
x=2
print("1. x =",x)
def fun1(a=15):
    x=10
    print("2. x =",x)
    return a
print("3. x =",x)
def fun2():
    x=20
    print("4. x =",x)
print("5. x =",x)
fun1()
fun2()
print("6. x =",x)
"""
gorevler = []

while True:
    gorev = input("Yapılacak bir görev giriniz (Bittiyse X giriniz): ")
    if gorev.lower() == "x":
        break
    else:
        gorevler.append(gorev)

print(gorevler)

while gorevler:
    bitenler = []
    for dd in range(len(gorevler)):
        durum = input(f'{gorevler[dd]} görevinizi yaptınız mı? e-h ?')
        if durum.lower() == "e":
            bitenler.append(gorevler[dd])
            for biten in bitenler:
                gorevler.remove(biten)
else:
    print("Tüm görevler tamamlanmıştır")
