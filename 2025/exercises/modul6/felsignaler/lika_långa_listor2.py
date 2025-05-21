def addera_elementvis(lst1, lst2):
    assert len(lst1) == len(lst2), "Ej lika långa"
    new_lst = []
    for i in range(len(lst1)):
        new_lst.append(lst1[i] + lst2[i])
    return new_lst

lst1 = [1, 1, 2, 2, 3, 3]
lst2 = [0, 1, 2, 3, 4, 5]
summa = addera_elementvis(lst1, lst2)
print(summa)

L1 = [1, 1, 1, 4, 4]
L2 = [3, 5, 6, 0, 2]
total = addera_elementvis(L1, L2)
print(total)
