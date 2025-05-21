# Skriv en funktion som adderar alla numeriska värden i en lista. Om listan innehåller element som inte är numeriska, och därmed inte kan adderas, ska dessa hoppas över. Om numeriska värden saknas ska värdet 0 returneras. Inget felmeddelande ska ges.

def addera_numeriska(lst):
    res = 0
    try:
        for item in lst:
            res += float(item)
    except ValueError:
        pass
    return res

l1 = [1, 2, 3, 4, 5, 'apa', 6.0]
summa = addera_numeriska(l1)
print(summa)                       # 21.0
