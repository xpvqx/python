s = 'Some sensitive information'

for c in s:                 # c är ett variable namn vi har valt, spara alla karaktärer i s(ordet)
    if c in 'aeiouy':       # om c är en volak
        print('*', end='')  # print '*'
    else:
        print(c, end='')    # annars printa c = character i s
