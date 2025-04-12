omo_peter = input('Skriv in ett ord: ')
omo_list = omo_peter.split()
for urkar in omo_list:
    if urkar.isupper():
        print(urkar)