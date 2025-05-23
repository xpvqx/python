# Läs in max last och vikt per paket
# Matar in paket sålänge maxlasten inte överskids

nuvarande_vikt = 0
antal_paket = 0

max_vikt = int(input('Ange maxvikt (kg): '))

while max_vikt > nuvarande_vikt:
    paket_vikt = int(input('Paketets vikt (kg): '))
    nuvarande_vikt += paket_vikt
    antal_paket += 1

    if nuvarande_vikt > max_vikt:
        print(f'Du kan lasta {antal_paket - 1} paket. Totalvikten är {nuvarande_vikt - paket_vikt} kg.')
        break
    elif nuvarande_vikt == max_vikt:
        print(f'Du kan lasta {antal_paket} paket. Totalvikten är {nuvarande_vikt} kg.')
        break
