word = input('Skriv in ett ord: ')
reversed_word = word[::-1]

for i in range(len(word)):
    print(word[i], '-', reversed_word[i])
print()
