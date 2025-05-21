def dela_med(täljare, nämnare):
    if nämnare == 0:
        raise ZeroDivisionError('Kan ej dividera med 0')
    else:
        return täljare / nämnare

täljare = int(input('Ange täljare: '))
nämnare = int(input('Ange nämnare: '))
res = dela_med(täljare, nämnare)
print(res)
