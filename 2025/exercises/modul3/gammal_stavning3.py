# change q to k and w to v

word = input('Write a word: ')  # user input
word2 = ''                      # create empty string to replace

for c in word:
    if c == 'q':
        word2 += 'k'
    elif c == 'w':
        word2 += 'v'
    else:
        word2 += c
print(word2)
