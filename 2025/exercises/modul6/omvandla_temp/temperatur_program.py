import temperatur

c = float(input('Temperatur i Celcius: '))
f = temperatur.c2f(c)
print(f'Temperatur i Fahrenheit: {f}')

f2 = float(input('Temperatur i Fahrenheit: '))
c2 = temperatur.f2c(f2)
print(f'Temperatur i Celcius: {c2:.2f}')
