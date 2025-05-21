# Multiplicera alla tal i en tupel och skriv ut resultatet

data = (3, 1, 4, 3, 2, 2, 1)
res = 1

for item in data:
    print(item)
    res *= item 
print(res)      # 3 * 1 * 4 * 3 * 2 * 2 * 1 = 144
