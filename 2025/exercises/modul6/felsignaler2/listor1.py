# använd assert för att kontrollera om två listor är lika långa
# listorna ska adderas elementvis

def addera_elementvis(lst1, lst2):
    # Kontrollera om listorna är samma längd
    assert len(lst1) == len(lst2), 'Ej samma längd'
    # Skapa ny lista för att spara den summerade listan
    new_lst = []
    # Iterera över varje element i första listan
    for i in range(len(lst1)):
        # Lägg till varje element i båda listorna i new_lst
        new_lst.append(lst1[i] + lst2[i])
    # Returnera nya listan
    return new_lst

lst1 = [1, 2, 2, 2, 3, 3]
lst2 = [0, 1, 2, 3 ,4 ,5]
summa = addera_elementvis(lst1, lst2)
print(summa)

L1 = [1, 1, 1, 4, 4]
L2 = [3, 5, 6, 0]
total = addera_elementvis(L1, L2)
print(total)
