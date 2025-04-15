s = 'Some sensitive word'

for c in s:
    if c in 'aeiouy':
        print('*', end='')
    else:
        print(c, end='')
