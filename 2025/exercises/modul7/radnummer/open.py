filename = input('Filname: ')

with open(filename) as f:
    content = f.readlines()

# for i in range(len(content)):
#     line = content[i]
#     print(i, line[:-1])

# samma sak:
for i, line in enumerate(content):
    print(i, line[:-1])
