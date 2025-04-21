numbers = input('Skriv in nummer ').split()
str = ['måndag', 'tisdag', 'onsdag', 'torsdag', 'fredag', 'lördag', 'söndag']

numbers2 = [int(x) for x in numbers]

for i in numbers2:
    print(str[i])
