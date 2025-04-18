# multiplicera vokalerna

word = input('Write a word: ')
vowels = 'AaåäEeIiOoöUuYy'

for c in word:
    if c in vowels:
        print(c * 3, end='')
    else:
        print(c, end='')
print()
