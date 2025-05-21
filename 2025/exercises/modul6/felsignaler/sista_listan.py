# Addera alla numeriska värden i en lista
# Hoppa över om ej innehåller nummer
# Om numeriska värden saknas ska 0 returneras
# Inget felmeddelande ska anges

# skapa definitionen
def addera_numeriska(lst):
    # börja på 0
    res = 0
    try:
        # iterera för varje element i listan
        for item in lst:
            # lägg till alla element som float i res
            res += float(item)
    # om det blir ValueError ...
    except ValueError:
        # skippa
        pass
    # returnera resultat
    return res

l1 = [1, 2, 3, 4, 5, 'apa', 6.0]
summa = addera_numeriska(l1)
print(summa)
