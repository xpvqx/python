max_vikt = int(input('Ange maxvikt (kg): '))        # läs in max_vikt
paket_vikt = int(input('Paketets vikt (kg): '))     # läs in paketet_vikt

antal_paket = 0                                     # ställ in antal_paketet till värde 0
total_vikt = 0                                      # ställ in total_vikt till värde 0

if paket_vikt >= max_vikt:                           # printa och avsluta om paket_vikt > max_vikt 
    print('Du kan lasta 0 paket. Totalvikten är 0 kg. ')
else:                                               # annars..
    antal_paket += 1                                # öka antalet paket med 1
    total_vikt = paket_vikt                         # sätt totalata vikten till första paketets vikt

    while True:                                     # fortsätt tills maxvikten är nådd
        paket_vikt2 = int(input('Paketets vikt (kg): '))
        if total_vikt + paket_vikt2 > max_vikt:
            break                                   # avsluta om vikten > maxvikt
        total_vikt += paket_vikt2                   # addera vikten på totalvikten
        antal_paket += 1                            # öka antal_paket med 1

print(f'Du kan lasta {antal_paket} paket. Totalvikten är {total_vikt} kg. ')
