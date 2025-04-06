lst = [41, 39, 26, 32, 40, 46, 51, 37]
först = lst[0]          # listans första element
sist = lst[-1]        # listans sista element
minst =  min(lst)        # listans minsta element
störst = max(lst)        # listans största element
summa =   sum(lst)         # summan av listans element
antal =  len(lst)         # antal element i listan, listans längd
print(först, sist, minst, störst, summa, antal)


lsti = [3, 0, -2, 1, 1, -1, -2, 3, 2, 3, 0]
ls = []
for item in lsti:
    # om item är positivt:
    if item >= 0:
        ls += str(item)
        # skriv ut item, avsluta med mellanslag

print(ls)