# Skriv en funktion som tar två lika långa listor och returnerar en ny lika lång lista vars element är summan av elementen från de två givna listorna. Listorna ska alltså adderas elementvis.

def addera_elementvis(lst)):
    addition1 = []
    addition2 = []
    for i in range(len(lst1)):
        addition1 += lst[i]
    for i in range(len(lst2)):
        addition2 += lst[i]
    return addition1, addition2

lst1 = [1, 1, 2, 2, 3, 3]
lst2 = [0, 1, 2, 3, 4, 5]
summa = addera_elementvis(lst1, lst2)
print(summa)

L1 = [1, 1, 1, 4, 4]
L2 = [3, 5, 6, 0, -1]
total = addera_elementvis(L1, L2)
print(total)
