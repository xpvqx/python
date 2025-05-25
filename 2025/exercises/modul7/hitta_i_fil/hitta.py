filename = input('Filnamn?: ')
ordet = input('Ord att leta efter: ')

with open(filename, encoding='utf-8') as f:
    content = f.readlines()

for i, line in enumerate(content):
    if ordet in line:
        print(line, end='')
