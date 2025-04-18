m = int(input('Hur många minuter?: '))
p = int(input('Hur mycket kostar det per minut?: '))
t = m * p

if t >= 300:
    t = t * 0.90
    print(f'Det kostar {t} kr i månaden. Du har rabatt. ')
else:
    print(f'Det kostar {t} kr i månaden. Du har ej rabatt. ')
