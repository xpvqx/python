# Skriv ett program som läser in en serie datum från användaren. Datumen ska
# anges på formatet ååmmdd. Alla datum antas vara på 2000-talet. Programmet ska
# skriva ut varje datum på en egen rad på formatet dd månad åååå, där månaden
# skrivs ut med små bokstäver, på svenska. Dagen ska inte anges med en
# inledande nolla. Årtalet ska anges med fyra siffror.

månader = ['januari', 'februari', 'mars', 'april', 'maj', 'juni', 'juli', 
            'augusti', 'september', 'oktober', 'november', 'december']

datum_lista = input('Ange ett datum (ÅÅMMDD): ').split()

for datum in datum_lista:
    år = '20' + datum[:2]
    månad = datum[2:4]
    dag = datum[4:]

    månad_namn = månader[int(månad) - 1]
    dag = str(int(dag))

    print(dag, månad_namn, år)
print()
