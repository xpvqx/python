vowel = 'AaåäEeIiOoöUuYy'
word = input('Write a word: ')

for c in word:
    if c in vowel:
        print('*', end='')
    else:
        print(c, end='')
print()
