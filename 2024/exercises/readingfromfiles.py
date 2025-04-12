f = open('/home/karl/Documents/test.txt')
for row in f:
    print(row, end='')
f.close()