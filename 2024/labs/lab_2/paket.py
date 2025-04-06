# Läs in totalvikt
total = int(input("Ange maxvikt (kg): "))

vikt = 0
count = 0

# Loopa tills den totala vikten överstiger maxvikten
while vikt <= total:
    vikt2 = int(input("Ange paketets vikt (kg): "))     # Läs in vikten av paket
    vikt += vikt2                                       # Lägg till paketets vikt till den totala vikten
    count += 1                                          # Öka räknaren för antalet paket

# Bryt loopen om den totala vikten överstiger maxvikten
    if vikt > total:
        print(f"Du kan lasta {count - 1} paket. Totalvikten är {vikt - vikt2} kg")
        break

# Bryt loopen om den totala vikten är exakt lika med maxvikten
    elif vikt == total:
        print(f"Du kan lasta {count} paket. Totalvikten är {vikt} kg")
        break