import random                                #PIN kod ochish o‘yini
random = random.randint(1000,9999)
print(random)
count = 0                          #Kompyuter 4 xonali maxfiy raqam (PIN) yaratadi.
                                   # Foydalanuvchi bu raqamni topishga harakat qiladi. Har urinishda:
while count < 8:
    option = int(input("maxfiy raqamni kiriting; "))
    count += 1
    if option > random:
        print("Juda katta son:")
        break
    elif option == random:
        print("Tabriklaymz:")
        break
    else:
        print("Juda kichik son:")
        break

else:
    print("Urinishlar soni tugadi",random)