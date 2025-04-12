# Läs in ett ord från användaren
ett_ord = (input('Skriv in ett ord: '))
avstavat = ''                           # Skapa en tom sträng som ska innehålla det nya ordet

for i in range(len(ett_ord) -1):        # Iterera över alla positioner i ordet, förutom den sista   
    avstavat += ett_ord[i] + '-'        # Lägg till bokstaven på den givna positionen och ett bindestreck
avstavat += ett_ord[-1]                 # Lägg till den sista bokstaven

print(avstavat)                         # Skriv ut resultatet