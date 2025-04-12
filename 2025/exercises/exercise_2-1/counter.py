# print numbers
i = int(input('Enter a number: '))

if i <= 10:
    print('Countdown... ')
    while i > 0:
        print(i, end=' ')
        i -= 1
    print()
elif i >= 10:
    print('To the skies... ')
    while i > 0 and i < 100:
        print(i + 1, end=' ')
        i += 1
    print()
