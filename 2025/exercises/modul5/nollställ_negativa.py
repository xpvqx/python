# definera funktionen
def nollställda_negativa(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i] = 0

värden = [4, 0, -3, 5, 1, -1]

nollställda_negativa(värden)

print(värden)
