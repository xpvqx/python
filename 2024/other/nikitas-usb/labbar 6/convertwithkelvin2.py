import convertwithkelvin as kelv

c = float(input('temperatur i Celsius: '))
f = kelv.c2f(c)
print(f'Temperatur i Fahrenheit: {f}')

f2 = float(input('Temperatur i Fahrenheit: '))
c2 = kelv.f2c(f2)
print (f'temperatur i Celsius: {c2:.2f}')
