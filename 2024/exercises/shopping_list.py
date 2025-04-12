# Open a file for writing, append if existing:
with open('groceries.txt', 'a') as f:   # append if existing - use 'a' if exists - vä öppnar filen groceries.txt i mode append - referenser lagras i variablen f
    print('Add to shopping list:')
    while True:
        item = input('? ')
        if item == '':
            break
        f.write(item + '\n')