def addera_numeriska(lst):
    # spara resultatet i res
    res = 0
    # försök ...
    try:
        # iterera för varje item i listan
        for item in lst:
            # lägg till alla item i res
            res += float(item)
    # om ValueError sker ...
    except ValueError:
        # skippa
        pass
    # returnera värdet
    return res

l1 = [1, 2, 3, 4, 5, 'apa', 6.0]
summa = addera_numeriska(l1)
print(summa)                       # 21.0
