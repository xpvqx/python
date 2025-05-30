# En budfirma ska lasta paket för utkörning i en bil. Bilen har en
# maxlast den kan ta och paketen har olika vikt. Paketen måste packas i
# den ordning de kommer, utan att maxlasten överskrids.
#
# Skriv ett program som läser in en maxlast och vikt per paket.
# Användaren matar in paket så länge maxlasten inte överskrids.
#
# Spara koden i en fil med namnet paket.py.

max_vikt = int(input('Ange maxvikt (kg): '))
paket = 0
nuvarande_vikt = 0

while max_vikt > nuvarande_vikt:
    paket_vikt = int(input('Paketets vikt: '))
    paket += 1
    nuvarande_vikt += paket_vikt

    if nuvarande_vikt > max_vikt:
        print(f'Du kan lasta {paket - 1} paket.')
        print(f'Totalvikten är {nuvarande_vikt - paket_vikt} kg')
    
    elif nuvarande_vikt == max_vikt:
        print(f'Du kan lasta {paket} paket. Totalvikten är {nuvarande_vikt}')
