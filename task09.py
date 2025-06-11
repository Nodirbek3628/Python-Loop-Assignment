import random    
                                           
pin = random.randint(1000,9999)

count = 0 
print("4 xonalik maxfiy raqam yaratadi")
print("7 urinish topib ko'ring")                        

while count < 8:
    option = int(input("maxfiy raqamni kiriting; "))
    count += 1

    if option > pin:
        print("Juda katta son:")

    elif option == pin:
        print("Tabriklaymz:")
        break
    else:
        print("Juda kichik son:")

else:
    print("afsus topolmadz")
    print(f"To'g'ri javob {pin}")