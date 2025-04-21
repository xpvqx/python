lst = [3, 0, -2, 1, 1, -1, -2, 3, 2, 3, 0]
for i in range(len(lst)):
    # om det aktuella elementet är negativt:
    if lst[i] < 0:
        lst[i] = 0
        # sätt elementet till 0
print(lst)
