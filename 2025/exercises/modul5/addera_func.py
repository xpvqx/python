# Skriv en funktion med namnet addera som tar två tal som parametrar. Funktionen ska returnera summan av de två talen. Placera funktionen på ett lämpligt ställe i följande kodruta så att anropet fungerar.

def addera(x, y):
    return(x + y)

tal_1 = int(input('Skriv in ett tal: '))
tal_2 = int(input('Skriv in ett annat tal: '))
summa = addera(tal_1, tal_2)

print(f'Summan av {tal_1} och {tal_2} är {summa}.')
