# Skriv ett program som läser in en serie datum från användaren. Datumen ska
# anges på formatet ååmmdd. Alla datum antas vara på 2000-talet. Programmet ska
# skriva ut varje datum på en egen rad på formatet dd månad åååå, där månaden
# skrivs ut med små bokstäver, på svenska. Dagen ska inte anges med en inledande
# nolla. Årtalet ska anges med fyra siffror.
#
# Spara koden i en fil med namnet datum.py.
#
# Följande är ett exempel på hur det kan se ut när programmet körs
#
# $ python datum.py Skriv in en serie datum: 130522 061103 220214 001209 22 maj
# 2013 3 november 2006 14 februari 2022 9 december 2000
#
# Du får inte lösa uppgiften med en if- eller match-sats.

datum_input = input('Skriv in en serie datum: ')
datum_lista = datum_input.split()

månader = [
    'januari',
    'februari',
    'mars',
    'april',
    'maj',
    'juni',
    'juli',
    'augusti',
    'september',
    'oktober',
    'november',
    'december'
]

for datum in datum_lista:
    år = '20' + datum[:2]
    månad = datum[2:4]
    dag = datum[4:]

    
    månad_namn = månader[int(månad) - 1]

    # gör om till string, tar bort nollan i början
    dag = str(int(dag))

    print(dag, månad_namn, år)
print()
