
text = input("Matn kiriting: ")        #Stringdagi unli harflarni sanang

vowel_latters = "aeiou"        #unli harflar
count = 0

for belgi in text.lower():
    if belgi in vowel_latters:
        count += 1

print("Unli harflar soni:",count)       # Natijani chiqarish
