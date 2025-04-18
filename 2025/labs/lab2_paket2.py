nuvarande_vikt = 0
antal_paket = 0

ange = int(input("Ange maxvikt (kg): "))

while ange > nuvarande_vikt:
    paket = int(input("Paketets vikt (kg): "))
    nuvarande_vikt += paket
    antal_paket +=1
    if nuvarande_vikt > ange:
        print(f"Du kan lasta {antal_paket - 1} paket. Totalvikten är {nuvarande_vikt - paket} kg.")
        break
    elif nuvarande_vikt == ange:
        print(f"Du kan lasta {antal_paket} paket. Totalvikten är {nuvarande_vikt} kg.")
        break
print()
