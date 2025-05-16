def medelvärde(lst):
    summa = sum(lst)
    n = len(lst)
    return summa / n

mätvärden = input('Mätvärden: ').split()
lst = [float(x) for x in mätvärden]
mv = medelvärde(lst)

print(f'Medelvärdet av de inmatade värdena är {mv}.')
