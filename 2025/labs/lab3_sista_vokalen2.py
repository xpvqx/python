word = input('Skriv in ett ord: ')
vowels = 'aouåeiyäöAOUÅEIYÄÖ'

for i in range(len(word) - 1, -1, -1):
    if word[i] in vowels:
        word = word[:i] + word[i] * 3 + word[i+1:]
        break
print(word)
print()
