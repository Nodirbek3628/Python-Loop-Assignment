pasword = input("haqiqiy parolni kiriting:").isalnum                 #Parol tasdiqlovchi

for i in range(3):                              #parol kiritiladi kiritilgandan so'ng parol 3 ta urinishda ham to'ri bulmasa bloklanadi
    option = input("parolni kiriting:")
    
    if option == pasword:
        print("to'g'ri kiritdingiz:")
        break
    elif option != pasword:
        print("yana o'rini ko'ring:")
else:
    print("Bloklandz.")
