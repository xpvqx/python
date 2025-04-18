# byt ut q mot k, och w mot v
ord = input('Ange ett ord med gammal stavning: ')
ord2 = ''

for c in ord:
    if c == 'q':
        ord2 += 'k'     # byt ut till k - lägg till i ord2
    elif c == 'w':
        ord2 += 'v'     # byt ut till v
    else:
        ord2 += c       # annars lägg till c i ord2
print(ord2)


# 1. Iterera för varje bokstav (c) i ordet
# 2. Om bokstaven är 'q̈́' ...
# 3. Lägg till bokstaven 'k' i nya ordet
# 4. Eller om bokstaven är 'w' ...
# 5. Lägg till bokstaven 'v' i nya ordet
# 6. Annars; Lägg till varje bokstav i ordet i nya ordet
