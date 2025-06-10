
matn = input("Matn kiriting")        #So‘zdagi katta harflarni sanang
             
soni = 0

for belgi in matn:
    if belgi.isupper():
        soni += 1

print("Katta harflar soni:", soni)
