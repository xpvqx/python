import math

# om man känner till längd för a och b, samt vinkeln v mellan dessa sidor
# kan man räkna ut längden av sidan c med formeln:
# c = sqrt(a ** 2 + b ** 2 - 2abcos(v))

# läs in längderna på två sidor i en triangel och vinkeln mellan sidorna
# avgör om triangeln är liksidig (alla sidor lika), likbent (två sidor lika)
# eller oliksidigt (inga sidor lika)

a = int(input('Hur lång är första sidan? '))
b = int(input('Hur lång är andra sidan? '))
v = int(input('Vad är vinkeln mellan dessa sidor? '))

# räkna ut tredje sidan
c = math.sqrt((a ** 2) + (b ** 2) - (2 * a * b * math.cos(v)))

if (a == b == c):
    print(f'Triangeln är liksidig')
elif (a == b) or (a == c) or (b == c):
    print(f'Triangeln är likbent')
else:
    print(f'Triangeln är oliksidig')
