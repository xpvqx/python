mätvärden = input('Mätvärden: ')
lst_data = mätvärden.split()
data = [float(x) for x in lst_data] # använd list comprehension här
summa = sum(data)
print(f'Summan av de inmatade värdena är {summa}')
