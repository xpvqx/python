# läs in maxvikt och vikt per paket
# mata in paket tills maxlasten överskrids

max_vikt = int(input('Ange maxvikt (kg): '))
nuvarande_vikt = 0
antal_paket = 0

while max_vikt > nuvarande_vikt:
    paket_vikt = int(input('Ange paketets vikt (kg): '))
    nuvarande_vikt += paket_vikt
    antal_paket += 1

    if nuvarande_vikt > max_vikt:
        print(f'Du kan lasta {antal_paket - 1} paket.', end=' ')
        print(f'Totalvikten är {nuvarande_vikt - paket_vikt} kg.')
        break

    elif nuvarande_vikt == max_vikt:
        print(f'Du kan lasta {antal_paket}.', end=' ')
        print(f'Totalvikten är {nuvarande_vikt} kg.')
        break
