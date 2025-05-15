# Skriv en funktion med namnet addera
# Addera summan av två tal

def addera(x, y):
    return x + y

tal_1 = int(input('Skriv ett tal: '))
tal_2 = int(input('Skriv ett annat tal: '))
summa = addera(tal_1, tal_2)
print(f'Summan av {tal_1} och {tal_2} är {summa}. ')
