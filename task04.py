import random 

a = random.randint(1,20)
print(a)
                #Random son topish o‘yini,kompyuter 1 dan 20 gacha tasodiy sonni randint bilan tanlaydi.foydalanuchi tug'ri topmaghincha qayta kiritaveradi
while True:
    option = int(input("sonni kiritin:"))
    if option == a:
        print("Topdingiz:")
        break
    else:
        print("sonni qayta kiriting")