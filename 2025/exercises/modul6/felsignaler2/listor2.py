# addera alla numeriska värden i en lista
# om listan innehåller element som ej är numeriska - skippa
# om numeriska värden saknas ska värdet 0 returneras

def addera_numeriska(lst):
    res = 0
    for item in lst:
        try:
            res += float(item)
        except ValueError:
            pass
    return res

l1 = [1, 2, 3, 4, 5, 'apa', 6.0]
summa = addera_numeriska(l1)
print(summa)                       # 21.0
