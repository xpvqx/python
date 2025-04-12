ord = input('Skriv ett ord: ')
första = ord[0]        # strängens första tecken
fjärde = ord[3]       # strängens fjärde tecken
sista = ord[-1]          # strängens sista tecken: kom ihåg att vi inte vet hur lång strängen är!
baklänges = ord[::-1]      # använd slicing för att vända på strängen
print(f'Ordet börjar på {första} och slutar på {sista}.')
print(f'Ordets fjärde bokstav är {fjärde}.')
print(f'Baklänges blir det {baklänges}.')